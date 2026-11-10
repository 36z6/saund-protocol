#!/usr/bin/env python3
"""SRE test suite: integrity / contract / determinism / version-independence.
Usage: python sre/tests/run_tests.py [--measured PATH]
Exit 0 = all pass. No SAUND core involvement; contract-only coupling."""
import json, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
SRE = os.path.dirname(HERE)
ROOT = os.path.dirname(SRE)
sys.path.insert(0, SRE)
import map_semantics as M2, emit_saund as E3
from contract import C

# Директивы, присутствующие в SAUND v3.3 и v3.4 одновременно (пересечение = ядро)
V33 = {"GLOBAL","ARC","WGT-MAP","DUR-PLAN","SPEAKERS","INST-MAP","GRV-MAP","HRM-MAP",
       "TRN-MAP","SPC-MAP","AUT-MAP","FX-MAP","SC-MAP","MIX-MAP","MAST-MAP","LEGEND",
       "SECTION","BUILD","DROP","ULT","TRANSITION","INSTRUMENTAL"}
V34 = V33 | {"LEAD-MAP","VOC-MAP","FID-MAP","SFX-MAP"}
RES = []
def check(name, cond, detail=""): RES.append((name, bool(cond), detail))

def fixture():
    secs = [{"idx": i, "section_idx": i, "t_start": i*20.0, "t_end": (i+1)*20.0,
             "rms": round(0.10+0.05*(i % 4), 4),
             "low_20_120": 0.35 if i % 3 == 0 else 0.10,
             "mid_120_2k": 0.45 if i % 2 else 0.20,
             "high_2k_8k": 0.20 if i in (3, 6) else 0.05,
             "air_8k_16k": 0.12 if i > 4 else 0.03,
             "transient_density": 1.2} for i in range(8)]
    return {"source": "fixture.wav", "sre_stage": 1, "duration_s": 160.0,
            "tempo_bpm": 128, "tempo_conf": "HIGH", "beat_periodicity": 0.15,
            "beat_conf": "LOW", "key": "F minor", "key_conf": 0.62,
            "sections": secs, "silence_gaps_s": [[60.0, 61.5]]}

def build(measured):
    sem = {"source": measured["source"], "sre_stage": 2,
           "groove": M2.map_beat_to_groove(measured["beat_periodicity"], measured["tempo_bpm"]),
           "timbre_slots": M2.map_spectral_to_timbre(measured["sections"]),
           "percussion": M2.map_transients_to_percussion(measured["sections"]),
           "sfx_candidates": M2.map_silence_to_sfx(measured["silence_gaps_s"]),
           "arc": M2.map_sections_to_arc(measured["sections"], measured["beat_periodicity"]),
           "harmony": M2.map_key_to_harmony(measured["key"], measured["key_conf"]),
           "tempo_bpm": measured["tempo_bpm"], "duration_s": measured["duration_s"],
           "sections": measured["sections"]}
    em = E3.Emitter(sem, "test intent", "fixture")
    return sem, em, em.zone_a_fit(), em.zone_b(), em.supplements(), em.report()

def directives_of(za): return re.findall(r"^\[([A-Z][A-Z0-9-]*)", za, re.M)
def markers_of(zb):    return re.findall(r"^\[([IGSKRPFO])\]", zb, re.M)

def main():
    ap = sys.argv[1:]
    measured = json.load(open(ap[ap.index("--measured")+1])) if "--measured" in ap else fixture()
    sem, em, za, zb, sup, rep = build(measured)
    dirs, marks, arc = directives_of(za), markers_of(zb), sem["arc"]["arc"]

    check("T01 directive subset (contract)",
          set(dirs) <= C["STABLE_DIRECTIVES"],
          str(set(dirs)-C["STABLE_DIRECTIVES"]))
    check("T02 DSE core sections only",
          set(arc) <= set(C["DSE_CORE_SECTIONS"]))
    check("T03 zone B purity",
          all(re.match(r"^\[[IGSKRPFO]\]$", l) or l.strip()==""
              or not l.strip().startswith("[") for l in zb.splitlines()))
    check("T04 ceilings",
          len(za) <= C["CEILINGS"]["STYLE"] and len(zb) <= C["CEILINGS"]["LYRICS"],
          f"{len(za)}/{len(zb)}")
    entries = [l for l in sup.splitlines() if l.startswith("ENTRY")]
    check("T05 entry mandatory fields",
          all(all(f in l for f in ("target=", "values=", "capability=", "source_trace="))
              for l in entries) or not entries)
    check("T06 capability/mode closed sets",
          all(e["capability_level"] in C["CAPABILITIES"] for e in em.applied+em.candidates))
    check("T07 targets registered",
          all(e["target"] in {"TIMBRE LIBRARY","GROOVE LIBRARY","SYMBOL REGISTRY",
                              "FX-MAP","MIX","SPEAKERS"}
              for e in em.applied+em.candidates))
    key_ok = (sem["harmony"]["confidence"] == "LOW") or (measured["key"].split()[0] in za)
    check("T08 integrity: no loss/mutation",
          f'{measured["tempo_bpm"]} BPM' in za and key_ok
          and len(arc) == len(measured["sections"]) and marks == arc
          and int(re.search(r"TOTAL=(\d+):(\d+)", za).group(1))*60
            + int(re.search(r"TOTAL=(\d+):(\d+)", za).group(2)) == round(measured["duration_s"]))
    check("T09 confidence gating",
          all(e["confidence"] != "LOW" for e in em.applied)
          and all(e["confidence"] == "LOW" for e in em.candidates))
    _, _, za2, zb2, sup2, _ = build(measured)
    check("T10 determinism", (za, zb, sup) == (za2, zb2, sup2))
    check("T11 version-independence",
          set(dirs) <= (V33 & V34) and set(dirs) <= C["STABLE_DIRECTIVES"])
    with tempfile.TemporaryDirectory() as td:
        good = os.path.join(td, "g.saund")
        open(good, "w").write(za+"\n\n"+zb+"\n")
        bad  = os.path.join(td, "b.saund")
        open(bad,  "w").write(za+"\n\n"+zb+"\n[FX-MAP: K=SAW:F]\n")
        rg = subprocess.run(
            [sys.executable, os.path.join(ROOT,"tools","saund-validate.py"), good],
            capture_output=True)
        rb = subprocess.run(
            [sys.executable, os.path.join(ROOT,"tools","saund-validate.py"), bad],
            capture_output=True)
        check("T12 validator: clean=RELEASED / impure=BLOCKED",
              rg.returncode == 0 and rb.returncode == 1)

    print("SRE TEST SUITE — contract v%d" % C["CONTRACT_VERSION"])
    print("-"*58)
    fails = 0
    for n, ok, d in RES:
        print(f"  {n:<44} {'PASS' if ok else 'FAIL'} {d if not ok else ''}")
        fails += (not ok)
    print("-"*58)
    print(f"  {len(RES)-fails}/{len(RES)} PASS — "
          + ("no loss, no mutation, version-independent" if not fails else "FIX REQUIRED"))
    sys.exit(0 if not fails else 1)

if __name__ == "__main__":
    main()
