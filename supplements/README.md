# SAUND Supplements — Additional Music Knowledge Libraries

These files are **extra data libraries** for SAUND. They contain music
terminology and reference tables: harmonic progressions, modes and scales,
grooves, sound design, mixing chains, genre formulas, BPM and trend tables.

They are **not code and not part of the core protocol**. They are add-ons:
the main engine (SAUND SUNO COMPILER SKILL v3.4 + SAUND Protocol v0.1)
reads them as reference data when compiling a track. Loading order does not
matter — load them together with the main skill or after it.

## Files

| File | Contains |
|---|---|
| `HARMONY-supplement.md` | Chord progressions (classical, jazz, blues, pop, modal, trance, ambient, dark), modulation techniques, grooves, weight sound design, mixing chains, genre formulas |
| `SCALES-supplement.md` | Modes and scales (diatonic, pentatonic, symmetric, exotic), horror/cinematic modes, 2026 style and BPM trend tables |

## How a SAUND document uses them

Add one line at the top of your `.saund` document:

The compiler then takes chords, modes, tempos and techniques from these
libraries instead of inventing them.

## Adding a new library

1. One knowledge file = one file in this folder.
2. Name it `TYPE-name.md`, where TYPE is one of:
   `HARMONY-`, `SCALES-`, `GROOVE-`, `SOUND_DESIGN-`, `MIX_MASTER-`, `ARRANGEMENT-`.
3. Add one row to the table above.

Supplements are DATA: they can grow without changing the protocol version.
