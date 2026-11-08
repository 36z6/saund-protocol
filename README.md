# SAUND Protocol

**A declarative standard for deterministic cross-modal AI media generation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1-blue.svg)](SAUND_PROTOCOL_SPEC_v0.1.md)

SAUND Protocol is a declarative, versioned, backend-agnostic specification for describing multimodal media artifacts (audio, video, voice, brand identity) in a single source document.

One authorial intent → multiple AI generation backends (Suno, Udio, Runway, Kling, Seedance, ElevenLabs, Midjourney) → synchronized output.

## Why SAUND?

Today's AI media tools are **silos**:
- Each model speaks its own prompt dialect
- Cross-modal sync is done manually in DAW/NLE
- Authorial intent is lost in translation
- No way to version, diff, or fork a media project

SAUND fixes this by introducing a **canonical intermediate representation** — the same role MIDI played for hardware synths, Markdown plays for documents, YAML plays for configuration.

## Quick Start

### 1. Read the Protocol

Start with **[SAUND_PROTOCOL_SPEC_v0.1.md](SAUND_PROTOCOL_SPEC_v0.1.md)** — the normative specification.

### 2. Try the Reference Implementation

The reference implementation **SAUND SUNO COMPILER SKILL v3.4** is the first conforming compiler. See **[SAUND_COMPILER_SPEC_v3.4.md](SAUND_COMPILER_SPEC_v3.4.md)** for the full technical spec.

### 3. Generate Your First Track

Copy any example from `/examples` into Suno and observe the difference vs. freeform prompting.

## License

MIT License. See [LICENSE](LICENSE).

## Attribution

SAUND Protocol and SAUND SUNO COMPILER SKILL designed by **36z6** (2025-2026).

---

**Built with SAUND v3.4** · Protocol v0.1
