#!/usr/bin/env python3
"""
SRE stage 2 — MAP SEMANTICS (facts → SAUND vocabulary).
Part of SAUND REVERSE ENGINE v0.1. Does NOT touch SAUND core.
Usage: python sre/map_semantics.py measured.json -o semantic.json
"""
import argparse, json
import numpy as np

BEAT_THRESHOLDS = {
    "HIGH_BEAT": 0.6,
    "MEDIUM_BEAT": 0.3,
}

SPECTRAL_BAND_THRESHOLDS = {
    "sub_dominant": 0.3,
    "mid_dominant": 0.4,
    "high_harsh": 0.15,
    "air_bright": 0.1,
}

TRANSIENT_THRESHOLDS = {
    "high_density": 2.0,
    "medium_density": 0.5,
}

SILENCE_GAP_THRESHOLD = 0.5

def map_beat_to_groove(beat_conf_value, tempo_bpm):
    if beat_conf_value > BEAT_THRESHOLDS["HIGH_BEAT"]:
        if tempo_bpm > 130:
            return {"pattern": "FOUR_ON_FLOOR", "confidence": "HIGH", "slot": "KCK"}
        elif tempo_bpm > 100:
            return {"pattern": "BREAKBEAT", "confidence": "HIGH", "slot": "KCK"}
        else:
            return {"pattern": "HALF_TIME", "confidence": "HIGH", "slot": "KCK"}
    elif beat_conf_value > BEAT_THRESHOLDS["MEDIUM_BEAT"]:
        return {"pattern": "SYNCOPATED_TECH", "confidence": "MEDIUM", "slot": "KCK"}
    else:
        return {"pattern": "NO_BEAT", "confidence": "HIGH", "slot": "KCK",
                "note": "BROKEN_GRID, FX_EVENTS_ONLY"}

def map_spectral_to_timbre(sections):
    timbre_slots = []
    for sec in sections:
        sec_timbre = []
        if sec["low_20_120"] > SPECTRAL_BAND_THRESHOLDS["sub_dominant"]:
            sec_timbre.append({"slot": "SUB", "profile": "sine-deep", "confidence": "HIGH"})
            sec_timbre.append({"slot": "BAS", "profile": "filthy-elastic", "confidence": "MEDIUM"})
        if sec["mid_120_2k"] > SPECTRAL_BAND_THRESHOLDS["mid_dominant"]:
            sec_timbre.append({"slot": "VOCAL", "profile": "forward", "confidence": "MEDIUM",
                               "note": "vocal-band detected; do NOT add to INST-MAP"})
        if sec["high_2k_8k"] > SPECTRAL_BAND_THRESHOLDS["high_harsh"]:
            sec_timbre.append({"slot": "SAW", "profile": "mosquito-squeal",
                             "confidence": "MEDIUM", "note": "4-8kHz harsh"})
        if sec["air_8k_16k"] > SPECTRAL_BAND_THRESHOLDS["air_bright"]:
            sec_timbre.append({"slot": "ATM", "profile": "bright-wide", "confidence": "LOW"})
        if not sec_timbre:
            sec_timbre.append({"slot": "PAD", "profile": "drone", "confidence": "LOW"})
        timbre_slots.append({"section_idx": sec["section_idx"], "timbre": sec_timbre})
    return timbre_slots

def map_transients_to_percussion(sections):
    perc_map = []
    for sec in sections:
        if sec["transient_density"] > TRANSIENT_THRESHOLDS["high_density"]:
            perc_map.append({"section_idx": sec["section_idx"],
                           "slot": "PRC", "profile": "metal-tick/chain-rattle",
                           "confidence": "MEDIUM"})
        elif sec["transient_density"] > TRANSIENT_THRESHOLDS["medium_density"]:
            perc_map.append({"section_idx": sec["section_idx"],
                           "slot": "HAT", "profile": "tight-metallic",
                           "confidence": "LOW"})
        else:
            perc_map.append({"section_idx": sec["section_idx"],
                           "slot": "ATM", "profile": "sparse-texture",
                           "confidence": "LOW"})
    return perc_map

def map_silence_to_sfx(silence_gaps):
    sfx_candidates = []
    for gap in silence_gaps:
        duration = gap[1] - gap[0]
        if duration > SILENCE_GAP_THRESHOLD:
            sfx_candidates.append({
                "type": "GATED_SILENCE",
                "t_start": gap[0], "t_end": gap[1],
                "duration": round(duration, 2),
                "confidence": "HIGH"
            })
    return sfx_candidates

def map_sections_to_arc(sections, beat_conf_value):
    if not sections: return []
    energy = [s["rms"] for s in sections]
    energy_norm = np.array(energy) / max(max(energy), 1e-6)
    arc_codes = []
    n = len(sections)
    for i, e in enumerate(energy_norm):
        if i == 0: arc_codes.append("I")
        elif i == n - 1: arc_codes.append("O")
        elif e < 0.3: arc_codes.append("R" if i < n // 2 else "P")
        elif e < 0.6: arc_codes.append("G" if i < n // 2 else "S")
        else: arc_codes.append("K" if i < n // 2 else "F")
    return {"arc": arc_codes, "confidence": "LOW",
            "note": "heuristic energy-based; verify manually"}

def map_key_to_harmony(key_str, key_conf):
    if key_conf < 0.3:
        return {"key": "atonal", "mode": "dissonant", "confidence": "LOW"}
    parts = key_str.split()
    if len(parts) != 2:
        return {"key": "unknown", "mode": "unknown", "confidence": "LOW"}
    return {"key": parts[0], "mode": parts[1],
            "confidence": "HIGH" if key_conf > 0.5 else "MEDIUM"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("measured")
    ap.add_argument("-o", "--out", default="semantic.json")
    a = ap.parse_args()
    measured = json.load(open(a.measured))
    semantic = {
        "source": measured["source"], "sre_stage": 2,
        "groove": map_beat_to_groove(measured["beat_periodicity"], measured["tempo_bpm"]),
        "timbre_slots": map_spectral_to_timbre(measured["sections"]),
        "percussion": map_transients_to_percussion(measured["sections"]),
        "sfx_candidates": map_silence_to_sfx(measured["silence_gaps_s"]),
        "arc": map_sections_to_arc(measured["sections"], measured["beat_periodicity"]),
        "harmony": map_key_to_harmony(measured["key"], measured["key_conf"]),
        "tempo_bpm": measured["tempo_bpm"], "duration_s": measured["duration_s"],
        "sections": measured["sections"],
        "note": "semantic mapping complete; next stage emits .saund + supplements"
    }
    json.dump(semantic, open(a.out, "w"), indent=2, ensure_ascii=False)
    print(f"[SRE stage2] wrote {a.out}")
    print(f"[SRE stage2] groove={semantic['groove']['pattern']} "
          f"arc={semantic['arc']['arc']} harmony={semantic['harmony']['key']} {semantic['harmony']['mode']}")

if __name__ == "__main__":
    main()
