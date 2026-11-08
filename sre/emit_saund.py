#!/usr/bin/env python3
"""
SRE stage 3 — EMIT (semantic.json -> track.saund + supplements + intake preview).
Part of SAUND REVERSE ENGINE v0.1. Does NOT touch SAUND core.
Emits only USER SOURCE artifacts; SAUND ingests them via SIE unchanged.
Usage: python sre/emit_saund.py semantic.json --intent "horror action demo" -o out/
"""
import argparse, json, os

SEC_MEANING = {"I":"Intro","G":"Grid Attack","S":"Sweeper Burst","K":"Kinetic Drop",
               "R":"Rhythm Fracture","P":"Pressure Lock","F":"Final Overdrive","O":"Outro"}

def mode_of(conf):  return "STRICT" if conf in ("HIGH","MEDIUM") else "CANDIDATE"
def cap_of(kind):   return "NATIVE" if kind in ("tempo","key","structure") else "SEMANTIC_ONLY"

class Emitter:
    def __init__(self, sem, intent, title):
        self.sem, self.intent, self.title = sem, intent, title
        self.applied, self.candidates, self.compact_log = [], [], []
        self.eid = 0
        self.src = os.path.basename(sem.get("source","track.mp3"))

    def entry(self, stype, action, target, name, meaning, values, kind, conf, trace):
        self.eid += 1
        e = dict(entry_id=f"E{self.eid:03d}", supplement_id=f"SRE-{stype}",
                 entry_type=stype, domain=target, name=name, meaning=meaning,
                 target=target, values=values, effects=[], constraints=[],
                 capability_level=cap_of(kind), priority=3,
                 source_trace=f"SRE:{self.src}:{trace}",
                 confidence=conf, mode=mode_of(conf), action=action)
        (self.applied if e["mode"]=="STRICT" else self.candidates).append(e)
        return e

    # ── Zone A with compact levels (FIX-4) ─────────────────────────────
    def zone_a(self, level=0):
        s, arc = self.sem, self.sem["arc"]["arc"]
        secs = self._sections_by_arc(arc)
        lines = []
        g = [self.intent or "reverse-engineered track", f'{s["tempo_bpm"]} BPM']
        if s["harmony"]["confidence"] != "LOW":
            g.append(f'key {s["harmony"]["key"]} {s["harmony"]["mode"]}')
        if s["groove"]["pattern"] == "NO_BEAT":
            g += ["NO BEAT", "BROKEN GRID", "FX EVENTS ONLY UNDER SUDDEN HITS"]
        g.append("CONFIDENCE: arc=LOW (verify manually); timbre=SEMANTIC_ONLY")
        lines.append("[GLOBAL: " + "; ".join(g) + ".]")
        lines.append("[ARC: " + " ".join(arc) + "]")

        # DUR-PLAN
        tot = int(round(s["duration_s"]))
        ds = [max(1, int(round(t["t_end"] - t["t_start"]))) for t in secs]
        ds[-1] += tot - sum(ds)
        lines.append("[DUR-PLAN: TOTAL=%d:%02d; %s]" % (
            tot//60, tot%60, ",".join(f"{c}={v}" for c, v in zip(arc, ds))))

        # WGT-MAP from normalized rms (level>=2: only peak sections + I,O)
        rms = [t["rms"] for t in secs]
        mx = max(rms) or 1.0
        wgt = []
        for i, (c, t) in enumerate(zip(arc, secs)):
            if level >= 2 and not (rms[i] >= 0.6*mx or c in ("I","O")):
                continue
            slots = [x["slot"] for x in t["timbre"]
                     if x["confidence"] in ("HIGH","MEDIUM") and x["slot"] != "VOCAL"]
            w = round(max(0.1, t["rms"]/mx), 1)
            wgt.append(f'{c}=' + ",".join(f'{sl}:{w}' for sl in sorted(set(slots)) or ["PAD"]))
        if wgt: lines.append("[WGT-MAP: " + "; ".join(wgt) + "]")

        # INST-MAP (HIGH/MEDIUM only; VOCAL excluded — FIX-2)
        inst = {}
        for t in secs:
            for x in t["timbre"]:
                if x["confidence"] in ("HIGH","MEDIUM") and x["slot"] != "VOCAL" \
                        and x["slot"] not in inst:
                    prof = x["profile"].split("/")[0] if level >= 2 else x["profile"]
                    inst[x["slot"]] = prof
                    if x["confidence"] == "MEDIUM":
                        self.entry("SOUND_DESIGN","EXTEND_ENTRY","TIMBRE LIBRARY",
                                   f'{x["slot"]}-{x["profile"]}', x.get("note", x["profile"]),
                                   f'slot={x["slot"]},profile={x["profile"]}',
                                   "timbre", "MEDIUM", f'timbre@sec{t["section_idx"]}')
        if inst: lines.append("[INST-MAP: " + "; ".join(f'{k}={v}' for k, v in inst.items()) + "]")

        # GRV-MAP
        if s["groove"]["pattern"] == "NO_BEAT":
            lines.append("[GRV-MAP: KCK=NONE; BROKEN_GRID; FX_EVENTS_ONLY_UNDER_SUDDEN_HITS]")
        else:
            lines.append(f'[GRV-MAP: KCK={s["groove"]["pattern"]}]')

        # HRM-MAP (level>=1: single representative entry)
        h = s["harmony"]
        if h["confidence"] != "LOW":
            if level >= 1:
                lines.append(f'[HRM-MAP: {arc[0]}={h["key"]} / {h["mode"]} / i / open / 0.5]')
            else:
                lines.append("[HRM-MAP: " + "; ".join(
                    f'{c}={h["key"]} / {h["mode"]} / i / open / {round(max(0.1, r/mx),1)}'
                    for c, r in zip(arc, rms)) + "]")

        # FX-MAP: gated silence -> core code G on ATM (level<3)
        if level < 3:
            fx = []
            for gap in s["sfx_candidates"]:
                code = self._sec_at(gap["t_start"], arc, secs)
                if code: fx.append(f'{code}=ATM:G')
            if fx: lines.append("[FX-MAP: " + "; ".join(sorted(set(fx))) + "]")

        lines.append("[MIX-MAP: MONO SUB<120; WIDE UPPER; VOCAL CLARITY PROTECTED]")
        lines.append("[MAST-MAP: LUFS=-9; TP=-1.0; FADE=none]")
        used = sorted(set(arc))
        lines.append("[LEGEND: SEC: " + "; ".join(f'{c}={SEC_MEANING[c]}' for c in used) + "]")
        return "\n".join(lines)

    def zone_a_fit(self):
        for lv in (0, 1, 2, 3):
            za = self.zone_a(lv)
            if len(za) <= 800:
                if lv: self.compact_log.append(f"WARN-COMPACT level={lv} (Zone A fit 800)")
                return za
        raise SystemExit("[SRE] Zone A >800 even at level 3 — split intent")

    # ── Zone B: markers only; vocals UNRESOLVED from audio ─────────────
    def zone_b(self):
        return "\n".join(f'[{c}]' for c in self.sem["arc"]["arc"])

    # ── Supplements ─────────────────────────────────────────────────────
    def supplements(self):
        out = []
        for mode, pool in (("STRICT", self.applied), ("CANDIDATE", self.candidates)):
            by = {}
            for e in pool: by.setdefault(e["entry_type"], []).append(e)
            for stype, es in by.items():
                out.append(f'[SUPPLEMENT: {stype}; MODE={mode}]')
                for e in es:
                    out.append(f'ENTRY {e["entry_id"]}: action={e["action"]}; '
                               f'target={e["target"]}; name={e["name"]}; '
                               f'meaning={e["meaning"]}; values={e["values"]}; '
                               f'capability={e["capability_level"]}; '
                               f'source_trace={e["source_trace"]}')
                out.append("")
        return "\n".join(out) or "[INTAKE] NULL\n"

    # ── Intake preview ──────────────────────────────────────────────────
    def report(self):
        nat = sum(1 for e in self.applied if e["capability_level"]=="NATIVE")
        sem = sum(1 for e in self.applied if e["capability_level"]=="SEMANTIC_ONLY")
        L = [f'[INTAKE] SUPPLEMENTS={len(set(e["supplement_id"] for e in self.applied+self.candidates))} '
             f'ENTRIES={len(self.applied)+len(self.candidates)} APPLIED={len(self.applied)} '
             f'BLOCKED=0 UNRESOLVED={len(self.candidates)}']
        for i, e in enumerate(self.applied, 1):
            L.append(f'[INTAKE] INJ-{i:03d}: {e["target"]} <- {e["supplement_id"]}/{e["entry_id"]} '
                     f'[{"NAT" if e["capability_level"]=="NATIVE" else "SEM"}]')
        for e in self.candidates:
            L.append(f'[INTAKE] WARN: {e["name"]} (LOW confidence -> CANDIDATE, not applied)')
        for w in self.compact_log:
            L.append(f'[INTAKE] {w}')
        L.append(f'[INTAKE] CAP: NATIVE={nat} SEMANTIC={sem} BACKEND=0 SPEC-BLOCKED=0')
        L.append('TODO: Zone B vocal text unknown from audio -> fill manually or declare [INSTRUMENTAL]')
        L.append('TODO: verify ARC (confidence LOW) against listening')
        return "\n".join(L)

    # ── helpers ─────────────────────────────────────────────────────────
    def _sections_by_arc(self, arc):
        n = len(self.sem["sections"])
        sec = {t.get("section_idx", i): t for i, t in enumerate(self.sem["sections"])}
        return [sec.get(i, {"section_idx":i,"rms":0.0,"timbre":[],
                            "t_start":0,"t_end":0}) for i in range(n)]
    def _sec_at(self, t, arc, secs):
        for i, s in enumerate(secs):
            if s["t_start"] <= t < s["t_end"]: return arc[i]
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("semantic"); ap.add_argument("--intent", default="")
    ap.add_argument("--title", default="SRE track"); ap.add_argument("-o", "--out", default="out")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sem = json.load(open(a.semantic))
    em = Emitter(sem, a.intent, a.title)
    za, zb = em.zone_a_fit(), em.zone_b()
    doc = f'# {a.title} — SRE-generated USER SOURCE (fresh-build mandatory, INV-019)\n\n{za}\n\n{zb}\n'
    open(f'{a.out}/track.saund','w').write(doc)
    open(f'{a.out}/track.supplements.md','w').write(em.supplements() + "\n")
    open(f'{a.out}/intake_preview.txt','w').write(em.report() + "\n")
    print(f'[SRE stage3] wrote {a.out}/track.saund, track.supplements.md, intake_preview.txt')

if __name__ == "__main__":
    main()
