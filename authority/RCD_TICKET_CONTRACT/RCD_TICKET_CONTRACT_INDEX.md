# RCD Ticket Contract -- Authority Index

**Version:** 1.1.0
**Status:** INSTALLED_NOT_ACTIVATED (runtime admission remains RCD-ENVELOPE-v3; selector-era authoring is ACTIVE via the selector gate)
**Authority:** RGA governs; RCD validates and executes.
**Boot rule:** RGA bootloader references this index by exact path and hash only.

## Active Contract Family

| File | Version | SHA-256 | Purpose |
|------|---------|---------|---------|
| RCD_TICKET_ENVELOPE.schema.json | 1.1.0 | `64ABB5C8BA1505FB46CECF61CD8E5B96C3BFFE68F15C425D83CC1981ACB92091` | Normative ticket envelope schema (v1.1: reconciled git_closeout_policy + selector fields) |
| RCD_AUTHORITY_SEAL.schema.json | 1.0.0 | `A579B3C0326657579CF064208EDA68673CD3FDE2CB156B80E0BA598F03DAD85B` | Normative authority decision and seal schema |
| RCD_TICKET_AUTHORING_SOP.md | 1.1.0 | `77375474784612CBFB93F65A41070A2E88BA8133F91C63C4374CDA51F8A283DB` | Human/AI authoring procedure with selector-manifest consumption requirement |
| RCD_TICKET_FIELD_SEMANTICS.md | 1.1.0 | `9CFC8A83D8DBFB7ED0B0EDB2A3253C6AE40BBB2D1679FB82EF09CF91EDFE9B73` | Canonical field ownership, selector rules, forbidden combinations |
| RCD_TICKET_ENVELOPE_CLASSES.md | 1.1.0 | `B0E785AFDBECE2BB3FF9016BB56D69E83059F924DDB8C236ACF2022D37916C3A` | Envelope classes incl. EXECUTION_RETURN/EXECUTION_TICKET, required/forbidden |
| RCD_TICKET_AUTHORITY_EFFECTS.md | 1.0.0 | `9D5776C203898A1E0E1468FA735ACFC1EE971AC0DCF10B48CE8F6F55E2C4C42D` | Authority-effect matrix and mutation consequences |
| RCD_TICKET_VERSIONING_AND_MIGRATION.md | 1.0.0 | `3F8A4F770AEBE6332B3EEA506136A2B893F4E0C3A3EBEF41112E8748B0539748` | Compatibility, version negotiation, rollback |
| RCD_TICKET_CONTROL_PLAN.md | 1.0.0 | `94CF6F7E99A893B671E455CC63AFA48D1BAEB1F3BDFC57942BBE8DC58637B185` | Operational metrics, validation gates, control limits |
| RCD_TICKET_AUTHORING_SCOPE_POLICY_v1.0.md | 1.0.0 | `9F5D2B29780E1A443EE89FC9A68E446CE330ADEB9BAC5A55EABEE176C1977802` | Ticket authoring scope, brevity, and exclusion policy |
| RCD_SELECTOR_MANIFEST_v1.json | 1.0 | `995917F6FEF7C8444D47E96B2897CCC87EE8343F0FE2B6DA907B1BE5FDD0687B` | **Selector manifest v1.0 (generated authority):** legal control-plane values, class contracts, provenance. Consumed by CLI/AI authoring + shared validator. Generated artifact -- regenerate via `RCD Tools/selector/generate_selector_manifest.py`, never hand-edit. |

## Child Hash Verification Rule
A compliant contract loader MUST verify every child file listed in this index against its declared SHA-256 before admitting any RCD ticket. Any missing, hash-mismatched, or unlisted child is a hard fail-closed. The RGA bootloader verifies this index hash against the authority manifest; child hashes are verified by the RCD contract loader at admission time.

## Selector-Era Authoring (ACTIVE)
- New envelopes MUST stamp `selector_manifest_version` and use only legal
  values from `RCD_SELECTOR_MANIFEST_v1.json`.
- Shared fail-closed validator: `D:\RETROFUSE_OPS\Tools\RCD\Tools\selector\validate_selector_envelope.py`.
- Required-unset and illegal selector values REFUSE submission before Conductor
  admission (no synonym, fuzzy, or silent-default behavior).
- Envelopes without the selector stamp follow the bounded legacy path unchanged.

## Precedence
This contract family defines the authoritative ticket format. It is currently INSTALLED_NOT_ACTIVATED. Runtime admission continues to use the pre-existing RCD-ENVELOPE-v3 path until Ticket 4 activates the validator. Selector-era construction is independent of that activation and is ACTIVE as of this chain.

## Refresh Rule
Any child-file hash change requires this index to be updated. The RGA bootloader verifies this index hash against the authority manifest. Child files listed above are verified by this index at RCD admission time; this index's own integrity is verified by the RGA boot manifest chain. The selector manifest is a generated artifact: regenerate from authoritative inputs, then re-register through RGA admission.

## Authority Response Contract (Chain 087)
| File | Version | SHA-256 | Purpose |
|------|---------|---------|---------|
| RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json | 3.0.0 | $schemaHash | Normative authority-response schema consumed by ConvertFrom-RCDContinuationJson |
| RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md | 1.0.0 | $sopHash | ChatGPT authority-response authoring procedure |
| _fixtures/terminal_valid.json | 1.0.0 | fixture | Valid terminal-seal response fixture |
| _fixtures/nonterminal_valid.json | 1.0.0 | fixture | Valid next-round continuation fixture |
| _fixtures/missing_classification.json | 1.0.0 | fixture | Missing-classification rejection fixture |
| _fixtures/malformed_json.txt | 1.0.0 | fixture | Malformed-JSON rejection fixture |
| _fixtures/natural_language_only.txt | 1.0.0 | fixture | Natural-language-only rejection fixture |
