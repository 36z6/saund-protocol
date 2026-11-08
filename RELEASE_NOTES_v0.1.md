# SAUND v0.1 — release notes

## What is inside

- **SAUND_PROTOCOL_SPEC_v0.1.md** — the normative standard
- **SAUND_COMPILER_SPEC_v3.4.md** — reference compiler spec (Suno backend)
- **tools/** — MVP validator + reverse-compiler skeleton
- **sre/** — Reverse Engine pipeline (measure → map → emit) + tests
- **examples/** — 4 real production artifacts with compiled Suno fields

## What works today

- Deterministic Zone A / Zone B authoring with budgets and parity
- MVP validation (6 gates, RELEASED/BLOCKED report)
- Lossy audio → spec reverse path with honest confidence tags
- 4 genre examples: trance, bassline techno, oriental funk, horror action

## What is honestly NOT working yet

- The full compiler is a **SPEC**, not code (validator is MVP-only)
- SRE arc detection is heuristic (confidence LOW, flagged)
- No video adapters, no vocal-text extraction from audio
- No live runtime (reserved for v2.0)

## Examples you can try right now

1. **Transcendental Trance** (140 BPM, RU female vocal) — evolving supersaw leads, emotional arcs
2. **Bassline Techno** (128 BPM, EN male vocal) — bass riff as identity, formant sweeps
3. **Oriental Funk** (102 BPM, Arabic vocal) — electro-funk with Egyptian dialect
4. **Horror Action** (128 BPM, EN) — no beat, SFX as rhythm, mosquito lead

Copy Zone A from any example into Suno "Style" field, Zone B into "Lyrics". Generate.

## Quick validation

If you have Python installed:

```bash
python tools/saund-validate.py examples/transcendental_trance.saund
```

Expected output: 6 gates PASS → `RELEASED`.

## How to contribute

- **DATA** (timbre families, groove patterns, vocal archetypes): submit via INTAKE directives in your SAUND documents. No version bump needed.
- **CODE** (adapters, validation tools, docs): open a PR.
- **Issues**: describe the SAUND document that failed, expected vs actual behavior, and backend version.

## License

MIT. This is a gift, not a product.

## Attribution

SAUND Protocol and SAUND SUNO COMPILER SKILL designed by **36z6** (2025-2026).

Delta-Shape Encoding (DSE) notation developed iteratively through real production use across industrial, oriental funk, trance, bassline techno, phonk, and commercial genres.

## What's next

- v0.2: JSON schema + `saund-suno` adapter
- v0.9: video directives (CHAR-LOCK, CHOREO-MAP, CAM-MAP)
- v1.0: first stable release, multiple adapters
- v1.1: reverse compiler MVP (audio → SAUND)
- v2.0: live runtime, brand layer

---

**Built with SAUND v3.4** · Protocol v0.1 · Release v0.1
