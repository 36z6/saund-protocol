#!/usr/bin/env python3
"""
SAUND Protocol Validator — MVP v0.1
Validates a SAUND document against core invariants.
Usage: python saund-validate.py track.saund
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Tuple

STYLE_CEILING = 800
LYRICS_CEILING = 4000
MANDATORY = {"[GLOBAL]", "[ARC]", "[LEGEND]"}
CORE_SEC_CODES = {"I", "G", "S", "K", "R", "P", "F", "O"}

@dataclass
class ValidationReport:
    file: str
    passes: List[str] = field(default_factory=list)
    warns: List[str] = field(default_factory=list)
    fails: List[str] = field(default_factory=list)
    
    def ok(self, gate: str, msg: str): self.passes.append(f"{gate} OK: {msg}")
    def warn(self, gate: str, msg: str): self.warns.append(f"{gate} WARN: {msg}")
    def fail(self, gate: str, msg: str): self.fails.append(f"{gate} FAIL: {msg}")
    
    @property
    def released(self) -> bool: return len(self.fails) == 0
    
    def render(self) -> str:
        lines = [f"SAUND VALIDATION REPORT — {self.file}", "=" * 60]
        for p in self.passes: lines.append(f"  ✓ {p}")
        for w in self.warns: lines.append(f"  ⚠ {w}")
        for f in self.fails: lines.append(f"  ✗ {f}")
        lines.append("=" * 60)
        lines.append(f"→ {'RELEASED' if self.released else 'BLOCKED'}")
        lines.append(f"  passes={len(self.passes)} warns={len(self.warns)} fails={len(self.fails)}")
        return "\n".join(lines)

def split_zones(text: str) -> Tuple[str, str]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\s*\[([IGSKRPFO])(?:#\d+)?\s*(?:[—\-|\]]|$)", line):
            return "\n".join(lines[:i]), "\n".join(lines[i:])
    return text, ""

def extract_arc(zone_a: str) -> List[str]:
    m = re.search(r"\[ARC\s*:\s*([^\]]+)\]", zone_a)
    if not m: return []
    tokens = re.split(r"[→\s,;]+", m.group(1))
    return [t.strip().split("#")[0] for t in tokens if t.strip() in CORE_SEC_CODES]

def extract_zone_b_sections(zone_b: str) -> List[str]:
    return [m.group(1) for line in zone_b.splitlines()
            if (m := re.match(r"^\s*\[([IGSKRPFO])(?:#\d+)?\s*(?:[—\-|\]]|$)", line))]

def extract_legend_codes(zone_a: str) -> set:
    m = re.search(r"\[LEGEND\s*:\s*([^\]]+)\]", zone_a, re.DOTALL)
    if not m: return set()
    return set(re.findall(r"([A-ZΨΤΩ][A-Z0-9_\-]*)=", m.group(1)))

def extract_map_codes(zone_a: str) -> set:
    return {f"{slot}@{sec}" for slot, sec in re.findall(r"\b([A-Z]{2,4})@([IGSKRPFO])\b", zone_a)}

def validate(path: Path) -> ValidationReport:
    text = path.read_text(encoding="utf-8")
    rep = ValidationReport(file=path.name)
    zone_a, zone_b = split_zones(text)
    
    style_len, lyrics_len = len(zone_a), len(zone_b)
    if style_len <= STYLE_CEILING:
        rep.ok("BUD-001", f"STYLE {style_len}/{STYLE_CEILING} chars")
    else:
        rep.fail("BUD-001", f"STYLE {style_len}/{STYLE_CEILING} chars (overflow {style_len - STYLE_CEILING})")
    
    if lyrics_len <= LYRICS_CEILING:
        rep.ok("BUD-002", f"LYRICS {lyrics_len}/{LYRICS_CEILING} chars")
    else:
        rep.fail("BUD-002", f"LYRICS {lyrics_len}/{LYRICS_CEILING} chars (overflow {lyrics_len - LYRICS_CEILING})")
    
    present = {d for d in MANDATORY if d in zone_a}
    missing = MANDATORY - present
    if not missing:
        rep.ok("SYN-001", f"mandatory directives present: {sorted(present)}")
    else:
        rep.fail("SYN-001", f"missing mandatory directives: {sorted(missing)}")
    
    arc = extract_arc(zone_a)
    zb = extract_zone_b_sections(zone_b)
    if not arc:
        rep.warn("SYN-002", "could not parse [ARC]")
    elif arc == zb:
        rep.ok("SYN-002", f"ARC parity: {arc}")
    else:
        rep.fail("SYN-002", f"ARC mismatch: ARC={arc} ZoneB={zb}")
    
    stray = [line.strip() for line in zone_b.splitlines()
             if re.match(r"^\s*\[[A-Z][A-Z0-9_\-]*(?:\s*:[^\]]*)?\]", line) 
             and not re.match(r"^\s*\[([IGSKRPFO])(?:#\d+)?\s*(?:[—\-|\]]|$)", line)]
    if not stray:
        rep.ok("INV-047", "zone purity: no stray directives in Zone B")
    else:
        rep.fail("INV-047", f"directives leaked into Zone B: {stray[:3]}")
    
    legend_codes = extract_legend_codes(zone_a)
    map_codes = extract_map_codes(zone_a)
    if map_codes and not legend_codes:
        rep.fail("INV-033", "maps use SLOT@SEC but [LEGEND] is empty")
    elif legend_codes:
        rep.ok("INV-033", f"LEGEND covers {len(legend_codes)} codes")
    else:
        rep.ok("INV-033", "no @-syntax used, LEGEND optional")
    
    return rep

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python saund-validate.py <file.saund>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)
    
    report = validate(path)
    print(report.render())
    sys.exit(0 if report.released else 1)
