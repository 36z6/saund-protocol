#!/usr/bin/env python3
"""
SRE runner — one command for the whole reverse pipeline.
Part of SAUND REVERSE ENGINE v0.1. Does NOT touch SAUND core.
Usage:
  python sre/run.py track.mp3 --intent "horror action demo; max pressure; EN only"
Options:
  -o OUT            output dir (default: out/)
  --skip-validate   do not run tools/saund-validate.py
  --validate PATH   path to validator (default: tools/saund-validate.py)
Exit code: 0 = RELEASED, 1 = BLOCKED or pipeline error.
"""
import argparse, os, subprocess, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode != 0:
        print(f"[SRE] pipeline stopped at: {' '.join(cmd)}")
        sys.exit(r.returncode)
    return r

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--intent", default="")
    ap.add_argument("--title", default="SRE track")
    ap.add_argument("-o", "--out", default="out")
    ap.add_argument("--skip-validate", action="store_true")
    ap.add_argument("--validate", default=os.path.join("tools", "saund-validate.py"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    py = sys.executable

    print("=" * 62)
    print("SAUND REVERSE ENGINE v0.1 — pipeline start")
    print("=" * 62)
    run([py, os.path.join("sre", "analyze.py"), a.audio,
         "-o", os.path.join(a.out, "measured.json")])
    run([py, os.path.join("sre", "map_semantics.py"),
         os.path.join(a.out, "measured.json"),
         "-o", os.path.join(a.out, "semantic.json")])
    run([py, os.path.join("sre", "emit_saund.py"),
         os.path.join(a.out, "semantic.json"),
         "--intent", a.intent, "--title", a.title, "-o", a.out])

    verdict = "RELEASED (validator not run)"
    if not a.skip_validate:
        r = subprocess.run([py, a.validate, os.path.join(a.out, "track.saund")], cwd=ROOT)
        verdict = "RELEASED" if r.returncode == 0 else "BLOCKED"

    m = json.load(open(os.path.join(a.out, "measured.json")))
    s = json.load(open(os.path.join(a.out, "semantic.json")))
    print("\n" + "=" * 62)
    print("SRE SUMMARY")
    print(f"  tempo      : {m['tempo_bpm']} BPM ({m['tempo_conf']})")
    print(f"  beat       : {s['groove']['pattern']} (periodicity {m['beat_periodicity']})")
    print(f"  key        : {s['harmony']['key']} {s['harmony']['mode']}")
    print(f"  arc        : {' '.join(s['arc']['arc'])} [{s['arc']['confidence']}]")
    print(f"  gaps       : {len(m['silence_gaps_s'])} silence candidates")
    print(f"  artifacts  : {a.out}/track.saund, track.supplements.md, intake_preview.txt")
    print(f"  verdict    : {verdict}")
    print("=" * 62)
    print("NEXT: paste track.saund Zone A -> Suno Style, Zone B -> Lyrics.")
    print("      Supplements file goes alongside as SIE input.")
    sys.exit(0 if verdict == "RELEASED" else 1)

if __name__ == "__main__":
    main()
