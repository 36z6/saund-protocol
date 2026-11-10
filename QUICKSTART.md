# SAUND Quickstart (5 minutes)

Goal: idea → Suno-ready Style + Lyrics fields.

## 1. Open an example

Start with any file in `/examples`:
- `transcendental_trance.saund` — euphoric female vocal + supersaw evolution
- `bassline_techno.saund` — bass riff as identity, 128 BPM
- `oriental_funk.saund` — Egyptian Arabic vocal + electro funk
- `horror_action.saund` — no beat, SFX as rhythm, vocal morph

## 2. Find the compiled Suno fields

Scroll to the **bottom** of the example file. You will find this block:

```
### COMPILED PROJECTION (Suno fields) ###

STYLE (780/800):
...one optimized line...

LYRICS:
Zone B as above...
```

This is the output ready to paste into Suno.

## 3. Copy into Suno

1. Copy the single line under **STYLE (XXX/800):** → paste into Suno **"Style of Music"**
2. Copy the **Zone B** block (from the first section marker `[I]` to the last line of vocal text) → paste into Suno **"Lyrics"**
3. Press **Create**

> **Why not paste the whole Zone A?** Zone A is the *protocol source* (directives, maps, legend) — it is longer than Suno's 800-char field and is meant for the SAUND compiler to read, not for Suno directly. The `STYLE (XXX/800)` line is the *compiled*, ceiling-safe version of Zone A. Always use it.

## 4. Make it yours

Change any of these, leave the rest alone:
- **Tempo / key** → edit the `[GLOBAL]` line in Zone A, then rebuild the STYLE line
- **Section order** → edit `[ARC: I G S K R P F O]`
- **Vocal text** → edit Zone B lines under each marker (this does not require rebuilding STYLE)
- **Language** → change `EN ONLY` / `Русский` in `[GLOBAL]`

If you only change vocal text in Zone B, you do not need to touch STYLE at all.

## 5. Validate (optional)

If you have Python:
```bash
python tools/saund-validate.py examples/your_file.saund
```

Expected: `RELEASED` with all gates green. If you see `BLOCKED`, the file is broken somewhere — fix and re-run.

## 6. Rules of thumb

- `STYLE (XXX/800)` must be ≤ **800 chars** (Suno ceiling)
- Zone B must be ≤ **4000 chars** (Suno ceiling)
- **No technical directives** inside Zone B (only `[I]`, `[G]`... markers + vocal text)
- Every letter code you use in Zone A **must appear** in `[LEGEND]`

## Want the reverse path?

Upload an existing track → get a draft SAUND spec:
```bash
python sre/run.py your_track.mp3 --intent "your intent" -o out
```

See `SAUND_PROTOCOL_SPEC_v0.1.md` §11 and the `/sre` folder.

## Need help?

- Protocol: `SAUND_PROTOCOL_SPEC_v0.1.md`
- Full compiler spec: `SAUND_COMPILER_SPEC_v3.4.md`
- Manifesto (why this exists): `MANIFESTO.md`
