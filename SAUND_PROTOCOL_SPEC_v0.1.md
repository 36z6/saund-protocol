# SAUND Protocol Specification v0.1

**A declarative standard for deterministic cross-modal AI media generation**

Author: 36z6 · Version: 0.1 (draft) · Date: 2026-10-28
Status: **Proposal · Pre-release draft**
License: MIT (final license TBD)

---

## 0. Abstract

SAUND Protocol is a declarative, versioned, backend-agnostic specification for describing multimodal media artifacts (audio, video, voice, brand identity) in a single source document. It enables one authorial intent to be projected deterministically into multiple AI generation backends (Suno, Udio, Runway, Kling, Seedance, ElevenLabs, Midjourney) with synchronized timing, shared identity, and verifiable output.

SAUND is not a prompt. It is a **protocol**: a typed schema, a resolution engine, and a validation gate that sits between human intent and model-specific input fields. The reference implementation is **SAUND SUNO COMPILER SKILL v3.4**, which targets the Suno audio backend. The protocol itself is backend-neutral.

---

## 1. Motivation

Today's AI media tools are **silos**:

- Each model speaks its own prompt dialect.
- Cross-modal sync (audio ↔ video ↔ voice) is done manually in a DAW/NLE.
- Authorial intent is lost in translation, re-translation, and post-editing.
- There is no way to version, diff, or fork a media project the way code is versioned.

SAUND Protocol fixes this by introducing a **canonical intermediate representation** — the same role MIDI played for hardware synths, Markdown plays for documents, and YAML plays for configuration.

**Core claims:**

1. One SAUND document should describe a complete media artifact (audio + video + voice + brand).
2. Multiple backends should consume the same document and produce synchronized output.
3. The document should be human-readable, diff-friendly, and version-controlled.
4. The protocol should never invent capabilities a backend does not have.

---

## 2. Design Principles

| Principle | Meaning |
|---|---|
| **Declarative, not procedural** | Documents describe *what*, not *how*. Resolution order is fixed by the spec. |
| **Typed, not freeform** | Every field has a closed registry. Unknown values are validation errors, not warnings. |
| **Traceable** | Every projected token carries a `source_trace` back to the originating node. |
| **Monotone capability** | Supplements and extensions may only *downgrade* capability levels, never upgrade. |
| **Backend-neutral core, backend-specific projections** | The protocol describes intent; adapters translate to model dialects. |
| **Immutable core, extensible data** | Directives, node types, invariants change only via version bump. Timbre, groove, SFX vocabularies extend at runtime via validated INTAKE. |

---

## 3. Scope

### 3.1 In scope

- **Audio**: music, sound design, voice, foley, mastering intent.
- **Video**: character identity, choreography, camera, physics, environment.
- **Brand**: sonic logo, color palette, typographic intent, motion identity.
- **Timing**: synchronized to a shared BPM/bar grid.
- **Constraints**: hard negatives, budget ceilings, fidelity class, density controls.

### 3.2 Out of scope

- Exact DSP parameters, plugin chains, stem export.
- Real-time performance (reserved for v2 Live Runtime extension).
- Visual artwork (reserved for v2 Brand extension).
- Model weights, training, fine-tuning.

---

## 4. Document Model

A SAUND document is a single UTF-8 text file composed of two zones:

```
Zone A — Directive Block       (typed control maps)
Zone B — Content Block         (lyrics, scene text, dialogue)
```

### 4.1 Directive layer

Square brackets `[ ]` are reserved. Core directives:

```
[GLOBAL]    [ARC]       [DUR-PLAN]   [WGT-MAP]   [SPEAKERS]
[VOC-MAP]   [INST-MAP]  [GRV-MAP]    [HRM-MAP]   [LEAD-MAP]
[FX-MAP]    [SPC-MAP]   [SFX-MAP]    [AUT-MAP]   [FID-MAP]
[TRN-MAP]   [SC-MAP]    [MIX-MAP]    [MAST-MAP]  [LEGEND]
```

### 4.2 Section code alphabet (DSE v2.6 CORE)

```
I=Intro  G=Grid Attack  S=Sweeper Burst  K=Kinetic Drop
R=Rhythm Fracture  P=Pressure Lock  F=Final Overdrive  O=Outro
```

These codes are **immutable**. They appear in `[ARC]` and as keys in every SEC-keyed directive.

### 4.3 Effect code alphabet (DSE v2.6 CORE)

```
R=Reverb  D=Delay  F=Filter  S=Saturation  W=Widen  P=Pump
B=Sub  L=Laser  G=Gate  C=Comp  Y=Fly-by
```

### 4.4 Behavior markers

```
→ flow    › seamless flow    ↺ recall    ↑ build    ↓ drop
† ult     ~ mutate           = inherit   + strengthen  − weaken
‹ close / decay / fade
```

### 4.5 Zone B purity

Zone B contains **only** section markers and content text. Technical directives are forbidden in Zone B (section markers exempted).

---

## 5. Registries (DATA, not code)

The protocol defines a closed set of registries that may be extended at runtime via validated INTAKE but never at the protocol-core level.

| Registry | Contents |
|---|---|
| TIMBRE LIBRARY | Family → slot profiles (F-HARSH, F-TECH, F-POP, F-AMB, F-BRK, F-TRN, F-BASS, F-LOFI, ...) |
| GROOVE LIBRARY | Pattern classes per slot |
| VOCAL ARCHETYPE LIBRARY | Typed archetype objects |
| LEAD LIBRARY | Role → source + evolution defaults per family |
| FIDELITY LIBRARY | Family → medium class defaults |
| SFX VOCABULARY | Transition / atmosphere / sting symbols |
| SYMBOL REGISTRY | Typed symbol objects (code, domain, capability, source_trace) |

**Rule:** supplements may ADD_ENTRY / EXTEND_ENTRY to registries. They may not add directives, node types, or invariants.

---

## 6. Resolution Engine

Every SAUND document is compiled through a fixed pipeline:

```
USER IDEA + SUPPLEMENTS
↓ INPUT NORMALIZER
↓ SAUND INTAKE (SIE)
↓ PARSER
↓ SEMANTIC EXTRACTOR
↓ CANONICAL IR
↓ CONTROL GRAPH
↓ CONFLICT RESOLUTION
↓ EFFECTIVE STATE
↓ (per-domain DESIGN engines: INSTRUMENT, GROOVE, HARMONY,
   VOCAL, LEAD, PRESENCE, EFFECT, SPECTRAL, SFX, SPATIAL,
   AUTOMATION, FIDELITY, ARRANGEMENT, DURATION, TRANSITION)
↓ AUTO-INJECT SC / MIX / MASTER
↓ TRANSLATION ENGINE
↓ STYLE / LYRICS / SCENE compilers (with hard ceilings)
↓ SYNC VALIDATOR
↓ BUDGET ENFORCEMENT (PASS 1 + PASS 2)
↓ LEGEND COMPILER
↓ FINAL OUTPUT VALIDATION
↓ RELEASE
```

Failure at any gate transitions the state machine to **BLOCKED** with an itemized report. Silent fallback is impossible by construction.

---

## 7. Cross-Modal Extension (v0.1 → v1.0 path)

v0.1 of the reference implementation targets Suno audio. The protocol is designed to extend to:

### 7.1 Video layer

New directives (reserved names, implementation in v1.0):

```
[CHAR-LOCK]    character identity sheet (proportions, colors, appendage count)
[CHOREO-MAP]   SEC=motion vocabulary + timing (locked to ARC bars)
[CAM-MAP]      SEC=shot type + motion + shake profile
[PHYS-MAP]     secondary motion, follow-through, weight, grounding
[ENV-LOCK]     environment identity (fixed across all shots)
[VID-NEG]      hard negatives (no morph, no drift, no cut)
```

### 7.2 Voice layer

```
[VOICE-LOCK]   speaker identity + timbre class
[DIAL-MAP]     SEC=dialogue + ducking profile
```

### 7.3 Brand layer

```
[BRAND-MAP]    sonic logo, color palette, typographic intent
```

### 7.4 Sync contract

All modal layers share the same `[ARC]` and `[DUR-PLAN]`. Cross-modal sync is automatic: the video `CHOREO-MAP` for section `K` is bound to the audio `INST-MAP` for section `K` at the same bar grid.

---

## 8. JSON Schema (excerpt)

A SAUND document has a canonical JSON projection for machine consumption:

```json
{
  "$schema": "saund-protocol/v0.1",
  "meta": {
    "title": "Transcendental Trance Anthem",
    "language": "ru",
    "tempo_bpm": 140,
    "meter": "4/4",
    "duration_total": "3:26"
  },
  "global": {
    "genre": ["TRANSCENDENTAL UPLIFTING TRANCE", "FUTURE RAVE"],
    "hard_constraints": [
      "CONTINUOUS_ENERGY",
      "NO_OVERDEVELOPMENT",
      "NO_BREAKDOWNS"
    ]
  },
  "arc": ["I","G","S","K","R","P","F","O"],
  "duration_plan": {
    "I":7,"G":14,"S":14,"K":24,"R":16,"P":16,"F":24,"O":8
  },
  "speakers": {
    "G": {"class":"FEMALE","archetype":"POP_LEAD"},
    "K": {"class":"FEMALE","archetype":"POP_LEAD"},
    "F": {"class":"FEMALE","archetype":"POP_LEAD"}
  },
  "vocal_map": {
    "G": {"register":"chest","delivery":"intimate"},
    "K": {"register":"chest","delivery":"soaring-melisma"},
    "F": {"register":"head","delivery":"radiant-belt"}
  },
  "lead_map": {
    "S": {"role":"HOOK","source":"SAW","motion":"~→=→↑","register":"mid-high"},
    "K": {"role":"HOOK","source":"SAW","motion":"HARMONIZE","register":"mid-high"},
    "F": {"role":"HOOK","source":"SAW","motion":"FINAL_FUSION","register":"high"}
  },
  "fidelity": {
    "medium_class": "digital-pristine",
    "noise_floor": "silent",
    "bandwidth": "full-20k",
    "dynamic_range": "dynamic"
  },
  "zone_b": [
    {"section":"G", "text":"Я закрывала глаза..."},
    {"section":"K", "text":"Я поднимаюсь выше..."},
    {"section":"F", "text":"Я выбираю свет — и открываю мир!"}
  ]
}
```

The JSON schema is the **machine source of truth**. The text format in §4 is its human projection. Both are derivations of the same IR.

---

## 9. Capability Matrix

Every declared capability has one of five levels:

| Level | Meaning |
|---|---|
| NATIVE | Backend natively supports this. |
| SEMANTIC_ONLY | Protocol can describe intent; backend execution is best-effort. |
| BACKEND_DEPENDENT | Requires explicit backend confirmation. |
| SPECULATIVE | Not realized by any known backend; blocked by default. |
| UNSUPPORTED | Outside protocol scope (e.g. visual avatar rendering). |

**Monotonicity rule:** supplements and adapters may only *downgrade* a level (e.g. NATIVE → SEMANTIC_ONLY), never upgrade. This is the protocol's primary safety invariant.

---

## 10. Adapters

An **adapter** translates a validated SAUND document into a specific backend's input format. Reference adapters planned:

| Adapter | Target |
|---|---|
| `saund-suno` | Suno v3.5 / v4 (STYLE + LYRICS fields) |
| `saund-udio` | Udio (prompt + tags) |
| `saund-runway` | Runway Gen-3/4 (scene prompts) |
| `saund-kling` | Kling 2.0 (motion + character) |
| `saund-seedance` | Seedance (continuous-shot choreography) |
| `saund-elevenlabs` | ElevenLabs (voice + dialogue) |
| `saund-midjourney` | Midjourney v6+ (character lock sheet) |

An adapter is a **pure function**: `(SAUND document, backend profile) → backend input`. Adapters must not introduce semantics absent from the source document.

---

## 11. Reverse Compiler (vision, v1.1)

A reverse compiler takes an existing media artifact (audio file, video clip, voice recording) and produces a **best-effort SAUND document** that would, when compiled forward, approximate the input.

```
audio.mp3 → [analyzer] → SAUND document (.saund)
video.mp4 → [analyzer] → SAUND document (.saund)
```

This enables:
- **Mutate existing works**: load a reference track, change one parameter, re-compile.
- **Style transfer via protocol**: decompose two works into SAUND, swap components, re-compile.
- **Education**: see the "source code" of any produced track.

The reverse compiler is inherently lossy; its output carries a `confidence` field per node.

---

## 12. Live Runtime (vision, v2.0)

A live runtime executes a SAUND document **incrementally** in response to performer input:

```
performer state changes → IR patch → live re-projection → backend streaming
```

This enables a new performance form: **AI live coding**, where the performer edits the IR in real time and the backend streams the evolving output. Reserved for v2.0.

---

## 13. Conformance

A tool conforms to SAUND Protocol v0.1 if it:

1. Parses documents according to §4–§6.
2. Rejects unknown directives and unregistered symbols with explicit errors (never silently).
3. Emits `[LEGEND]` parity-checked against used codes.
4. Respects hard ceilings (STYLE ≤ 800, LYRICS ≤ 4000 for audio targets).
5. Never invents capabilities; respects the monotonicity rule (§9).
6. Produces an INTAKE REPORT and VALIDATION REPORT for every compilation.

---

## 14. Governance and Versioning

- **Core changes** (directives, invariants, DSE codes) require a **major or minor version bump** and public CHANGELOG.
- **Data changes** (library entries, vocabulary extensions) happen at runtime via INTAKE and do not bump the protocol version.
- The reference implementation is the **canonical interpreter**; in case of ambiguity, the spec text wins over the reference implementation.

---

## 15. Roadmap

| Version | Scope |
|---|---|
| v0.1 | This document. Audio-only reference impl (SAUND v3.4). |
| v0.2 | JSON schema formalized. `saund-suno` adapter published. |
| v0.9 | Video directives (`CHAR-LOCK`, `CHOREO-MAP`, `CAM-MAP`, `PHYS-MAP`) stabilized. |
| v1.0 | First stable release. `saund-kling` + `saund-seedance` adapters. |
| v1.1 | Reverse compiler MVP (audio → SAUND). |
| v2.0 | Live runtime. Brand layer. |

---

## 16. Relation to the Reference Implementation

The reference implementation **SAUND SUNO COMPILER SKILL v3.4** (by 36z6) is the first conforming compiler of this protocol. It implements §4–§9 fully for the Suno audio target. This protocol document is the **normative specification** the reference implementation conforms to.

Where the reference implementation contains Suno-specific projections (STYLE/LYRICS field ceilings, Suno budget classes P1–P4), these are marked as adapter-level details and are **not** part of the protocol core.

---

## 17. Attribution

SAUND Protocol and the SAUND SUNO COMPILER SKILL were designed by **36z6** between 2025 and 2026. The Delta-Shape Encoding (DSE) notation was developed iteratively through real production use across industrial, oriental funk, trance, bassline techno, phonk, and commercial genres.

---

## 18. Next Steps (for the reader)

1. **Review** this spec. Open issues on the repository when published.
2. **Try** the reference implementation: copy any example from `/examples` into Suno and observe the difference vs. freeform prompting.
3. **Contribute** DATA (timbre families, groove patterns, SFX vocabularies) via INTAKE — no protocol version bump required.
4. **Build** an adapter for your favorite backend.

---

*End of SAUND Protocol Specification v0.1.*
```
