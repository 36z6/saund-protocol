# SAUND Quickstart (5 minutes)

Goal: idea → Suno-ready Style + Lyrics fields.

## 1. Open an example

Start with any file in `/examples`:
- `transcendental_trance.saund` — euphoric female vocal + supersaw evolution
- `bassline_techno.saund` — bass riff as identity, 128 BPM
- `oriental_funk.saund` — Egyptian Arabic vocal + electro funk
- `horror_action.saund` — no beat, SFX as rhythm, vocal morph

## 2. Copy into Suno

1. Open the example file
2. Copy **Zone A** (from `[GLOBAL]` to `[LEGEND]`) → paste into Suno **"Style of Music"**
3. Copy **Zone B** (section markers `[I]`, `[G]`... + vocal text) → paste into Suno **"Lyrics"**
4. Press **Create**

## 3. Make it yours

Change any of these, leave the rest alone:
- **Tempo / key** → edit the `[GLOBAL]` line
- **Section order** → edit `[ARC: I G S K R P F O]`
- **Vocal text** → edit Zone B lines under each marker
- **Language** → change `EN ONLY` / `Русский` in `[GLOBAL]`

## 4. Validate (optional)

If you have Python:
```bash
python tools/saund-validate.py examples/your_file.saund
```

## 5. Rules of thumb

- Zone A ≤ **800 chars** (Suno ceiling)
- Zone B ≤ **4000 chars** (Suno ceiling)
- **No technical directives** inside Zone B (only `[I]`, `[G]`... markers + vocal text)
- Every letter code you use **must appear** in `[LEGEND]`

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
