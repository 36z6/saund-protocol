#!/usr/bin/env python3
"""
SRE A/B comparator — fingerprint distance between two measured.json.
Usage: python sre/compare.py out_A/measured.json out_B/measured.json
Score 0..1 (1 = identical sonic DNA). Acceptance threshold: 0.70.
"""
import argparse, json, sys
import numpy as np

def band_vec(m):
    v = []
    for s in m["sections"]:
        v += [s["low_20_120"], s["mid_120_2k"], s["high_2k_8k"], s["air_8k_16k"]]
    return np.array(v, dtype=float)

def cos(a, b):
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b")
    ap.add_argument("--threshold", type=float, default=0.70)
    x = ap.parse_args()
    A, B = json.load(open(x.a)), json.load(open(x.b))

    band   = cos(band_vec(A), band_vec(B))
    beat   = 1.0 if A["beat_conf"] == B["beat_conf"] else 0.0
    key    = 1.0 if A["key"] == B["key"] else 0.0
    tempo  = max(0.0, 1.0 - abs(A["tempo_bpm"] - B["tempo_bpm"]) / 30.0)
    gA, gB = len(A["silence_gaps_s"]), len(B["silence_gaps_s"])
    gaps   = max(0.0, 1.0 - abs(gA - gB) / max(gA, gB, 1))

    score = 0.30*band + 0.20*beat + 0.20*key + 0.15*tempo + 0.15*gaps
    rows = [("spectral bands (cos)", band, 0.30), ("beat class", beat, 0.20),
            ("key", key, 0.20), ("tempo proximity", tempo, 0.15),
            ("silence-gap count", gaps, 0.15)]
    print("SRE A/B SCORECARD — fingerprint distance")
    print("-" * 52)
    for name, val, w in rows:
        print(f"  {name:<24} {val:.2f}  (weight {w:.2f})")
    print("-" * 52)
    print(f"  TOTAL SCORE: {score:.2f}  (threshold {x.threshold:.2f})")
    print(f"  VERDICT: {'PASS — sonic DNA reproduced' if score >= x.threshold else 'FAIL — calibrate stage 2 thresholds'}")
    sys.exit(0 if score >= x.threshold else 1)

if __name__ == "__main__":
    main()
