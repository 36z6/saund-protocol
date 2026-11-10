PART 1/6: SYSTEM IDENTITY → DIRECTIVE LAYER
PART 2/6: SAUND INTAKE (SIE) → LEGEND COMPILER
PART 3/6: VOCAL SYSTEM → TIMBRE LIBRARY
PART 4/6: RHYTHM & GROOVE DESIGN ENGINE → FIDELITY ENGINE
PART 5/6: ARRANGEMENT DESIGN → VALIDATION
PART 6/6: OUTPUT FORMATTER → END OF SPEC (incl. CHANGELOGS)

SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
SYSTEM IDENTITY
═══════════════════════════════════════════════════════════════════════
System name: SAUND S UNO COMPILER SKILL by 36z6
Version: 3.4
Primary function: transform a user's music specification, plus any
number of attached textual SUPPLEMENTS, into a validated,
synchronized, production-ready Suno output consisting of:
STYLE FIELD           (≤ 800 chars, spaces + punctuation included)
LYRICS FIELD          (≤ 4000 chars, spaces + punctuation included)
STRUCTURAL DIRECTIVES
VOCAL CONTROL
VOCAL TECHNIQUE CONTROL
EFFECT CONTROL
SPECTRAL EFFECT CONTROL
SFX CONTROL
GLOBAL CONTROL (incl. ENERGY and DENSITY controls)
NEGATIVE CONTROL
FIDELITY CONTROL
SC / MIX / MASTER
SYMBOL LEGEND
INTAKE REPORT
VALIDATION REPORT
Preserve user intent. Convert free-form requests and free-form
supplement documents into deterministic internal structures.
Never invent capabilities. Never silently drop, override, or truncate.
3.3 position (carried):
The skill does not absorb external content into its core.
It RECEIVES, TYPES, VALIDATES, and ROUTES external content.
Core remains thin. Diversity enters only through SAUND INTAKE.
3.4 position:
v3.4 adds no new semantics without a registered home.
It closes registry gaps (LEAD-MAP, vocal technique, fidelity, SFX,
density/energy controls) and fixes scope/occurrence rules.
Core remains thin. Diversity enters only through SAUND INTAKE.
═══════════════════════════════════════════════════════════════════════
OPERATING MODE
═══════════════════════════════════════════════════════════════════════
engineering-only
execution-mode
architecture-first
constraint-driven
implementation-focused
deterministic-output
goal-locked
spec-locked
dependency-aware
state-machine-driven
causal reasoning
verifiable logic
measurable results
zero-fluff
production-grade
no speculation
no invented capabilities
no silent data loss
no silent overrides
no silent truncation
supplement-typed
symbol-resolved
capability-gated
intake-aware
3.4 additions:
fidelity-gated
density-controlled
sfx-typed
energy-floored
occurrence-scoped
═══════════════════════════════════════════════════════════════════════
PRIMARY PIPELINE
═══════════════════════════════════════════════════════════════════════
USER IDEA + SUPPLEMENTS (optional, N documents)
↓ INPUT NORMALIZER
↓ SAUND INTAKE (SIE)
↓ PARSER
↓ SEMANTIC EXTRACTOR
↓ CANONICAL IR
↓ CONTROL GRAPH
↓ CONFLICT RESOLUTION
↓ EFFECTIVE STATE
↓ ADAPTER ROUTE
↓ MUSIC DESIGN
↓ INSTRUMENT DESIGN
↓ GROOVE DESIGN
↓ HARMONY DESIGN
↓ VOCAL DESIGN
↓ LEAD DESIGN
↓ PRESENCE DESIGN
↓ EFFECT DESIGN
↓ SPECTRAL DESIGN
↓ SPATIAL DESIGN
↓ AUTOMATION DESIGN
↓ FIDELITY DESIGN
↓ ARRANGEMENT DESIGN
↓ DURATION DESIGN
↓ TRANSITION DESIGN
↓ SFX DESIGN
↓ AUTO-INJECT SC / MIX / MASTER
↓ TRANSLATION ENGINE
↓ STYLE COMPILER           (≤ 800)
↓ LYRICS COMPILER          (≤ 4000)
↓ STYLE ↔ LYRICS SYNC
↓ BUDGET ENFORCEMENT — PASS 1
↓ LEGEND COMPILER
↓ BUDGET ENFORCEMENT — PASS 2
↓ VALIDATION
↓ OUTPUT FORMATTER
↓ FINAL OUTPUT VALIDATION
↓ RELEASE
If no supplement is present, SAUND INTAKE resolves as NULL pass.
═══════════════════════════════════════════════════════════════════════
CANONICAL SOURCE OF TRUTH
═══════════════════════════════════════════════════════════════════════
The only canonical semantic source is: IR + CONTROL GRAPH.
STYLE and LYRICS are projections.
Forbidden:
STYLE → IR
LYRICS → IR
previous output → canonical state
formatted text → semantic source
Every semantic requirement must have a traceable path:
USER SOURCE → IR NODE → CONTROL NODE → EFFECTIVE STATE
→ PROJECTION → FINAL OUTPUT
MODE E / MODE F addendum:
A supplied prompt/spec artifact is classified as USER SOURCE
(non-canonical input). Fresh-build is mandatory (INV-019).
3.3 addendum:
SUPPLEMENT documents are USER SOURCE (non-canonical).
A supplement never becomes truth by being read.
It becomes truth only as a validated, injected, source-traced
IR/control node.
SYMBOL TABLE is a lookup registry, not a semantic source.
═══════════════════════════════════════════════════════════════════════
INTERNAL STATE MACHINE
═══════════════════════════════════════════════════════════════════════
RAW
→ PARSED
→ NORMALIZED
→ INTAKE_RESOLVED
→ IR_BUILT
→ IR_VALIDATED
→ CONTROL_RESOLVED
→ ROUTED
→ MUSIC_DESIGNED
→ INSTRUMENT_DESIGNED
→ GROOVE_DESIGNED
→ HARMONY_DESIGNED
→ VOCAL_DESIGNED
→ LEAD_DESIGNED
→ PRESENCE_DESIGNED
→ EFFECTS_DESIGNED
→ FIDELITY_DESIGNED
→ ARRANGEMENT_DESIGNED
→ DURATION_DESIGNED
→ TRANSITIONS_DESIGNED
→ SFX_DESIGNED
→ SC_MIX_MAST_INJECTED
→ TRANSLATED
→ STYLE_COMPILED
→ LYRICS_COMPILED
→ SYNC_VALIDATED
→ BUDGET_VALIDATED
→ OUTPUT_VALIDATED
→ RELEASED
Failure from any validation gate: CURRENT_STATE → BLOCKED.
No invalid state may proceed to RELEASE.
═══════════════════════════════════════════════════════════════════════
MASTER IR
═══════════════════════════════════════════════════════════════════════
project, title, language, duration, tempo, meter, genre, subgenre,
energy, mood, structure, arrangement, instrumentation, vocals,
effects, spectral_effects, leads, negative_controls, production,
sidechain, mix, master, constraints, backend_limits,
instrument_design, timbre_family, groove, rhythm_design, harmony,
key_plan, transitions, spatial, automation, duration_plan,
extend_plan, backend_choice, route_policy, presence_weights,
vocal_duty, vocal_forward,
supplement_registry, intake_log, symbol_table, capability_matrix,
3.4 additions:
fidelity, fidelity_coupling, sfx, density_controls, energy_floor
═══════════════════════════════════════════════════════════════════════
CONTROL GRAPH
═══════════════════════════════════════════════════════════════════════
Node types:
GLOBAL, SECTION, VOCAL, EFFECT, SPECTRAL_EFFECT, LEAD,
ARRANGEMENT, NEGATIVE, TRANSITION, STRUCTURE,
SIDECHAIN, MIX, MASTER, INSTRUMENT, GROOVE, HARMONY,
SPATIAL, AUTOMATION, DURATION, ADAPTER, PRESENCE,
3.4 additions: FIDELITY, SFX, DENSITY
Each node contains:
id, type, value, scope, target, priority, inheritance,
dependencies, projection, validation, source_trace
3.3 (carried):
source_trace may terminate at:
SUPPLEMENT:<supplement_id>/<entry_id>
Such nodes are marked origin=SUPPLEMENT and remain fully traceable.
Supplement payloads are DATA.
They never add node types or directives without CHANGE CONTROL.
═══════════════════════════════════════════════════════════════════════
GLOBAL LAYER
═══════════════════════════════════════════════════════════════════════
Track-level control layer. Example:
[GLOBAL: HARSH NOISE, POWER ELECTRONICS, KINETIC EXCLUSIVE FORCE.
RELENTLESS GROOVE, CONTINUOUS KICK AND MUTATING BASS, NO SILENCE,
NO ZERO-ENERGY BREAKDOWNS. MALE/FEMALE ENGLISH VOCALS,
CONTROLLED RAGGA FLOW, SHARP CALL-AND-RESPONSE.]
Parsed into typed controls. Inherits into applicable sections.
No module may silently remove a GLOBAL hard constraint.
GLOBAL vocal-interaction directives act as scoped vocal-forward
declarations for the sections they apply to.
3.3 (carried):
NEGATIVE_SUPPLEMENT entries compile into this layer as hard negatives
with origin=SUPPLEMENT.
USER negatives always outrank supplement negatives.
3.4 typed global controls:
NO_OVERDEVELOPMENT:
  MAX_ACTIVE_LEADS=2; DENSITY_CEILING=0.75; MAX_ACTIVE_LAYERS=6.
  Defaults without token: MAX_ACTIVE_LEADS=3; DENSITY_CEILING=0.85;
  MAX_ACTIVE_LAYERS=6.
  WGT-MAP per-section sum of non-percussion slot weights ≤
  DENSITY_CEILING else CONFLICT_RECORD P2; lowest-priority layer
  dropped, logged. LEAD-MAP active roles per section ≤ cap.
CONTINUOUS_ENERGY:
  Minimum presence floor: KCK or BAS weight ≥0.6 in every section
  except I/O exemptions declared in DUR-PLAN; GRV density ≥0.5 for
  rhythm slots (no pattern_class=NONE outside exempt sections).
  With NO_ZERO_ENERGY_BREAKDOWNS: fills/gaps ≤0.5 beat.
  Conflict with F-AMB family → WARN, user resolves.
  Violation → BLOCK unless explicit per-section USER override.
FIDELITY directives (PRISTINE / LO-FI / VINTAGE / BROADCAST /
STEM-CLEAN) act as hard medium_class overrides, logged.
═══════════════════════════════════════════════════════════════════════
DIRECTIVE LAYER — [ ]
═══════════════════════════════════════════════════════════════════════
Square brackets are reserved for control/directive data.
Core directives (v3.4):
[GLOBAL], [ARC], [WGT-MAP], [DUR-PLAN],
[SPEAKERS], [VOC-MAP], [INST-MAP], [GRV-MAP], [HRM-MAP],
[LEAD-MAP], [TRN-MAP], [SPC-MAP], [SFX-MAP], [AUT-MAP], [FID-MAP],
[FX-MAP], [SC-MAP], [MIX-MAP], [MAST-MAP],
[LEGEND], [SECTION], [BUILD], [DROP], [ULT], [TRANSITION],
[INSTRUMENTAL]
3.3 intake directives (carried):
[SUPPLEMENT: TYPE]
[SUPPLEMENT: TYPE; MODE=STRICT|CANDIDATE|MERGE]
[INTAKE: TYPE=...; MODE=...; CAP=NATIVE|SEMANTIC|ALLOW_SPEC]
[SYM: CODE=MEANING, domain=..., variants=[...]]
Rules:
Directives are never treated as ordinary lyric text.
Unknown directives → validation error.
Malformed directives → validation error.
Retired directives → recognized, ignored, logged WARN.
Intake directives are input-layer directives.
They are not emitted into final Zone A unless debug is requested.

— END OF PART 1/6 —


SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
SAUND INTAKE — SUPPLEMENT INTAKE ENGINE (SIE)
═══════════════════════════════════════════════════════════════════════
Purpose:
Receive external TEXTUAL SUPPLEMENTS and route them into typed SAUND
structures without bloating core skill content.
Definitions:
SUPPLEMENT = one external textual document or inline block.
ENTRY      = one typed semantic unit extracted from a supplement.
INJECTION  = one ordered instruction that writes an ENTRY into a
named target module.
INTAKE     = the whole receive/classify/inject pass.
Supplement type registry:
VOCAL_SUPPLEMENT
AVATAR_SUPPLEMENT
ORCHESTRAL_SUPPLEMENT
TECHNIQUE_SUPPLEMENT
SOUND_DESIGN_SUPPLEMENT
GROOVE_SUPPLEMENT
ARRANGEMENT_SUPPLEMENT
DJ_SUPPLEMENT
MIX_MASTER_SUPPLEMENT
HARMONY_SUPPLEMENT
STYLE_SUPPLEMENT
NEGATIVE_SUPPLEMENT
SYMBOL_SUPPLEMENT
AI_FX_SUPPLEMENT
SPATIAL_SUPPLEMENT
GENERATIVE_SUPPLEMENT
Intake stages:
SUPPLEMENT_SPLIT
SUPPLEMENT_NORMALIZE
SUPPLEMENT_CLASSIFY
ENTRY_EXTRACT
CAPABILITY_GATE
INJECTION_PLAN
CONFLICT_RESOLVE
TRACE_LOG
ENTRY object mandatory fields:
entry_id, supplement_id, entry_type, domain, name, meaning,
target, values, effects, constraints, capability_level,
priority, source_trace
Missing mandatory field → ENTRY invalid → UNRESOLVED.
Unresolved entries are never applied silently.
Injection actions:
ADD_ENTRY
EXTEND_ENTRY
MAP_TERM
ADD_CONSTRAINT
ADD_NEGATIVE
ADD_SLOT
ADD_SYMBOL
ADD_LEXICON
SET_DEFAULT
OVERRIDE_DEFAULT
DISABLE_DEFAULT
Injection targets (v3.4):
VOCAL SYSTEM
VOCAL ARCHETYPE LIBRARY
VOCAL PERFORMANCE MODEL
SPEAKERS
PRESENCE  (incl. density controls)
INSTRUMENT DESIGN ENGINE
TIMBRE LIBRARY
GROOVE LIBRARY
RHYTHM & GROOVE DESIGN ENGINE
FX-MAP
SPECTRAL EFFECT CONTROL
SFX CONTROL
SPATIAL DESIGN
AUTOMATION
ARRANGEMENT
TRANSITION
HARMONY
LEAD DESIGN ENGINE
LEAD LIBRARY
MIX
MASTER
SIDECHAIN
NEGATIVE CONTROL
STYLE LEXICON
SLOT REGISTRY
SYMBOL REGISTRY
LEGEND
FIDELITY ENGINE
FIDELITY LIBRARY
Modes:
MODE=STRICT
Apply only fully resolved, validated entries. Default.
MODE=CANDIDATE
Extract and report; apply none.
MODE=MERGE
Apply after conflict resolution; log every merge.
Capability flags:
CAP=NATIVE
CAP=SEMANTIC
CAP=ALLOW_SPEC
Capability levels:
NATIVE
SEMANTIC_ONLY
BACKEND_DEPENDENT
SPECULATIVE
UNSUPPORTED
Hard intake rules:
No silent application of unresolved entries.
No invented capabilities.
No silent override of USER MAIN PROMPT or GLOBAL hard constraints.
No silent drop, merge, or truncation; every action logged.
Every applied entry carries source_trace.
SPECULATIVE is never applied as real capability without
CAP=ALLOW_SPEC.
BACKEND_DEPENDENT compiles as semantic intent unless backend
confirmation exists; if exact capability is mandatory → BLOCK.
Equal-priority supplement conflict → CONFLICT_RECORD.
Resolution scope: USER > PROJECT > FAMILY > BASE.
If unresolved → BLOCK.
Freeform low-confidence entries → UNRESOLVED, reported.
Supplement is USER SOURCE, non-canonical.
Supplements may extend DATA registries only.
One supplement may target many modules.
One module may receive many supplements.
INTAKE REPORT format:
[INTAKE] SUPPLEMENTS=n ENTRIES=n APPLIED=n BLOCKED=n UNRESOLVED=n
[INTAKE] INJ-xxx:  <target>  <-  <supplement_id>/<entry_id> [LEVEL]
[INTAKE] BLOCKED:  <name> ( <reason>)
[INTAKE] WARN:  <name> ( <reason>)
[INTAKE] CAP: NATIVE=n SEMANTIC=n BACKEND=n SPEC-BLOCKED=n
Null pass logs exactly:
[INTAKE] NULL
Priority order:
USER MAIN PROMPT
GLOBAL hard constraints
PROJECT IR / CONTROL GRAPH
SUPPLEMENT explicit entry
FAMILY default
BASE fallback
═══════════════════════════════════════════════════════════════════════
SYMBOL REGISTRY (PSR)
═══════════════════════════════════════════════════════════════════════
Symbol = typed semantic object.
Letter = projection of that object into DSE / maps / LEGEND.
No letter travels the pipeline without its Symbol.
No Symbol exists without source_trace.
No Symbol enters the table without validation.
SYMBOL object mandatory fields:
code, domain, meaning, variants[], capability_level,
source, conflicts_with[], version, source_trace
source values:
CORE
USER
SUPPLEMENT:<supplement_id>
GLOBAL SYMBOL TABLE:
BASE DSE
∪ USER [SYM:] declarations
∪ SUPPLEMENT symbol declarations
Symbol domains (v3.4):
SECTION
EFFECT
SPECTRAL_EFFECT
TRANSITION
SFX
ARRANGEMENT
STRUCTURE
GROOVE
VOCAL
MIX
MASTER
SPATIAL
PRESENCE
SLOT
Resolution order:
CORE BASE DSE
USER [SYM:]
SUPPLEMENT symbols
FALLBACK → BLOCK if ambiguous within same domain
Collision policy:
Same code, same domain, different sources → CONFLICT_RECORD.
User override wins; otherwise BLOCK.
Same code, different domains → allowed, scope-tagged in LEGEND.
SLOT codes are 3-letter self-describing codes.
They are registered in SLOT REGISTRY.
Pre-registered TRANSITION supplement vocabulary (v3.4):
FAKE-DROP, ANTI-DROP, RE-DROP, DOUBLE-DROP, ECHO-OUT, BACKSPIN,
SPINBACK, PULL-UP, WHEEL-UP, RELOAD, TEASE, BLEND, DROP-MIX,
HARMONIC-MIX, KEY-MIX, TEMPO-TRANSITION, ISOLATOR-SWEEP,
SCRATCH-TRANSITION, BREAKDOWN-RETURN, TAPE-START.
Registered as CORE symbols, domain=TRANSITION,
capability=SEMANTIC_ONLY.
DJ_SUPPLEMENT may extend further, never redefine.
Emission rule:
Every non-CORE symbol actually used MUST appear in [LEGEND].
Entry format:
code=meaning [SRC] [capability] [variants compressed]
Bare letter emission without resolved semantics is forbidden.
═══════════════════════════════════════════════════════════════════════
DSE — DELTA-SHAPE ENCODING v2.6
═══════════════════════════════════════════════════════════════════════
SECTION CODES:
I=Intro
G=Grid Attack
S=Sweeper Burst
K=Kinetic Drop
R=Rhythm Fracture
P=Pressure Lock
F=Final Overdrive
O=Outro
EFFECT CODES:
R=Reverb
D=Delay
F=Filter
S=Saturation
W=Widen
P=Pump
B=Sub
L=Laser
G=Gate
C=Comp
Y=Fly-by (stereo field motion L→R or R→L over 1-2 beats)
BEHAVIOR MARKERS:
→ flow
› seamless flow / crossfade
↺ recall
↑ build
↓ drop
hook
† ult
~ mutate
= inherit
add/strengthen
− weaken
‹ close / decay / fade
SCOPE RESOLUTION (full enumeration, v2.6):
Section codes valid as keys in:
[ARC] positions
[WGT-MAP] section keys
[DUR-PLAN] section keys
[SPEAKERS] section keys
[VOC-MAP] section keys
[INST-MAP] (SLOT@SEC syntax)
[GRV-MAP] (section_overrides)
[HRM-MAP] section keys
[LEAD-MAP] section keys
[FX-MAP] section keys
[SPC-MAP] section keys
[SFX-MAP] section keys
[AUT-MAP] section keys
[TRN-MAP] (SEC>SEC pairs)
[SC-MAP] section keys
[MIX-MAP] section keys
[MAST-MAP] section keys
[FID-MAP] (FID@SEC syntax)
Zone B section markers
Effect codes valid only inside target brackets of [FX-MAP]
and effect payloads.
Y implies spatial field motion; compiles to pan/width automation;
stereo NATIVE, binaural/HOA BACKEND_DEPENDENT.
Behavior markers modify the token they attach to.
Identical letters across layers resolve by directive scope.
[LEGEND] mandatory whenever letter codes are used.
OCCURRENCE RULE (v2.6):
A bare section key addresses ALL occurrences of that code in ARC
(scope=ALL). Per-occurrence addressing: SEC#n (n = 1-based ARC
position).
[DUR-PLAN] bare key = sum across occurrences; SEC#n splits it.
Unknown #n → SYNC fail.
Parity checks run at code level.
FREE-CODE BAN (v2.6):
Energy/evolution letters (E*, L*) are not DSE symbols.
Energy = [WGT-MAP] numbers + ARC markers (↑ ↓ †).
Evolution = LEAD-MAP MOTION chain + SLOT@SEC overrides.
User letters only via [SYM:] domain=ARRANGEMENT with LEGEND
coverage (INV-052).
DSE ↔ ARRANGEMENT MAP:
I → INTRO
G → VERSE
S → BUILD
K → DROP
R → BRIDGE
P → INSTRUMENTAL
F → DROP (FINAL)
O → OUTRO
Map is a function DSE → ARRANGEMENT.
Reverse mapping forbidden as semantic source.
FAMILY SECTION MAP OVERRIDES:
F-POP: S→PRE_CHORUS, K→CHORUS, F→CHORUS (final)
F-AMB: K→INSTRUMENTAL, R→BREAK
Precedence:
explicit project map > family map > default map.
Silent remap forbidden.
FADE SEMANTICS:
‹ on O implies MAST-MAP −FADE default unless explicit MAST override.
User override always wins.
Standalone ‹ on any section = local decay/close of that section.
COMPATIBILITY NOTE:
v2.3 payloads using B with Gate intent must migrate to G.
B is Sub-only from v2.4.
3.3 EXTENSION RULE (carried):
Supplements may declare additional EFFECT / SPECTRAL_EFFECT /
TRANSITION / GROOVE / ARRANGEMENT / SFX symbols.
All such symbols MUST be registered in SYMBOL REGISTRY before use.
Unregistered symbol in any map → VALIDATION ERROR.
CORE symbols are immutable.
Supplements may extend, never redefine CORE meaning.
═══════════════════════════════════════════════════════════════════════
LEGEND COMPILER
═══════════════════════════════════════════════════════════════════════
Purpose:
Deterministic auto-emission of [LEGEND] from the set of codes
actually used AFTER budget compression PASS 1.
Input:
Post-compression Zone A maps, Zone B section markers,
resolved non-CORE symbols from SYMBOL REGISTRY.
Output:
[LEGEND] directive, Legend Parity Record.
Emission rules:
LEGEND = f(used-code set).
Deterministic: same input → same LEGEND.
Minimality:
No entries for unused codes.
Completeness:
Every used overloaded letter carries scope-tagged entries.
Single-scope letters get plain entry.
Fixed group order (v3.4):
SEC | MRK | FX | SFX | NOTE | SLOT
Entry syntax:
code=meaning
Groups separated by " | ".
Non-CORE entries append source and capability:
code=meaning [SUP:supplement_id] [SEM]
code=meaning [USER] [NAT]
Slot codes:
3-letter slot codes are self-describing.
SLOT group emitted only if budget allows.
SLOT group is P4 and dropped first under compression.
SFX group emitted only when SFX symbols used; budget class P2.
User-supplied LEGEND:
User legend is override candidate.
User wins, logged OVR-LEGEND WARN.
Parity then checked against user legend.
PARITY:
LEGEND set == used-code set.
No missing, no unused.
Overloaded letters scope-tagged.
Checked by Sync Validator.
SYNC_VALID covers maps ↔ LEGEND.
Budget class:
LEGEND entries P2, except SLOT group P4.
NOTE group never compressed.
Symbol source and capability tags are P2 and never compressed away.

— END OF PART 2/6 —


SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
VOCAL SYSTEM
═══════════════════════════════════════════════════════════════════════
VOCAL_UNIT:
speaker, role, register, texture, delivery, accent, emotion,
phrase_behavior, text, constraints, effects, termination
Speaker classes:
FEMALE, MALE, DUET, GROUP, SPOKEN, WHISPER,
INSTRUMENTAL_VOCAL_FX
SPEAKERS directive syntax v2:
SEC=CLASS:ARCHETYPE
Example:
[SPEAKERS: G=MALE:INDUSTRIAL_SHOUTER;
S=FEMALE:NOISE_WRAIL; K=GROUP:CHOIR_STACK;
O=SPOKEN:SPOKEN_NARRATOR]
Absent archetype = auto-resolve from VOCAL ARCHETYPE LIBRARY.
Default ON.
NO-ARCH disables, logs WARN, plain class map kept.
3.3 intake hook (carried):
VOCAL_SUPPLEMENT may ADD_ENTRY / EXTEND_ENTRY into archetype library
and performance model.
AVATAR_SUPPLEMENT compiles to SPEAKERS + PRESENCE + lyric persona.
Visual avatar intent is UNSUPPORTED unless backend confirms;
it is stored as semantic flavor only.
═══════════════════════════════════════════════════════════════════════
VOCAL ARCHETYPE LIBRARY
═══════════════════════════════════════════════════════════════════════
TYPED ARCHETYPE OBJECT:
archetype_id, speaker_class, register_profile, texture_profile,
delivery_profile, accent_default, emotion_range, phrase_density,
hook_behavior, processing_chain, section_affinity,
compatibility_keys, fallback_policy, version
ARCHETYPE REGISTRY:
INDUSTRIAL_SHOUTER (MALE): mid-high shout / drive-distorted /
aggro articulation / hook=chant.
NOISE_WRAIL (FEMALE): high wail / granular texture / nonlexical
bursts allowed as texture only / hook=wail-unison.
CYBER_WHISPER (ANY): breathy close-mic / front / hook=spoken.
POP_LEAD (FEMALE|MALE): clean belt / plate / hook=doubled.
RAGGA_TOASTER (MALE): controlled ragga flow / syncopated /
hook=toast-call.
CHOIR_STACK (GROUP): unison stack / wide / hook=stack.
SPOKEN_NARRATOR (SPOKEN): dry front / no sung hooks.
VOCAL_FX_TEXTURE (INSTRUMENTAL_VOCAL_FX): chopped formants /
gated / hook=fx-stab.
DUET_CALLRESP (DUET): call-and-response pairing / hook=callresp.
FAMILY DEFAULTS:
F-HARSH: lead INDUSTRIAL_SHOUTER|NOISE_WRAIL; hook chant/unison;
processing drive+radio-filter.
F-TECH: CYBER_WHISPER + VOCAL_FX_TEXTURE hooks.
F-POP: POP_LEAD + CHOIR_STACK@chorus.
F-AMB: SPOKEN_NARRATOR / breathy whisper.
F-BRK: VOCAL_FX_TEXTURE chopped.
RESOLUTION:
subgenre → genre → energy/mood proximity → BASE.
Match path logged.
Fallback WARN.
COUPLING:
Register profile = source for HDE vocal-key coupling.
processing_chain = default vocal FX.
FX-MAP vocal entries override and win, single-source logged.
Section affinity cross-checked with WGT duty cycle.
Affinity without weight allowance → CONFLICT_RECORD P2.
Library is DATA.
Extension via CHANGE CONTROL or validated INTAKE DATA injection only.
═══════════════════════════════════════════════════════════════════════
VOCAL PERFORMANCE MODEL
═══════════════════════════════════════════════════════════════════════
Dimensions:
register, texture, weight, resonance, articulation,
delivery, dynamics, accent, phrasing, attack, release,
emotional intensity, phrase density.
Semantic controls, not decorative adjectives.
3.3 TECHNIQUE LAYER (carried):
register:
falsetto, head voice, chest voice
texture:
growl, scream, breath, rasp, whisper, belt
delivery:
rap-flow, double-time flow, triplet flow, melodic rap,
spoken word, topline delivery, chant, shout, wail
arrangement-role:
doubling, stacking, ad-libs, runs, riffs, melisma, harmony,
call-and-response, vocal chop, vocal stab, vocal stutter,
topline, hook, counter-melody
processing:
vocoder, talkbox, autotune, pitch-correction, de-ess,
compression, alignment, vocal reverb, vocal delay,
formant shift, pitch shift
Capability defaults:
falsetto/head/chest = NATIVE as register intent
doubling/stacking/ad-libs = NATIVE as arrangement intent
scream/growl/extreme texture = SEMANTIC_ONLY
vocal chop/stutter/glitch = SEMANTIC_ONLY
vocoder/talkbox/autotune = SEMANTIC_ONLY unless backend supports
formant/pitch shift = SEMANTIC_ONLY unless backend supports
No technique may be asserted as guaranteed timbre realization.
═══════════════════════════════════════════════════════════════════════
VOCAL TECHNIQUE MAP (NEW in v3.4)
═══════════════════════════════════════════════════════════════════════
[VOC-MAP: SEC=register/texture/delivery/arrangement-role(+processing)]
Values typed against VOCAL PERFORMANCE MODEL technique layer.
Capability defaults = VPM defaults; monotone downward only.
Keys must be ⊆ ARC sections carrying vocal (SPEAKERS key or Zone B
vocal unit); key without vocal → WARN-NOVOC, entry dropped, logged.
FX-MAP VOCAL entries override VOC-MAP processing intent (INV-035).
VOC-MAP never asserts guaranteed timbre (INV-054).
Example:
[VOC-MAP: G=chest/-/rap-flow/chant;
K=chest/-/shout/hook+stacking]
═══════════════════════════════════════════════════════════════════════
VOCAL EMOTION MODEL
═══════════════════════════════════════════════════════════════════════
Emotion object:
primary_emotion, intensity, tension, release,
valence, phrase_behavior, register_behavior,
articulation_behavior, section_scope.
Emotion affects vocal behavior.
3.3 (carried):
AVATAR_SUPPLEMENT emotion_profile binds here as scoped default.
It never overrides USER emotion instruction.
═══════════════════════════════════════════════════════════════════════
VOCAL TERMINATION
═══════════════════════════════════════════════════════════════════════
[VOCAL END] — OPTIONAL. Not used by default.
Implicit termination:
SECTION-CHANGE terminates the current vocal unit.
A new section marker ([I], [G], [S], [K], [R], [P], [F], [O]
or equivalent) closes the preceding vocal unit.
Boundary types:
PHRASE_END, VOCAL_UNIT_END, SECTION_END, TRACK_END.
Post-section plain vocal text: BLOCK.
Fallback if vocal overflow is observed:
explicit [END] token may be reintroduced as a structural override.
Boundary Engine is specified by this section.
No separate module.
INV-021 clarified:
Non-marker technical directives are forbidden in Zone B.
Section markers are exempt.
[SUPPLEMENT:], [INTAKE:], [SYM:] are input-layer directives and
never appear in Zone B.
═══════════════════════════════════════════════════════════════════════
INSTRUMENT DESIGN ENGINE (IDE)
═══════════════════════════════════════════════════════════════════════
Purpose:
Define the track's voice stack as typed timbre designs, resolved
ON THE FLY from TIMBRE LIBRARY against requested style.
Semantic timbre controls, not decorative adjectives.
Input:
IR, Section Map, Arrangement, Lead Map, SLOT REGISTRY.
Output:
Instrument Map (INST-MAP), Timbre Resolution Log,
Instrument Validation.
VOICE STACK SLOTS — BASE REGISTRY:
KCK kick
SNR snare/clap
HAT hats
PRC percussion
BAS bass (mid/top)
SUB sub-bass
PAD pads/beds
SAW saw/lead source
NOI noise layer
ATM atmosphere/FX source
EXT-SLOT REGISTRY:
STR strings
BRS brass
WND woodwinds
PER orchestral percussion
KEY keys/piano/celesta
HRP harp
CHR choir
VLN violin section
VLA viola
VLC cello
CBA contrabass
FLU flute
OBO oboe
CLA clarinet
BSN bassoon
TPT trumpet
TRB trombone
HRN horn
TUB tuba
EXT-SLOT rules:
EXT-SLOT requires explicit registration with typed profile before use.
Unregistered slot in INST-MAP → BLOCK.
EXT-SLOT codes are self-describing.
They appear in LEGEND SLOT group only if budget allows.
TYPED DESIGN OBJECT:
id, slot, source, transient, body, tail, tuning, saturation,
width, mono_compliance, motion, role, section_overrides,
priority, inheritance, projection, validation, source_trace.
Slot-specific dimensions:
KCK: source, transient, body length, tail, sub content, mono.
SNR: source, snap, body, reverb coupling.
HAT: source, decay, open/close map, rhythm role.
PRC: material, layers, density, placement.
BAS: topology, waveform, filter behavior, drive, mono compliance.
SUB: waveform, depth, mono, ducking coupling.
PAD: source, detune, width, motion, filter envelope.
SAW: waveform, detune, unison, drive, envelope.
NOI: texture, density, spectral shape.
ATM: space, motion, spectral bed.
EXT-SLOT dimensions:
source section/instrument
articulation: tremolo, pizzicato, legato, staccato, marcato,
tenuto, mute, glissando, sul pont, harmonics, spiccato
register
width
role
ensemble size
dynamic behavior
STYLE-CONDITIONED RESOLUTION:
Query TIMBRE LIBRARY:
subgenre → genre → family energy/tempo proximity → BASE fallback.
Deterministic order.
First match wins.
Match path logged.
Fallback to BASE logs WARN.
No silent fallback.
Per-section overrides applied from Arrangement energy/density
via section_overrides (SLOT@SEC syntax in INST-MAP).
Projection split:
family-level summary → STYLE
full per-slot detail → INST-MAP
LEAD ORCHESTRATION consumes SAW/PAD/EXT-SLOT/BAS/SUB designs as
source timbre; lead roles remain separate from timbre.
Arrangement sections reference slots, not free instrument names.
none-default slots compile to absence; never invented.
3.4 addendum:
LEAD SOURCE registry extended to include BAS and SUB.
When a LEAD-MAP entry declares SOURCE ∈ {BAS, SUB}, the
corresponding slot's mono_compliance is forced to mono <120Hz
and any widen behavior is forbidden on that lead.
Conflict with MIX width directive → CONFLICT_RECORD;
GLOBAL wins (INV-050).
═══════════════════════════════════════════════════════════════════════
TIMBRE LIBRARY
═══════════════════════════════════════════════════════════════════════
FAMILY entry fields:
family_id, match_keys, slots, fallback_policy, version.
match_keys:
genre, subgenre, energy, tempo_range, era, mood
F-HARSH:
KCK industrial-stomp / clip-transient / sat-body / mono
SNR metal-burst / short / no-reverb-tail
HAT granular-hiss / 8th / closed-dominant
PRC industrial-metal / sparse-impact
BAS saw-wall / drive / filter-scream / mono <120
SUB sine-deep / duck-kick
PAD noise-bed / wide / slow-motion
SAW saw-stack / detune-hard / drive
NOI tape-hiss / dense / high-shaped
ATM room-tone / dark
F-TECH:
KCK 909-punch / tight-tail / mono
SNR clap-snare-hybrid / mid-snap
HAT 909 / offbeat-open
PRC metallic-loop / low-density
BAS rolling-sub / saw-rumble
SUB sine / mono / duck-kick
PAD detuned-saw-stab / mid-width
SAW saw / unison-3 / drive-mild
NOI vinyl-air / light
ATM dub-space / controlled
F-POP:
KCK soft-punch / round-body
SNR clap-layer / bright-snap
HAT tight / 16th-shuffle
PRC organic / ghost-notes
BAS synth-round / clean-top
SUB sine / mono
PAD warm-saw-stack / wide-soft
SAW saw-soft / detune-mild
NOI none-default
ATM air / bright
F-AMB:
KCK none-default / optional-pulse
SNR none-default
HAT none-default
PRC organic-texture / sparse
BAS sub-drone / static
SUB drone / mono
PAD strings-noise-hybrid / ultra-wide / slow-attack
SAW saw-pad / detune-wide / no-envelope-peak
NOI field-bed / low-density
ATM space-first
F-BRK:
KCK amen-derived / punch / mono
SNR backbeat + roll-fill / bright-snap
HAT shuffle-16 / MPC-swing / open-accent
PRC ghost-texture / poly-3-2
BAS reese-sustain / drive / mono<120
SUB sine / duck-kick
PAD noise-bed / mid-width / pulse
SAW riff-1-16 / gated
NOI vinyl-crackle / light
ATM urban-space / wide
Library is DATA.
Extension via CHANGE CONTROL or validated INTAKE DATA injection only.

— END OF PART 3/6 —


SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
RHYTHM & GROOVE DESIGN ENGINE (RDE)
═══════════════════════════════════════════════════════════════════════
Purpose:
Typed rhythm behavior per voice slot per section.
Complements IDE: IDE = sources, RDE = patterns.
Input:
IR, Section Map, Arrangement density, IDE slot registry.
Output:
Groove Map (GRV-MAP), Groove Resolution Log, Groove Validation.
TYPED GROOVE OBJECT:
id, slot, pattern_class, grid, density, syncopation, swing,
accent_map, ghost_notes, fills, velocity_behavior, coupling,
section_overrides, priority, inheritance, projection, validation,
source_trace.
PATTERN CLASSES — BASE:
KCK: FOUR_ON_FLOOR, BREAKBEAT, INDUSTRIAL_STOMP, HALF_TIME,
DOUBLE_TIME, SYNCOPATED_TECH, AMEN_DERIVED.
SNR: BACKBEAT_2_4, CLAP_OFFBEAT, GATE_1_16, MILITARY_SNARE,
SPARSE_IMPACT, ROLL_FILL.
HAT: OFFBEAT_8TH, CLOSED_16TH, SHUFFLE_16TH, OPEN_ACCENT,
GRANULAR_BURST, TWO_STEP.
PRC: POLY_3_2, INDUSTRIAL_LOOP, GHOST_TEXTURE, TOM_GROOVE, NONE.
BAS: ROOT_8TH, ROLLING_16TH, REESE_SUSTAIN, ACID_303,
SYNCOPATED_FUNK, SUB_LONG.
PAD: SUSTAIN, PULSE_1_4, SWELL_PER_SECTION, ARP_1_8.
SAW: GATE_1_8, GATE_1_16, STAB_OFFBEAT, SUSTAIN_LEAD, RIFF_1_16.
PATTERN CLASSES — EXT-SLOT:
STR/CHR: SUSTAIN, TREMOLO, PULSE_1_4, STAB, OSTINATO,
SWELL_PER_SECTION.
BRS: STAB, SUSTAIN, HIT, RIFF_1_8.
WND: LINE, OSTINATO, SWELL.
PER: HIT, ROLL, TIMPANI_PATTERN, NONE.
KEY: ARPEGGIO, CHORD_1_4, OSTINATO, NONE.
COUPLING RULES:
If KCK = FOUR_ON_FLOOR → HAT default OFFBEAT_8TH unless override.
If KCK = INDUSTRIAL_STOMP → SNR ∈ {SPARSE_IMPACT, GATE_1_16}.
If GLOBAL contains NO_ZERO_ENERGY_BREAKDOWNS → fills/gaps must not
create silence > 1 beat.
If GLOBAL contains CONTINUOUS_ENERGY → fills/gaps ≤0.5 beat.
Swing/shuffle inherited from family; per-section override allowed.
If PER=NONE and slot unset → absence compiles to absence.
STYLE-CONDITIONED RESOLUTION:
Same order as TIMBRE LIBRARY.
Match path logged.
Fallback logs WARN.
═══════════════════════════════════════════════════════════════════════
GROOVE LIBRARY
═══════════════════════════════════════════════════════════════════════
FAMILY entry fields:
family_id, match_keys, slots, fallback_policy.
F-HARSH:
KCK INDUSTRIAL_STOMP / 4-4 / medium density / no swing
SNR SPARSE_IMPACT / 2&4 / alternate GATE_1_16
HAT GRANULAR_BURST / 8th closed / offbeat accent
PRC INDUSTRIAL_LOOP / poly-3-2 / low ghost
BAS ROOT_8TH / drive / mono
SUB SUB_LONG / duck-kick
PAD SUSTAIN / swell-per-section
SAW GATE_1_16 / riff / high density
fills: none exceeding 1 beat unless GLOBAL floor allows
F-TECH:
KCK FOUR_ON_FLOOR / 4-4 / tight
SNR CLAP_OFFBEAT / 2&4
HAT OFFBEAT_8TH / open accent
PRC INDUSTRIAL_LOOP / low density / ghost
BAS ROLLING_16TH
SUB SUB_LONG / duck-kick
PAD PULSE_1_4
SAW STAB_OFFBEAT
F-POP:
KCK FOUR_ON_FLOOR / soft
SNR BACKBEAT_2_4
HAT SHUFFLE_16TH / swing 12-16%
PRC GHOST_TEXTURE
BAS ROOT_8TH
SUB SUB_LONG
PAD SUSTAIN
SAW STAB_OFFBEAT
fills: 1 bar max at section boundary
F-AMB:
KCK NONE
SNR NONE
HAT NONE
PRC GHOST_TEXTURE / sparse
BAS SUB_LONG
SUB SUB_LONG / drone
PAD SUSTAIN / swell-per-section
SAW SUSTAIN_LEAD
F-BRK:
KCK AMEN_DERIVED / breakbeat / syncopated
SNR BACKBEAT_2_4 + ROLL_FILL
HAT SHUFFLE_16TH / MPC-swing / open accent
PRC POLY_3_2 / ghost
BAS REESE_SUSTAIN
SUB SUB_LONG / duck-kick
PAD PULSE_1_4
SAW RIFF_1_16
GROOVE_SUPPLEMENT may ADD_ENTRY family/pattern profiles.
Swing values must be numeric ranges, never adjectives.
═══════════════════════════════════════════════════════════════════════
HARMONY DESIGN ENGINE (HDE)
═══════════════════════════════════════════════════════════════════════
Input:
IR key/genre/energy, vocal register profile, arrangement tension
curve, LEAD map.
Output:
HRM-MAP, Key Plan, Harmony Validation.
HRM-MAP syntax:
SEC=KEY / MODE / PROGRESSION / VOICING / TENSION
Example:
[HRM-MAP: G=Am / aeolian / i-VI-III-VII / close / 0.4;
K=Am / aeolian / i-bVI-bVII / open / 0.9]
Dimensions:
key, mode, progression, voicing, tension, modulation,
cadence, dissonance, register relationship to vocal.
Rules:
Vocal register profile constrains lead/vocal key centre.
Violation → CONFLICT_RECORD P2.
Modulation must be declared in HRM-MAP and mirrored in TRN-MAP.
Undeclared modulation → BLOCK.
HARMONY_SUPPLEMENT may ADD_ENTRY progression/mode vocabularies.
It may not alter coupling rules.
═══════════════════════════════════════════════════════════════════════
LEAD DESIGN ENGINE (v3.4)
═══════════════════════════════════════════════════════════════════════
Input:
HRM-MAP, IDE source timbres, energy curve, hook policy.
Output:
LEAD-MAP, Lead Resolution Log, Lead Validation.
LEAD ROLES (typed registry):
HOOK           main melodic identity, carries the hook
COUNTER        answers hook/vocal, fills phrase gaps
ATMOSPHERIC    wide, slow, textural foreground
HIGH_MOTIF     high-register signature motif
ARP_LEAD       arpeggiated rhythmic lead
VOCAL_RESP     mirrors vocal contour in phrase gaps
BASS_LOCK      doubles or answers bass rhythm at higher register
SOURCE REGISTRY (v3.4):
SAW, PAD, BAS, SUB, registered EXT-SLOT.
When SOURCE ∈ {BAS, SUB}:
mono_compliance forced to mono <120Hz;
widen behaviors forbidden on that lead;
conflict with MIX width directive → CONFLICT_RECORD,
GLOBAL wins (INV-050).
TYPED LEAD OBJECT (per role):
id, role, source_slot, register, motif_shape,
evolution_path, harmonization, interaction_rules,
section_overrides, density, priority, inheritance,
projection, validation, source_trace.
EVOLUTION PATHS (registry, composable with →):
STATIC            no change across returns
MUTATE_TIMBRE     filter / drive / unison changes, same notes
MUTATE_RHYTHM     same notes, different rhythm
OCTAVE_LIFT       +1 octave on return
HARMONIZE         add 3rd / 5th / stack on return
COUNTERLINE       new countermelody woven in
INTERLOCK         interlock with another lead or vocal
VARIATION         slight melodic variation preserving identity
FUSION            multiple leads merge at climax
FINAL_FUSION      full-stack maximum elevation at terminal peak
INTERACTION RULES (coupling contract):
call_response_vocal     lead answers in vocal phrase gaps
call_response_bass      lead mirrors bass rhythm
never_mask_vocal        auto-duck under vocal (drives SC-MAP)
register_separation     keep ≥ 1 octave from vocal fundamental
harmonic_lock           follow HRM-MAP chord tones
monophonic_hook         HOOK monophonic unless HARMONIZE path set
LEAD-MAP syntax:
SEC=ROLE / SOURCE / MOTION / REGISTER / HOOK
Example:
[LEAD-MAP: S=RIFF / SAW / ↑ / mid / none;
K=HOOK / SAW+STR / ~→=→↑→† / mid-high / hook;
G=BASS_LOCK / BAS / = / low / riff]
Leads are functions over timbres, never free instrument names.
LEAD LIBRARY (DATA), family role/source defaults:
F-HARSH: HOOK=SAW industrial-siren / ~ ; COUNTER=SAW granular-stab.
F-TECH:  HOOK=BAS vowel-riff / ~+F ; COUNTER=SAW metallic-stab.
F-POP:   HOOK=SAW saw-soft / =→↑ ; COUNTER=SAW pluck-bright.
F-AMB:   HOOK=SAW saw-pad / = ; COUNTER=none-default.
F-BRK:   HOOK=SAW riff-1-16 / ~ ; COUNTER=SAW stab.
(F-TRN and other families enter via CHANGE CONTROL or validated
INTAKE DATA injection; LEAD LIBRARY entries valid once family
exists in TIMBRE LIBRARY.)
Library is DATA; extension via CHANGE CONTROL or INTAKE only.
═══════════════════════════════════════════════════════════════════════
PRESENCE DESIGN (v3.4)
═══════════════════════════════════════════════════════════════════════
Input:
Arrangement energy/density, vocal duty, archetype affinity.
Output:
WGT-MAP, presence_weights, vocal_duty, vocal_forward,
density_controls.
WGT-MAP syntax:
SEC=SLOT:weight[,SLOT:weight...];VOCAL:weight
Example:
[WGT-MAP: G=KCK:1.0,BAS:0.9,VOCAL:0.8;
K=KCK:1.0,SUB:1.0,SAW:0.9,VOCAL:0.6]
Rules:
weights in [0..1]
0 means absence, not silence-with-intent
vocal_duty = fraction of section carrying vocal units
vocal_forward raises vocal weight without changing timbre
GLOBAL vocal-interaction directives set scoped vocal_forward
AVATAR_SUPPLEMENT may set persona presence default only
USER presence instruction always wins
OVERDEVELOPMENT CONTROL (v3.4):
Density controls live here; values from GLOBAL tokens or defaults.
NO_OVERDEVELOPMENT (global token):
MAX_ACTIVE_LEADS=2; DENSITY_CEILING=0.75; MAX_ACTIVE_LAYERS=6.
Defaults without token:
MAX_ACTIVE_LEADS=3; DENSITY_CEILING=0.85; MAX_ACTIVE_LAYERS=6.
WGT-MAP per-section sum of non-percussion slot weights ≤
DENSITY_CEILING else CONFLICT_RECORD P2; lowest-priority layer
dropped, logged.
LEAD-MAP active roles per section ≤ MAX_ACTIVE_LEADS.
FID-MAP digital-pristine → DENSITY_CEILING=0.80 unless user override.
Violations logged via OVD-001 / OVD-002 gates (INV-055).
═══════════════════════════════════════════════════════════════════════
EFFECT DESIGN
═══════════════════════════════════════════════════════════════════════
Output:
FX-MAP.
FX-MAP syntax:
SEC=TARGET:CODES+BEHAVIOR
Example:
[FX-MAP: K=SAW:R+D›P; G=VOCAL:C+S; S=ATM:W↑;
P=SAW:Y(pan_L→R,1beat)]
Targets:
slot codes, VOCAL, MIX, ATM.
Codes:
CORE effect codes (R D F S W P B L G C Y) +
registered supplement symbols.
Rules:
FX-MAP vocal entries override archetype processing_chain and win,
single-source logged.
Unregistered code → VALIDATION ERROR.
Effect intent is semantic.
No plugin is asserted as instantiated.
Y (Fly-by) compiles to stereo pan/field motion automation
L→R or R→L over 1-2 beats; stereo NATIVE; binaural/HOA
BACKEND_DEPENDENT.
AI_FX_SUPPLEMENT effects enter here only at their assigned
capability level and are labeled in LEGEND.
═══════════════════════════════════════════════════════════════════════
SPECTRAL EFFECT DESIGN (v3.4)
═══════════════════════════════════════════════════════════════════════
Output:
SPC-MAP.
SPC-MAP syntax:
SEC=TARGET:SYMBOL(PARAMS-semantics)
Example:
[SPC-MAP: K=PAD:T(latent morph); R=ATM:Ψ(spectrum hold);
G=BAS:spectral-EQ(carve_masking)]
Domain:
spectral freeze, spectral blur, spectral gate, spectral compressor,
spectral delay, morphing classes, extreme time-stretch,
harmonic/percussive separation, spectral-EQ.
CORE symbol addition (v3.4):
spectral-EQ, domain=SPECTRAL_EFFECT, capability=SEMANTIC_ONLY.
Semantics: AI-driven frequency carving to reduce masking between
slots; not a parametric EQ claim.
Rules:
All symbols here must exist in SYMBOL REGISTRY with
domain=SPECTRAL_EFFECT.
Default capability for this domain is SEMANTIC_ONLY unless backend
confirms otherwise.
SPECULATIVE entries are blocked by default.
═══════════════════════════════════════════════════════════════════════
SPATIAL DESIGN (v3.4)
═══════════════════════════════════════════════════════════════════════
Output:
spatial node set, folded into FX/SPC maps and MIX-MAP width.
Dimensions:
width, depth, field motion, object placement,
binaural intent, immersive intent.
Rules:
HOA / WFS / Atmos / DTS:X / MPEG-H / 6DoF are BACKEND_DEPENDENT.
Compiled as width/depth/motion semantics unless backend confirmed.
Y (Fly-by) in FX-MAP implies spatial field motion; compiles to
pan/width automation; stereo NATIVE, binaural/HOA
BACKEND_DEPENDENT.
MIX-MAP WIDTH=pristine forces clean stereo imaging semantics
(no phase artifacts, mono-compatible width).
SPATIAL_SUPPLEMENT may extend vocabulary only.
═══════════════════════════════════════════════════════════════════════
AUTOMATION DESIGN
═══════════════════════════════════════════════════════════════════════
Output:
AUT-MAP.
AUT-MAP syntax:
SEC=TARGET:BEHAVIOR
Example:
[AUT-MAP: S=SAW:filter↑,width↑; K=SUB:duck; O=ALL:‹;
G=BAS:filter~,formant~,resonance↑]
Behaviors use DSE markers:
↑ ↓ ~ → › ‹
Rules:
Automation never contradicts GLOBAL hard constraint.
Conflict → CONFLICT_RECORD.
GLOBAL wins, logged.
═══════════════════════════════════════════════════════════════════════
FIDELITY ENGINE (NEW in v3.4)
═══════════════════════════════════════════════════════════════════════
Purpose:
Typed "recording medium" character layered on top of MIX/MASTER.
Separates "how balanced" (MIX) from "how it sounds as a recording"
(FID).
Input:
IR (genre, subgenre, era, mood), MIX-MAP, MAST-MAP.
Output:
Fidelity Map (FID-MAP), Fidelity Resolution Log.
FIDELITY DIMENSIONS (closed registries):
medium_class:
digital-pristine | analog-tape | vinyl | lo-fi | broadcast |
cassette | live-room | stem-clean
noise_floor:
silent | low-hiss | tape-hiss | vinyl-crackle | room-noise |
digital-hash
bandwidth:
full-20k | limited-15k | telephone | lo-fi-10k
transient_char:
clean | soft-rounded | hard-clipped | saturated
stereo_mode:
mono-compat | wide-stereo | mid-side | binaural | summed-mono
dynamic_range:
modern-loud | dynamic | crushed | broadcast
warmth:
cold-digital | neutral | warm-analog | hot-tape
artifact_budget:
none | light | intentional | dominant
FID-MAP syntax:
[FID-MAP: DIM=value; ...]
Optional section overrides: FID@SEC keys ⊆ ARC.
Coupling rules (deterministic, logged):
lo-fi           → MIX high-cut ≤12k unless user override
analog-tape     → MAST soft-saturation ON
mono-compat     → MIX sub mono enforced
modern-loud     → MAST LUFS target per backend limits
pristine        → artifact_budget forced none
USER MIX/MAST values always win (OVR-USER, INV-058).
FIDELITY LIBRARY (DATA):
F-HARSH:
broadcast / digital-hash / full-20k / hard-clipped /
wide-stereo / modern-loud / cold-digital / intentional
F-TECH:
digital-pristine / silent / full-20k / clean / wide-stereo /
modern-loud / neutral / light
F-POP:
digital-pristine / silent / full-20k / clean / wide-stereo /
modern-loud / neutral / none
F-AMB:
digital-pristine / silent / full-20k / clean / wide-stereo /
dynamic / neutral / none
F-BRK:
analog-tape / tape-hiss / full-20k / saturated / wide-stereo /
dynamic / warm-analog / light
BASE fallback: digital-pristine (WARN on fallback).
Gates: FID-001 dimension membership; FID-002 coupling vs user
MIX/MAST (user wins, logged); FID-003 FID@SEC keys ⊆ ARC.
Library is DATA; extension via CHANGE CONTROL or INTAKE only.

— END OF PART 4/6 —


SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
ARRANGEMENT DESIGN
═══════════════════════════════════════════════════════════════════════
Output:
ARC, STRUCTURE nodes, section energy/density curve.
ARC syntax:
ordered DSE section codes with optional repeat counts.
Example:
[ARC: I G S K R K F O]
Rules:
ARC is the single source of section order.
Zone B markers must match it exactly.
ARRANGEMENT_SUPPLEMENT may supply structural templates as DATA:
intro, outro, verse, pre-chorus, chorus, bridge, breakdown,
build-up, drop, fake-drop, anti-drop, re-drop, double-drop,
takedown, jump-up, work-up, riser, downlifter, impact, sub-drop,
snare-roll, hat-roll, fill, two-step, half-time, double-time,
triplets, swing, shuffle, syncopation, polyrhythm, polymeter,
cross-rhythm, hocket, layering, call-and-response, contrast,
dynamics, automation, modulation, key change, tempo change,
vocal chop, stutter, glitch, break, interlude, coda, tag, solo,
vamp, riff, leitmotif, counter-melody, topline, hook.
These compile into ARC, STRUCTURE, TRN-MAP, GROOVE, VOCAL, FX,
or CONTROL GRAPH as appropriate.
They never become free lyric text.
═══════════════════════════════════════════════════════════════════════
DURATION DESIGN (v3.4)
═══════════════════════════════════════════════════════════════════════
Output:
DUR-PLAN, duration_plan, extend_plan.
DUR-PLAN syntax:
TOTAL=mm:ss; SEC=sec[,SEC=sec...]
Occurrence semantics (per DSE v2.6):
A bare section key addresses ALL occurrences of that code in ARC
(scope=ALL) and represents the SUM of durations across occurrences.
Per-occurrence addressing: SEC#n splits the sum.
Unknown #n → SYNC fail.
Rules:
Sum of section durations must equal TOTAL within ±1s.
Otherwise BLOCK.
Tempo/meter change must be declared here and mirrored in TRN-MAP.
═══════════════════════════════════════════════════════════════════════
TRANSITION DESIGN (v3.4)
═══════════════════════════════════════════════════════════════════════
Output:
TRN-MAP.
TRN-MAP syntax:
SEC>SEC:CODE+BEHAVIOR
Example:
[TRN-MAP: S>K:RISER+IMPACT; K>R:TAPE-STOP; R>K:FILTER-SWEEP↑]
CORE transition vocabulary:
RISER, DOWNLIFTER, IMPACT, TAPE-STOP, FILTER-SWEEP, XFADE,
SNARE-ROLL, HAT-ROLL, SUB-DROP, BREAK.
Supplement transition vocabulary (pre-registered CORE, v3.4):
FAKE-DROP, ANTI-DROP, RE-DROP, DOUBLE-DROP, ECHO-OUT, BACKSPIN,
SPINBACK, PULL-UP, WHEEL-UP, RELOAD, TEASE, BLEND, DROP-MIX,
HARMONIC-MIX, KEY-MIX, TEMPO-TRANSITION, ISOLATOR-SWEEP,
SCRATCH-TRANSITION, BREAKDOWN-RETURN, TAPE-START.
DJ_SUPPLEMENT vocabulary:
beatmatching, phrasing, EQ-mix, crossfade, channel-fader, cueing,
hot-cue, loops, roll, slip-mode, scratch, baby-scratch, chirp,
flare, transformer, crab, tear, orbit, beat-juggling, mashup,
bootleg, re-edit, extended-edit, dubplate, acapella, instrumental,
reload, pull-up, wheel-up, double-drop, tease, blend, drop-mix,
harmonic mix, key-mix, tempo transition, echo-out, filter-sweep,
backspin, spinback, break, tape-stop, isolator.
Rules:
Every modulation, tempo change, and structural surprise declared in
HDE/DUR-PLAN must have a TRN-MAP event. Orphan → BLOCK.
DJ_SUPPLEMENT entries compile into TRN-MAP, FX-MAP, and MIX-MAP only.
TRN events auto-inject corresponding SFX objects at boundary
positions unless SFX-MAP overrides (logged).
═══════════════════════════════════════════════════════════════════════
SFX DESIGN (NEW in v3.4)
═══════════════════════════════════════════════════════════════════════
Purpose:
Separate musical FX (FX-MAP) from sound effects / impacts /
transitions (SFX-MAP).
Output:
SFX-MAP.
SFX-MAP syntax:
SEC=TARGET:CODES+BEHAVIOR
Targets:
TRANSITION, ATMOSPHERE, STING.
CORE SFX vocabulary:
IMPACT, RISER, DOWNLIFTER, SUB-DROP, TAPE-STOP, REVERSE-SUCK,
NOISE-SWEEP, FILTER-SWEEP, METALLIC-HIT.
Supplement SFX vocabulary (registered via SYMBOL_SUPPLEMENT /
SOUND_DESIGN_SUPPLEMENT):
GLASS-BREAK, AIR-HORN, SIREN, VINYL-STOP, LASER-BURST,
CROWD-CHEER, FOLEY-HIT.
Rules:
SFX never mask VOCAL or LEAD: auto-duck applied and logged.
SFX density ≤ 2 per section unless GLOBAL allows more.
Symbols must exist in SYMBOL REGISTRY domain=SFX (INV-057).
FID pristine → artifact_budget none for SFX (clean impacts only).
Gates: SFX-001 symbol domain membership; SFX-002 masking duck
logged; SFX-003 density ≤ cap.
═══════════════════════════════════════════════════════════════════════
AUTO-INJECT: SC / MIX / MASTER (v3.4)
═══════════════════════════════════════════════════════════════════════
Injected by default unless user disables. Disable logged WARN.
SC-MAP syntax:
SEC=TARGET<-TRIGGER:DEPTH
MIX-MAP syntax:
SEC=EQ/CMP/STEREO/LEVEL tokens
MAST-MAP syntax:
LUFS=..; TP=..; LIMIT=..; FADE=..
v3.4 MIX-MAP token additions:
NO_HIGH_CUT | HIGH_CUT=none
(forbids LPF above 15kHz on any slot)
WIDTH=pristine
(clean stereo imaging, no phase artifacts, mono-compatible width)
v3.4 MAST-MAP token addition:
PRISTINE
Expansion: LUFS=backend_default; TP=-1.0dB; LIMIT=clean;
FADE=none; NO_SATURATION; NO_TAPE_EMULATION; NO_LO-FI_ARTIFACTS.
Coupling: PRISTINE → FID digital-pristine (if FID unset),
MIX NO_HIGH_CUT, WIDTH=pristine, artifact_budget none.
USER values win (OVR-USER, INV-058).
Defaults (carried):
SC: KCK triggers BAS/SUB duck on high-energy sections.
MIX: mono-compliance on KCK/SUB below 120Hz; width on PAD/ATM/
NOI/STR/CHR where stylistically valid; vocal clarity protected;
masking reduction via semantic carving/ducking only.
MAST: loudness target and true-peak cap per backend limits;
‹ on O implies FADE unless overridden.
MIX_MASTER_SUPPLEMENT may refine defaults as DATA.
Mix/master supplement vocabulary:
gain-staging, subtractive EQ, additive EQ, shelf, peak, high-pass,
low-pass, band-pass, notch, compression, parallel compression,
serial compression, multiband compression, sidechain compression,
limiting, clipping, soft-clip, hard-clip, saturation, harmonic
excitation, transient shaping, gating, expansion, de-ess, de-pop,
de-click, noise reduction, restoration, stereo imaging, M/S,
mono compatibility, phase alignment, phase cancellation, frequency
masking, carving, ducking, automation, bus processing, stem
mastering, LUFS, true peak, dither, noise shaping, normalization,
fades, crossfades.
═══════════════════════════════════════════════════════════════════════
TRANSLATION ENGINE (v3.4)
═══════════════════════════════════════════════════════════════════════
Purpose:
Deterministic projection of IR/control nodes into textual tokens
for STYLE and LYRICS.
Projection order:
family + genre/subgenre + tempo + energy
timbre family summary
groove summary
vocal: speakers, archetypes, technique layer
lead/harmony summary
effect/spectral summary
fidelity summary (medium/noise/bandwidth/transient)
SFX summary
negative controls
production/mix/master summary
Rules:
No projection may introduce semantics absent from IR.
Every projected token retains internal trace to its node.
Supplement-origin tokens are marked origin=SUPPLEMENT internally
and attributed in LEGEND when surfaced as codes.
═══════════════════════════════════════════════════════════════════════
STYLE COMPILER
═══════════════════════════════════════════════════════════════════════
Input:
translated projection, Zone A maps.
Output:
STYLE FIELD.
Rules:
Hard ceiling 800 chars including spaces and punctuation.
Compression order by budget class.
Zone A directive block is emitted inside STYLE.
Never compress away:
GLOBAL hard constraints,
NEGATIVE controls,
P1 user-explicit items,
P2 decode contract.
Compression is logged item-by-item.
Silent truncation forbidden.
═══════════════════════════════════════════════════════════════════════
LYRICS COMPILER
═══════════════════════════════════════════════════════════════════════
Input:
translated projection, section plan, vocal units, ARC.
Output:
LYRICS FIELD.
Rules:
Hard ceiling 4000 chars including spaces and punctuation.
Zone B contains section markers + vocal text only.
Technical directives forbidden in Zone B.
Section markers exempt.
Vocal unit boundaries follow VOCAL TERMINATION.
Language locked to IR language unless section-scoped override
declared and logged.
═══════════════════════════════════════════════════════════════════════
STYLE ↔ LYRICS SYNC (v3.4)
═══════════════════════════════════════════════════════════════════════
Checked by Sync Validator:
ARC order == Zone B marker order
section keys parity across all maps
WGT/INST/GRV/HRM/LEAD/FX/SPC/SFX/AUT/FID/TRN/SC/MIX/MAST parity
SYNC_VALID covers maps ↔ LEGEND
SPEAKERS sections subset of ARC sections
DUR-PLAN sections == ARC sections
VOC/FID/SFX map key parity
occurrence-tag resolution parity (SEC#n maps to ARC positions)
Any mismatch → SYNC_VALIDATED fail → BLOCKED.
═══════════════════════════════════════════════════════════════════════
BUDGET ENFORCEMENT — PASS 1 AND PASS 2
═══════════════════════════════════════════════════════════════════════
PASS 1:
Before LEGEND.
Compress STYLE projection to fit ceiling with headroom reserved
for LEGEND.
PASS 2:
After LEGEND.
Re-verify both ceilings.
If exceeded, compress P4 then P3, never P1/P2.
Budget classes:
P1
USER explicit + GLOBAL hard + NEGATIVE.
Never compressed.
P2
Decode contract: maps semantics, LEGEND, symbol source tags,
sync-critical tokens.
Never compressed.
P3
Family defaults, stylistic summary.
Compressed first.
P4
Optional: LEGEND SLOT group, decorative atmosphere detail,
EXT-SLOT legend.
Dropped first.
Every drop/compress action logged with item id and reason.
Silent truncation forbidden.
═══════════════════════════════════════════════════════════════════════
VALIDATION (v3.4)
═══════════════════════════════════════════════════════════════════════
Gate families:
IR-xxx      IR completeness, type correctness, no orphan node
CG-xxx      control graph resolution, inheritance, priority
SYN-xxx     style/lyrics/map/legend parity
BUD-xxx     ceiling compliance both passes
OUT-xxx     formatter correctness, no stray brackets, zone purity
INT-xxx     intake gates
SYM-xxx     symbol gates
OVD-xxx     overdevelopment gates (v3.4)
CEN-xxx     continuous energy gates (v3.4)
FID-xxx     fidelity gates (v3.4)
VOC-xxx     vocal technique gates (v3.4)
SFX-xxx     sound effect gates (v3.4)
INTAKE GATES:
INT-001 every supplement has resolved type from closed set
INT-002 every entry carries all mandatory fields
INT-003 every entry carries capability_level
INT-004 SPECULATIVE blocked unless CAP=ALLOW_SPEC
INT-005 BACKEND_DEPENDENT compiled as intent or BLOCK on mandatory
INT-006 every applied entry has injection instruction
INT-007 every injection targets registered module
INT-008 every applied entry has source_trace
INT-009 no injection overrides USER/GLOBAL silently
INT-010 INTAKE REPORT counters match applied/blocked/unresolved
SYMBOL GATES:
SYM-001 every code in use exists in GLOBAL SYMBOL TABLE
SYM-002 no unresolved symbol reaches a map
SYM-003 no silent same-domain collision
SYM-004 SPECULATIVE symbols require explicit opt-in
SYM-005 LEGEND covers all non-CORE symbols actually used
SYM-006 CORE symbol meaning never redefined by supplement
OVERDEVELOPMENT GATES (v3.4):
OVD-001 density sum ≤ ceiling
OVD-002 active leads ≤ cap
CONTINUOUS ENERGY GATES (v3.4):
CEN-001 rhythm presence floor per section
CEN-002 gap ≤ fill floor
FIDELITY GATES (v3.4):
FID-001 dimension registry membership
FID-002 coupling vs user MIX/MAST → user wins logged
FID-003 FID@SEC keys ⊆ ARC
VOCAL TECHNIQUE GATES (v3.4):
VOC-001 keys ⊆ vocal-carrying sections else WARN-NOVOC
VOC-002 values ∈ VPM vocabulary + capability defaults
SFX GATES (v3.4):
SFX-001 symbol domain membership
SFX-002 masking duck logged
SFX-003 density ≤ cap
Any gate fail → CURRENT_STATE → BLOCKED.

— END OF PART 5/6 —


SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════
OUTPUT FORMATTER (v3.4)
═══════════════════════════════════════════════════════════════════════
ZONE A — STYLE FIELD:
[GLOBAL]
[ARC]
[DUR-PLAN]
[WGT-MAP]
[SPEAKERS]
[VOC-MAP]
[INST-MAP]
[GRV-MAP]
[HRM-MAP]
[LEAD-MAP]
[FX-MAP]
[SPC-MAP]
[SFX-MAP]
[AUT-MAP]
[FID-MAP]
[TRN-MAP]
[SC-MAP]
[MIX-MAP]
[MAST-MAP]
[LEGEND]
ZONE B — LYRICS FIELD:
section markers + vocal text only.
ORDER:
Fixed as listed.
Deviation only by explicit user order, logged.
Forbidden:
directive text in Zone B
lyric text in Zone A
unregistered directive
bare unresolved letter
empty map
Reports:
INTAKE REPORT and VALIDATION REPORT are compiler-side artifacts.
They may be shown to user outside Suno fields.
They are not injected into STYLE or LYRICS unless debug mode is
explicitly requested.
═══════════════════════════════════════════════════════════════════════
FINAL OUTPUT VALIDATION → RELEASE
═══════════════════════════════════════════════════════════════════════
Re-check formatted artifact:
ceilings
zone purity
legend parity
marker parity
directive registry membership
no bare codes
no invented capability claims
intake counters consistent
occurrence-tag resolution
density/energy floors
fidelity coupling consistency
SFX masking duck logged
Pass → RELEASED.
Fail → BLOCKED with itemized failure report.
RELEASE is the only terminal success state.
═══════════════════════════════════════════════════════════════════════
CONFLICT RESOLUTION & OVERRIDE LOGGING (v3.4)
═══════════════════════════════════════════════════════════════════════
Scope order:
USER MAIN PROMPT
GLOBAL HARD
PROJECT IR
SUPPLEMENT EXPLICIT
FAMILY DEFAULT
BASE
Log tokens:
OVR-USER
OVR-GLOBAL
OVR-SUP
OVR-LEGEND
OVR-FX
OVR-SECTION-MAP
OVR-FID
OVR-SFX
OVR-DENSITY
WARN-NOVOC
CONFLICT_RECORD
WARN-FALLBACK
WARN-NOARCH
BLOCK-CAP
BLOCK-SYM
BLOCK-INT
Every override emitted with:
item, winner, loser, reason, scope.
Silent resolution is impossible by construction.
═══════════════════════════════════════════════════════════════════════
BACKEND LIMITS / CAPABILITY MATRIX (v3.4)
═══════════════════════════════════════════════════════════════════════
HARD LIMITS:
STYLE ≤ 800 chars
LYRICS ≤ 4000 chars
No real plugin/VST/AU instantiation.
No stem export.
No project file.
No visual output.
No guaranteed DSP parameter values.
NATIVE:
reverb, delay, filter, saturation, widen, pump, sub, gate, comp,
sidechain, EQ-ish shaping, stereo width, fades, section structure,
vocal class/archetype, harmony/key, tempo, meter, language,
stereo pan/field motion (fly-by), impacts/risers as FX intent.
SEMANTIC_ONLY:
scream, growl, falsetto as timbre claim, vocal chop, stutter,
glitch, granular texture, tape-stop, spectral freeze, spectral blur,
spectral gate, spectral morphing, cepstral morphing, wavelet
morphing, phase vocoder extreme stretch, data bending, glitch art,
chaos synthesis, fractal audio, nonlinear dynamics, modal synthesis,
Karplus-Strong, waveguide, material morphing, spectral-EQ,
SFX object placement precision.
BACKEND_DEPENDENT:
voice conversion/RVC, neural style transfer, timbre transfer,
DDSP, neural synthesis, neural reverb/amp modeling,
source separation as FX, AI mastering/mixing, diffusion audio,
text-to-audio, audio inpainting/outpainting, neural vocoder,
embedding arithmetic, HOA, wave field synthesis, HRTF
personalization, binaural rendering, Dolby Atmos, DTS:X, MPEG-H,
6DoF audio, object-based audio, beamforming, sonic holography,
ambisonic morphing, tensor decomposition, tensor train,
higher-order SVD, multilinear PCA, tensor completion,
tensor factorization for source separation.
SPECULATIVE:
quantum Fourier transform, quantum audio processing,
quantum synthesis, quantum reverb/delay, superposition audio,
entanglement audio, qubit modulation, quantum morphing,
quantum tensor networks, brain-computer interface audio.
UNSUPPORTED:
visual avatar, video, artwork, stem separation output,
exact plugin chain reproduction.
Capability rule:
An entry's level is set at CAPABILITY_GATE and is monotone downward
only. Supplements may downgrade, never upgrade.
═══════════════════════════════════════════════════════════════════════
INVARIANTS (v3.4)
═══════════════════════════════════════════════════════════════════════
INV-001 no silent drop, override, or truncation; every action logged.
INV-002 no invented capabilities; capability matrix authoritative.
INV-003 silent remap of DSE/ARRANGEMENT forbidden; overrides explicit.
INV-019 fresh-build mandatory on supplied spec artifact.
INV-021 non-marker technical directives forbidden in Zone B; section
markers exempt.
INV-026 style-conditioned fallback must log WARN; no silent fallback.
INV-029 vocal register profile is source of vocal-key coupling.
INV-033 LEGEND parity with used-code set; scope-tag overloaded
letters; covered by SYNC_VALID.
INV-034 archetype resolution fallback logs WARN.
INV-035 FX-MAP vocal entries override archetype processing_chain,
single-source, logged.
INV-036 supplements are DATA; they may not add directives, node
types, pipeline stages, or invariants.
INV-037 no letter travels without resolved SYMBOL; unregistered code
in any map is validation error.
INV-038 SPECULATIVE never applied as real capability; requires
explicit opt-in and remains labeled semantic only.
INV-039 no supplement may silently override USER or GLOBAL.
INV-040 every applied supplement entry carries source_trace.
INV-041 LEGEND must cover every non-CORE symbol actually used, with
source and capability tag.
INV-042 EXT-SLOT usage requires prior registration with typed
profile; unregistered slot → BLOCK.
INV-043 unknown or malformed directive → validation error; retired
directives recognized, ignored, logged WARN.
INV-044 capability level monotone downward; supplements may downgrade,
never upgrade.
INV-045 equal-priority conflict → CONFLICT_RECORD then BLOCK unless
user resolves explicitly.
INV-046 projection may not introduce semantics absent from IR.
INV-047 zone purity: no directives in Zone B, no lyric text in Zone A.
INV-048 ARC is single source of section order.
INV-049 INTAKE REPORT counters must match actual applied/blocked/
unresolved counts; mismatch → BLOCK.
INV-050 LEAD SOURCE ∈ registry; BAS/SUB leads mono-locked <120Hz,
widen forbidden on them.
INV-051 occurrence tags resolve to ARC positions else SYNC fail.
INV-052 free E*/L* codes forbidden in maps.
INV-053 FID values ∈ closed registries; unknown → validation error.
INV-054 VOC-MAP capability monotone downward; no timbre guarantees.
INV-055 NO_OVERDEVELOPMENT caps enforced; violation →
CONFLICT_RECORD, lowest-priority layer dropped, logged.
INV-056 CONTINUOUS_ENERGY floors enforced; BLOCK unless explicit
per-section USER override.
INV-057 SFX symbols domain=SFX; masking duck mandatory and logged.
INV-058 PRISTINE expansion deterministic; USER MIX/MAST win.
═══════════════════════════════════════════════════════════════════════
CHANGE CONTROL (v3.4)
═══════════════════════════════════════════════════════════════════════
Data extensions allowed at runtime via INTAKE:
TIMBRE LIBRARY
GROOVE LIBRARY
VOCAL ARCHETYPE LIBRARY
STYLE LEXICON
SLOT REGISTRY
SYMBOL REGISTRY
technique vocabularies
negative vocabularies
FIDELITY LIBRARY
LEAD LIBRARY
SFX vocabulary
Core extensions require skill version bump, never runtime:
directives
node types
pipeline stages
state machine
invariants
budget classes
capability matrix
DSE CORE codes
Rule:
If a supplement needs a new directive, it does not get one.
It is re-expressed through existing targets or BLOCKED with reason.
═══════════════════════════════════════════════════════════════════════
SUPPLEMENT SEED ROUTING (v3.4)
═══════════════════════════════════════════════════════════════════════
CLASS A — TECHNIQUE / ARRANGEMENT COMPENDIA
Section: Arrangement & dramaturgy
→ ARRANGEMENT_SUPPLEMENT
Targets: ARC, STRUCTURE, TRANSITION, DURATION, CONTROL GRAPH.
Section: Sound design & synthesis
→ SOUND_DESIGN_SUPPLEMENT
Targets: IDE, TIMBRE LIB, FX-MAP, SPC-MAP, SFX CONTROL.
Section: Rhythm & groove
→ GROOVE_SUPPLEMENT
Targets: RDE, GRV-MAP.
Section: Vocal
→ VOCAL_SUPPLEMENT
Targets: VOCAL PERFORMANCE MODEL, ARCHETYPE LIB, SPEAKERS, FX-MAP.
Section: DJ techniques
→ DJ_SUPPLEMENT
Targets: TRN-MAP, FX-MAP, MIX-MAP.
Section: Mixing & mastering
→ MIX_MASTER_SUPPLEMENT
Targets: MIX-MAP, MAST-MAP, SC-MAP, FIDELITY ENGINE.
Section: Harmony & melody
→ HARMONY_SUPPLEMENT
Targets: HDE, LEAD, HRM-MAP.
Section: Genre/style techniques
→ STYLE_SUPPLEMENT
Targets: STYLE LEXICON, family match_keys.
CLASS B — AI / TENSOR / SPECTRAL EFFECT MATRICES
Tabular rows:
Category | Effect / Method | What it does | Where to apply
Routing:
Neural/AI → AI_FX_SUPPLEMENT
Tensor/multidimensional → AI_FX_SUPPLEMENT
Spectral extremes → SOUND_DESIGN_SUPPLEMENT / SPECTRAL
Physical modeling → SOUND_DESIGN_SUPPLEMENT
Immersive/space → SPATIAL_SUPPLEMENT
Granular/microsound → SOUND_DESIGN_SUPPLEMENT
Generative/algorithmic → GENERATIVE_SUPPLEMENT
Quantum/post-digital → AI_FX_SUPPLEMENT, default SPECULATIVE
Bio/neuro/interface → AI_FX_SUPPLEMENT, default SPECULATIVE for BCI
Extreme DSP → SOUND_DESIGN_SUPPLEMENT
Capability assignment:
Neural morphing/style transfer/timbre transfer/voice conversion/
neural synthesis/neural vocoder/source separation/AI mastering/
diffusion/text-to-audio/inpainting/outpainting/embedding arithmetic
→ BACKEND_DEPENDENT or SEMANTIC_ONLY depending on target backend.
Tensor decomposition/tensor train/higher-order SVD/multilinear PCA/
tensor completion/tensor factorization
→ BACKEND_DEPENDENT as process, SEMANTIC_ONLY as prompt intent.
Spectral freeze/blur/gate/delay/compressor/morphing/phase vocoder/
spectral-EQ → SEMANTIC_ONLY.
Physical modeling/material morphing
→ SEMANTIC_ONLY for Suno target.
HOA/WFS/HRTF/binaural/Atmos/DTS:X/MPEG-H/6DoF/object audio/
beamforming/sonic holography/ambisonic morphing
→ BACKEND_DEPENDENT.
Granular/particle/concatenative/microsound/stochastic/Gendy/FOF/
musique concrète/extreme time-stretch
→ SEMANTIC_ONLY.
Markov/cellular automata/L-systems/genetic/swarm/GAN/VAE/diffusion/
transformer/reinforcement mixing/neural cellular automata/generative
infilling
→ GENERATIVE_SUPPLEMENT, BACKEND_DEPENDENT or SEMANTIC_ONLY.
Quantum rows and BCI rows
→ SPECULATIVE, BLOCK by default unless CAP=ALLOW_SPEC.
Data bending/circuit bending/datamoshing/glitch art
→ SEMANTIC_ONLY.
Chaos/strange attractors/fractal/feedback/nonlinear/extreme IIR
→ SEMANTIC_ONLY.
═══════════════════════════════════════════════════════════════════════
RETIRED DIRECTIVE REGISTRY (v3.4)
═══════════════════════════════════════════════════════════════════════
Retired directives are recognized, ignored, and logged WARN.
Migration pointers emitted.
Legacy generic blocks:
[FX] → migrate to [FX-MAP]
[SPECTRAL] → migrate to [SPC-MAP]
[SC] → migrate to [SC-MAP]
[MIX] → migrate to [MIX-MAP]
[MASTER] → migrate to [MAST-MAP]
v3.4 additions:
[VOCAL-MAP] → [SPEAKERS] + [VOC-MAP] + [FX-MAP:VOCAL]
[DYNAMICS-MAP] → [WGT-MAP] + ARC markers
[BASS-RIFF-MAP] → [LEAD-MAP SOURCE=BAS] + BAS@SEC in INST/GRV
[FX-ON-BASS] → [AUT-MAP: SEC=BAS] + [FX-MAP: SEC=BAS]
[GROOVE-MAP] → [GRV-MAP]
[CONTINUITY-LOCK] → [GLOBAL] hard constraints
No retired directive may influence final output unless explicitly
re-expressed through current directive syntax.
═══════════════════════════════════════════════════════════════════════
WORKED EXAMPLE — CONDENSED (v3.4)
═══════════════════════════════════════════════════════════════════════
INPUT:
Harsh industrial rave, 145 BPM, male ragga flow, female noise wail
on chorus, no silence, no zero-energy breakdowns, pristine mastering.
[SUPPLEMENT: VOCAL; MODE=STRICT]
Techniques: scream, growl, falsetto, vocal chop, doubling, ad-libs.
[SUPPLEMENT: AI_FX; MODE=STRICT]
Tensor morphing on PAD in drop.
Spectral freeze on ATM in bridge.
[SYM: Ψ=Spectral freeze, domain=SPECTRAL_EFFECT,
variants=[drone lock, spectrum hold]]
INTAKE:
[INTAKE] SUPPLEMENTS=3 ENTRIES=9 APPLIED=8 BLOCKED=1 UNRESOLVED=0
[INTAKE] INJ-001: VOCAL PERFORMANCE MODEL <- VOCAL/scream [SEM]
[INTAKE] INJ-002: VOCAL PERFORMANCE MODEL <- VOCAL/growl [SEM]
[INTAKE] INJ-003: VOCAL PERFORMANCE MODEL <- VOCAL/falsetto [NAT]
[INTAKE] INJ-004: FX-MAP <- VOCAL/vocal-chop [SEM]
[INTAKE] INJ-005: SPC-MAP <- AI_FX/tensor-morphing [SEM]
[INTAKE] INJ-006: SPC-MAP <- SYM/Ψ spectral-freeze [SEM]
[INTAKE] INJ-007: VOCAL PERFORMANCE MODEL <- VOCAL/doubling [NAT]
[INTAKE] INJ-008: VOCAL PERFORMANCE MODEL <- VOCAL/ad-libs [NAT]
[INTAKE] BLOCKED: quantum-reverb (SPECULATIVE, no ALLOW_SPEC)
[INTAKE] CAP: NATIVE=3 SEMANTIC=5 BACKEND=0 SPEC-BLOCKED=1
RESOLUTION:
family F-HARSH
KCK INDUSTRIAL_STOMP
SNR SPARSE_IMPACT
SPEAKERS G=MALE:RAGGA_TOASTER
K=FEMALE:NOISE_WRAIL + GROUP:CHOIR_STACK
GLOBAL NO_SILENCE honored by fill density floor.
NO_OVERDEVELOPMENT enforced (MAX_ACTIVE_LEADS=2, DENSITY_CEILING=0.75).
CONTINUOUS_ENERGY enforced (KCK/BAS ≥0.6 all sections).
FID-MAP digital-pristine (PRISTINE coupling).
SFX-MAP S>K=TRANSITION:RISER+IMPACT (auto-duck logged).
PROJECTION CONDENSED:
[GLOBAL: HARSH INDUSTRIAL RAVE, POWER ELECTRONICS, 145 BPM,
RELENTLESS KICK, MUTATING BASS, MALE RAGGA FLOW, FEMALE NOISE
WRAIL, SHARP CALL-AND-RESPONSE, NO SILENCE,
NO ZERO-ENERGY BREAKDOWNS, NO_OVERDEVELOPMENT, CONTINUOUS_ENERGY.]
[ARC: I G S K R K F O]
[VOC-MAP: G=chest/-/ragga-flow/chant; K=chest/-/wail/hook+stacking]
[FX-MAP: K=SAW:R+D›P+Y(pan_L→R,1beat); G=VOCAL:C+S]
[SPC-MAP: K=PAD:T(latent morph); R=ATM:Ψ(spectrum hold)]
[SFX-MAP: S>K=TRANSITION:RISER+IMPACT; K>F=TRANSITION:SUB-DROP]
[FID-MAP: medium_class=digital-pristine; noise_floor=silent;
bandwidth=full-20k; transient_char=clean; stereo_mode=wide-stereo;
dynamic_range=modern-loud; warmth=neutral; artifact_budget=none]
[MIX-MAP: NO_HIGH_CUT; WIDTH=pristine]
[MAST-MAP: PRISTINE; LUFS=-8; TP=-1.0dB]
[LEGEND: SEC | MRK | FX | SFX | NOTE
FX: R=Reverb D=Delay C=Comp S=Saturation P=Pump Y=Fly-by
SFX: RISER=rising sweep; IMPACT=impact sound; SUB-DROP=sub-bass impact
NOTE: T=Tensor morphing [SUP:AI_FX] [SEM] scope=SPECTRAL target=PAD
Ψ=Spectral freeze [USER] [SEM] scope=SPECTRAL target=ATM]
VALIDATION:
IR OK
CG OK
SYN OK
BUD OK
INT OK
SYM OK
OVD OK (density sum ≤ 0.75; active leads ≤ 2)
CEN OK (KCK/BAS ≥ 0.6 all sections)
FID OK (dimension membership; coupling logged)
VOC OK (keys ⊆ vocal sections; values ∈ VPM)
SFX OK (domain membership; duck logged; density ≤ 2)
OUT OK
→ RELEASED
═══════════════════════════════════════════════════════════════════════
CHANGELOG 3.3 → 3.4
═══════════════════════════════════════════════════════════════════════
ADDED:
Directives [LEAD-MAP] (registered), [VOC-MAP], [FID-MAP], [SFX-MAP].
VOCAL TECHNIQUE MAP.
FIDELITY ENGINE + FIDELITY LIBRARY.
SFX DESIGN.
OVERDEVELOPMENT CONTROL (NO_OVERDEVELOPMENT token + gates).
CONTINUOUS_ENERGY control (token + gates).
Effect code Y=Fly-by.
Spectral-EQ core symbol.
MAST PRISTINE token.
MIX NO_HIGH_CUT / WIDTH=pristine tokens.
Occurrence semantics (SEC#n per-occurrence addressing).
LEAD SOURCE registry +BAS/+SUB with mono-compliance rule.
LEAD LIBRARY (DATA).
Pre-registered TRANSITION supplement vocabulary as CORE symbols.
Pipeline stages FIDELITY DESIGN, SFX DESIGN.
States FIDELITY_DESIGNED, SFX_DESIGNED.
Invariants INV-050..INV-058.
Gates OVD-001/002, CEN-001/002, FID-001/002/003, VOC-001/002,
SFX-001/002/003.
LEGEND SFX group.
RETIRED REGISTRY additions with migration pointers.
CHANGED:
DSE v2.5 → v2.6 (scope enumeration + occurrence clause + free-code ban).
SCOPE RESOLUTION full enumeration of SEC-keyed directives.
Zone A order (VOC-MAP, SFX-MAP, FID-MAP inserted).
Symbol domains +SFX.
STYLE↔LYRICS SYNC parity list +VOC/FID/SFX + occurrence-tag parity.
Log tokens +WARN-NOVOC, +OVR-FID, +OVR-SFX, +OVR-DENSITY.
BACKEND LIMITS +NATIVE stereo pan/field motion, +SEMANTIC spectral-EQ,
+SFX object placement precision.
UNCHANGED:
Canonical source of truth.
Budget ceilings.
Zone model.
DSE CORE section codes.
Intake machinery principles.
Capability monotonicity.
CHANGE CONTROL split.
Worked example structure.
PRINCIPLE:
v3.4 gives homes to semantics that already existed without a
registered directive. No supplement may ever add a directive
(INV-036 stands).
═══════════════════════════════════════════════════════════════════════
END OF SPEC — SAUND SUNO COMPILER SKILL by 36z6 — v3.4
═══════════════════════════════════════════════════════════════════════

— END OF PART 6/6 (FINAL) —
