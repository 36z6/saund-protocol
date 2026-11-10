#!/usr/bin/env python3
"""
SRE batch variations — N mutant docs, same timbre DNA.
Axes: transpose / tempo / arc-swap / density / sfx-gaps.
Contract-only output; every variant auto-validated.
Usage: python sre/variants.py out/semantic.json -n 6 -o out/variants
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import emit_saund as E3
KEYS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def mutate(sem, i):
    s = json.loads(json.dumps(sem))
    plan = {}
    r = i % 5
    if r == 1 and s["harmony"]["key"] in KEYS:
        s["harmony"]["key"] = KEYS[(KEYS.index(s["harmony"]["key"]) + 2) % 12]
        plan["transpose"] = "+2 st"
    elif r == 2:
        s["tempo_bpm"] += 6
        plan["tempo"] = "+6 BPM"
    elif r == 3 and len(s["arc"]["arc"]) > 5:
        a = s["arc"]["arc"]
        a[4], a[5] = a[5], a[4]
        plan["arc"] = "swap@4,5"
    elif r == 4:
        for t in s["sections"]: t["rms"] = round(t["rms"] * 0.8, 4)
        plan["density"] = "x0.8"
    elif r == 0 and i:
        s["sfx_candidates"] = []
        plan["sfx"] = "gaps off"
    return s, plan

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("semantic")
    ap.add_argument("-n", type=int, default=6)
    ap.add_argument("--intent", default="")
    ap.add_argument("-o", "--out", default="out/variants")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    base = json.load(open(a.semantic))
    manifest = []
    
    for i in range(1, a.n + 1):
        s, plan = mutate(base, i)
        em = E3.Emitter(s, a.intent + f"; variant {i:02d}", f"variant {i:02d}")
        za, zb = em.zone_a_fit(), em.zone_b()
        p = os.path.join(a.out, f"v{i:02d}.saund")
        open(p, "w").write(f"# SRE variant {i:02d} — axes: {plan or 'baseline'}\n\n{za}\n\n{zb}\n")
        
        r = subprocess.run(
            [sys.executable, os.path.join(ROOT, "tools", "saund-validate.py"), p],
            capture_output=True
        )
        manifest.append({
            "variant": f"v{i:02d}", 
            "axes": plan or "baseline",
            "zone_a_len": len(za), 
            "verdict": "RELEASED" if r.returncode == 0 else "BLOCKED"
        })
        
    json.dump(manifest, open(os.path.join(a.out, "manifest.json"), "w"), indent=2)
    
    print("SRE VARIANTS — contract v1")
    print("-" * 58)
    for m in manifest:
        print(f'  {m["variant"]}  {str(m["axes"]):<18} ZA={m["zone_a_len"]:>3}  {m["verdict"]}')
    print("-" * 58)
    bad = [m["variant"] for m in manifest if m["verdict"] != "RELEASED"]
    print(f"  {len(manifest)-len(bad)}/{len(manifest)} RELEASED" + (f"  BLOCKED: {bad}" if bad else ""))
    sys.exit(0 if not bad else 1)

if __name__ == "__main__":
    main()
