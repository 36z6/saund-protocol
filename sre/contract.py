"""
SRE ↔ SAUND CONTRACT v1 (version-invariant handshake).

This is the SINGLE coupling point between SRE and SAUND.
If SAUND improves (v3.4 → v3.5 → v4...), SRE keeps working.
If the intake contract itself changes (version bump + changelog):
update ONLY this file; test T11 fails loudly until repinned.
"""

C = dict(
    CONTRACT_VERSION=1,

    # Directives that exist in both SAUND v3.3 AND v3.4 (stable core)
    STABLE_DIRECTIVES={
        "GLOBAL", "ARC", "DUR-PLAN", "WGT-MAP", "SPEAKERS", "INST-MAP",
        "GRV-MAP", "HRM-MAP", "FX-MAP", "MIX-MAP", "MAST-MAP", "LEGEND",
        "TRN-MAP", "SC-MAP", "SPC-MAP", "AUT-MAP",
    },

    # DSE section codes (immutable per SAUND spec)
    DSE_CORE_SECTIONS=["I", "G", "S", "K", "R", "P", "F", "O"],

    # DSE effect codes (immutable per SAUND spec)
    DSE_CORE_EFFECTS={"R", "D", "F", "S", "W", "P", "B", "L", "G", "C"},

    # Supplement types registered in SAUND INTAKE (v3.3+)
    SUPPLEMENT_TYPES={
        "VOCAL_SUPPLEMENT", "AVATAR_SUPPLEMENT", "ORCHESTRAL_SUPPLEMENT",
        "TECHNIQUE_SUPPLEMENT", "SOUND_DESIGN_SUPPLEMENT", "GROOVE_SUPPLEMENT",
        "ARRANGEMENT_SUPPLEMENT", "DJ_SUPPLEMENT", "MIX_MASTER_SUPPLEMENT",
        "HARMONY_SUPPLEMENT", "STYLE_SUPPLEMENT", "NEGATIVE_SUPPLEMENT",
        "SYMBOL_SUPPLEMENT", "AI_FX_SUPPLEMENT", "SPATIAL_SUPPLEMENT",
        "GENERATIVE_SUPPLEMENT",
    },

    # Mandatory fields for ENTRY objects (SIE requirement)
    ENTRY_FIELDS={
        "entry_id", "supplement_id", "entry_type", "domain", "name",
        "meaning", "target", "values", "effects", "constraints",
        "capability_level", "priority", "source_trace",
    },

    # Injection actions (SIE requirement)
    INJECTION_ACTIONS={
        "ADD_ENTRY", "EXTEND_ENTRY", "MAP_TERM", "ADD_CONSTRAINT",
        "ADD_NEGATIVE", "ADD_SLOT", "ADD_SYMBOL", "ADD_LEXICON",
        "SET_DEFAULT", "OVERRIDE_DEFAULT", "DISABLE_DEFAULT",
    },

    # Supplement modes
    MODES={"STRICT", "CANDIDATE", "MERGE"},

    # Capability levels
    CAPABILITIES={
        "NATIVE", "SEMANTIC_ONLY", "BACKEND_DEPENDENT",
        "SPECULATIVE", "UNSUPPORTED",
    },

    # Hard ceilings (Suno limits)
    CEILINGS={"STYLE": 800, "LYRICS": 4000},

    # Zone B rule
    ZONE_B_RULE="markers + vocal text only; technical directives forbidden",

    # Intake report prefix
    INTAKE_PREFIX="[INTAKE]",
)

# Rule: SRE → SAUND exclusively via SIE.
# When intake contract changes in SAUND (version bump + changelog),
# update ONLY this file; test T11 fails loudly until repinned.
