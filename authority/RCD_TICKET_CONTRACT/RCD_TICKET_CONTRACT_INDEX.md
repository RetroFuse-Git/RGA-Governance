# RCD Ticket Contract -- Authority Index

**Version:** 1.2.0
**Status:** INSTALLED_NOT_ACTIVATED (runtime admission remains RCD-ENVELOPE-v3; selector-era authoring is ACTIVE via the selector gate)
**Authority:** RGA governs; RCD validates and executes.
**Boot rule:** RGA bootloader references this index by exact path and hash only.

## Active Contract Family

| File | Version | SHA-256 | Purpose |
|------|---------|---------|---------|
| RCD_TICKET_ENVELOPE.schema.json | 1.1.0 | `9C6E7D2EA87DF7093CD1855FC53CCB03F442CFF9CA70B780EB39D7F3A7392BAB` | Normative ticket envelope schema (v1.1: reconciled git_closeout_policy + selector fields + legacy_provenance) |
| RCD_AUTHORITY_SEAL.schema.json | 1.0.0 | `A579B3C0326657579CF064208EDA68673CD3FDE2CB156B80E0BA598F03DAD85B` | Normative authority decision and seal schema |
| RCD_TICKET_AUTHORING_SOP.md | 1.1.0 | `6F7208ABC0D4CC7D8AA1CC5E6C3148BF9F5C25D58775CE65016DB9DED3B07C5F` | Human/AI authoring procedure with selector-manifest consumption requirement |
| RCD_TICKET_FIELD_SEMANTICS.md | 1.1.0 | `C3076989BDCC134A659CF36983DCEC04A10C49B86151D01C346DB121DF98CBAB` | Canonical field ownership, selector rules, legacy qualification, forbidden combinations |
| RCD_TICKET_ENVELOPE_CLASSES.md | 1.1.0 | `828E91E6C0963AF8780536ED75B53418CE9B93379A40F4E3C23655D1D63EFC53` | Envelope classes incl. EXECUTION_RETURN/EXECUTION_TICKET, required/forbidden |
| RCD_TICKET_AUTHORITY_EFFECTS.md | 1.0.0 | `9D5776C203898A1E0E1468FA735ACFC1EE971AC0DCF10B48CE8F6F55E2C4C42D` | Authority-effect matrix and mutation consequences |
| RCD_TICKET_VERSIONING_AND_MIGRATION.md | 1.0.0 | `3F8A4F770AEBE6332B3EEA506136A2B893F4E0C3A3EBEF41112E8748B0539748` | Compatibility, version negotiation, rollback |
| RCD_TICKET_CONTROL_PLAN.md | 1.0.0 | `94CF6F7E99A893B671E455CC63AFA48D1BAEB1F3BDFC57942BBE8DC58637B185` | Operational metrics, validation gates, control limits |
| RCD_TICKET_AUTHORING_SCOPE_POLICY_v1.0.md | 1.0.0 | `9F5D2B29780E1A443EE89FC9A68E446CE330ADEB9BAC5A55EABEE176C1977802` | Ticket authoring scope, brevity, and exclusion policy |
| RCD_SELECTOR_MANIFEST_v1.json | 1.0 | `CE75EEF8438B2C7976D58C648E20EBEDF6A0BD1E4F8E30DED870D8504E2B9FFB` | **Selector manifest v1.0 (generated authority):** legal control-plane values, class contracts, provenance (8 inputs). Consumed by CLI/AI authoring + shared validator. Generated artifact -- regenerate via `RCD Tools/selector/generate_selector_manifest.py`, never hand-edit. |

## Child Hash Verification Rule
A compliant contract loader MUST verify every child file listed in this index against its declared SHA-256 before admitting any RCD ticket. Any missing, hash-mismatched, or unlisted child is a hard fail-closed. The RGA bootloader verifies this index hash against the authority manifest; child hashes are verified by the RCD contract loader at admission time.

## Selector-Era Authoring (ACTIVE)
- New envelopes MUST stamp `selector_manifest_version` and use only legal
  values from `RCD_SELECTOR_MANIFEST_v1.json`.
- Shared fail-closed validator: `D:\RETROFUSE_OPS\Tools\RCD\Tools\selector\validate_selector_envelope.py`.
- Required-unset and illegal selector values REFUSE submission before Conductor
  admission (no synonym, fuzzy, or silent-default behavior).
- Unknown git_closeout_policy REFUSES -- never silent default.
- NEW unstamped envelopes REFUSE (absence of the stamp is NOT legacy);
  legacy envelopes qualify ONLY with positive `legacy_provenance`
  (source_kind + existing source_path).
- Direct RF/operator prose authority is never constrained by selector validation.

## Precedence
This contract family defines the authoritative ticket format. It is currently INSTALLED_NOT_ACTIVATED. Runtime admission continues to use the pre-existing RCD-ENVELOPE-v3 path until Ticket 4 activates the validator. Selector-era construction is independent of that activation and is ACTIVE as of this chain.

## Refresh Rule
Any child-file hash change requires this index to be updated. The RGA bootloader verifies this index hash against the authority manifest. Child files listed above are verified by this index at RCD admission time; this index's own integrity is verified by the RGA boot manifest chain. The selector manifest is a generated artifact: regenerate from authoritative inputs, then re-register through RGA admission.

## Authority Response Contract (Chain 087)
| File | Version | SHA-256 | Purpose |
|------|---------|---------|---------|
| RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json | 3.0.0 | `6F462F7711A5DC183DEC3C98D5A3F2F0E8F0EE6A55A1FA246563686164AB0331` | Normative authority-response schema consumed by ConvertFrom-RCDContinuationJson |
| RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md | 1.0.0 | `A847C27AE6F5123283BA301F52ACD9F804720D06CFE7D7CA570448FAA9C0223A` | ChatGPT authority-response authoring procedure and binding authority-output defect ownership |
| _fixtures/terminal_valid.json | 1.0.0 | `EDA5B18199B1B468C19616F3868012E0C4524771185987CEAF95744CD156A86D` | Valid terminal-seal response fixture |
| _fixtures/nonterminal_valid.json | 1.0.0 | `115D3E7BFA9E834D3A0DD669757F778BB512A455A6BFAC0C4CAB7EFC69653305` | Valid next-round continuation fixture |
| _fixtures/missing_classification.json | 1.0.0 | `BB08F494FAAB5649B553CA1D64CDC460C65B69AA41C320915FCD3BDD55B88B8E` | Missing-classification rejection fixture |
| _fixtures/malformed_json.txt | 1.0.0 | `3F67B065F4A3CF6DCF742FD850A1102AC7D4947812C13F5C23FDBF5C0F012F8F` | Malformed-JSON rejection fixture |
| _fixtures/natural_language_only.txt | 1.0.0 | `26BBF741933D33205C3A0275CD3180819F38CAE7D8D93E0B7735575753896F41` | Natural-language-only rejection fixture |
