#!/usr/bin/env python3
"""
SRE stage 1 — MEASURE (facts only, no semantics).
Part of SAUND REVERSE ENGINE v0.1. Does NOT touch SAUND core.
Usage: python sre/analyze.py track.mp3 -o measured.json
Requires: pip install librosa numpy
"""
import argparse, json
import numpy as np
import librosa

KEY_NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
MAJOR_T = [6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]
MINOR_T = [6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17]

def est_key(chroma):
    best = (None, -2.0)
    for sh in range(12):
        for mode, tpl in (("major", MAJOR_T), ("minor", MINOR_T)):
            score = float(np.corrcoef(chroma.mean(axis=1), np.roll(tpl, sh))[0,1])
            if score > best[1]: best = (f"{KEY_NAMES[sh]} {mode}", score)
    return best

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("-o","--out",default="measured.json")
    ap.add_argument("--sections", type=int, default=8)
    a = ap.parse_args()

    y, sr = librosa.load(a.audio, sr=None, mono=True)
    dur = float(librosa.get_duration(y=y, sr=sr))
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beats = librosa.frames_to_time(beats, sr=sr)

    # beat periodic strength -> is there a beat at all?
    if len(beats) > 4:
        ibi = np.diff(beats)
        beat_conf = float(1.0 - np.std(ibi)/max(np.mean(ibi),1e-6))
    else:
        beat_conf = 0.0

    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    key, key_conf = est_key(chroma)

    # sections by energy
    rms = librosa.feature.rms(y=y)[0]
    t = librosa.frames_to_time(np.arange(len(rms)), sr=sr)
    bounds = np.linspace(0, len(rms), a.sections+1).astype(int)
    secs = []
    for i,(s,e) in enumerate(zip(bounds[:-1], bounds[1:])):
        seg = y[int(t[s]*sr):int(t[e]*sr)]
        if len(seg) < sr: seg = np.pad(seg, (0, sr-len(seg)))
        sp = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))**2
        f = np.fft.rfftfreq(len(seg), 1/sr)
        band = lambda lo,hi: float(sp[(f>=lo)&(f<hi)].sum()/max(sp.sum(),1e-9))
        secs.append({
            "idx": i, "section_idx": i,
            "t_start": round(float(t[s]),2), "t_end": round(float(t[e]),2),
            "rms": round(float(rms[s:e].mean()),5),
            "low_20_120": band(20,120),        # sub/bass presence
            "mid_120_2k": band(120,2000),      # body / vocal region
            "high_2k_8k": band(2000,8000),     # harshness / mosquito region
            "air_8k_16k": band(8000,16000),
            "transient_density": round(float(
                len(librosa.onset.onset_detect(y=seg, sr=sr))/max(dur/a.sections,1e-6)),3),
        })

    # silence gaps > 0.5s (gated silence candidates)
    sil = []
    thr = float(np.percentile(rms, 5)) * 1.5
    in_s = None
    for i in range(len(rms)):
        if rms[i] < thr and in_s is None: in_s = t[i]
        elif rms[i] >= thr and in_s is not None:
            if t[i]-in_s > 0.5: sil.append([round(float(in_s),2), round(float(t[i]),2)])
            in_s = None

    out = {
        "source": a.audio, "sre_stage": 1,
        "duration_s": round(dur,2),
        "tempo_bpm": int(tempo), "tempo_conf": "HIGH",
        "beat_periodicity": round(beat_conf,3),
        "beat_conf": "HIGH" if beat_conf > 0.6 else ("MEDIUM" if beat_conf > 0.3 else "LOW"),
        "key": key, "key_conf": round(key_conf,3),
        "sections": secs, "section_conf": "LOW",
        "silence_gaps_s": sil,
        "note": "facts only; semantics assigned at SRE stage 2",
    }
    json.dump(out, open(a.out,"w"), indent=2, ensure_ascii=False)
    print(f"[SRE stage1] wrote {a.out}")
    print(f"[SRE stage1] tempo={out['tempo_bpm']} beat_conf={out['beat_conf']} "
          f"key={key}({key_conf:.2f}) gaps={len(sil)}")

if __name__ == "__main__":
    main()
