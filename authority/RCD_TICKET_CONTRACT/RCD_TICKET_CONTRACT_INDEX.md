# RCD Ticket Contract -- Authority Index

**Version:** 1.0.0
**Status:** INSTALLED_NOT_ACTIVATED
**Authority:** RGA governs; RCD validates and executes.
**Boot rule:** RGA bootloader references this index by exact path and hash only.

## Active Contract Family

| File | Version | SHA-256 | Purpose |
|------|---------|---------|---------|
| RCD_TICKET_ENVELOPE.schema.json | 1.0.0 | `45C7B0DA04A4F8D765FF0E7495BF2FA5AA104060D761FEEED7BBB929356611DF` | Normative ticket envelope schema |
| RCD_AUTHORITY_SEAL.schema.json | 1.0.0 | `A579B3C0326657579CF064208EDA68673CD3FDE2CB156B80E0BA598F03DAD85B` | Normative authority decision and seal schema |
| RCD_TICKET_AUTHORING_SOP.md | 1.0.0 | `559FC77931DFCFFEB3AA604E61C96B51D06EF6960055B0E040896284AE06ECB1` | Human authoring procedure with lookup-first workflow |
| RCD_TICKET_FIELD_SEMANTICS.md | 1.0.0 | `F30847F1519F88D6168120AA4E5F2330FF6FFB3D6EE94794601863A51314A0E2` | Canonical field ownership and constraints |
| RCD_TICKET_ENVELOPE_CLASSES.md | 1.0.0 | `1B744B8CCC119B27DCD2E3AD3B7955FDEFD9D6DC9F067CADC0F08158A918C761` | Envelope classes with required/forbidden fields |
| RCD_TICKET_AUTHORITY_EFFECTS.md | 1.0.0 | `9D5776C203898A1E0E1468FA735ACFC1EE971AC0DCF10B48CE8F6F55E2C4C42D` | Authority-effect matrix and mutation consequences |
| RCD_TICKET_VERSIONING_AND_MIGRATION.md | 1.0.0 | `3F8A4F770AEBE6332B3EEA506136A2B893F4E0C3A3EBEF41112E8748B0539748` | Compatibility, version negotiation, rollback |
| RCD_TICKET_CONTROL_PLAN.md | 1.0.0 | `94CF6F7E99A893B671E455CC63AFA48D1BAEB1F3BDFC57942BBE8DC58637B185` | Operational metrics, validation gates, control limits |

## Child Hash Verification Rule
A compliant contract loader MUST verify every child file listed in this index against its declared SHA-256 before admitting any RCD ticket. Any missing, hash-mismatched, or unlisted child is a hard fail-closed. The RGA bootloader verifies this index hash against the authority manifest; child hashes are verified by the RCD contract loader at admission time.

## Precedence
This contract family defines the authoritative ticket format. It is currently INSTALLED_NOT_ACTIVATED. Runtime admission continues to use the pre-existing RCD-ENVELOPE-v3 path until Ticket 4 activates the validator.

## Refresh Rule
Any child-file hash change requires this index to be updated. The RGA bootloader verifies this index hash against the authority manifest. The 8 child files listed above are verified by this index at RCD admission time; this index's own integrity is verified by the RGA boot manifest chain.

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