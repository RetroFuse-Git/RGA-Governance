# README_FIRST.md -- RetroFuse Authority Boot Pointer

**Status:** Authoritative boot surface for the ChatGPT/AI boot lane  
**Authority:** The files in this folder are byte-identical across the Google Drive boot surface mirror and the canonical disk root, verified by the RGA boot manifest / autohasher trust chain. For the AI boot lane they ARE the governing copies; do not treat them as reference, examples, or memory.  
**Purpose:** Load the complete RetroFuse authority stack into a fresh ChatGPT/project-lane session and acknowledge. This is a one-time authority load per session. Authority documents are referenced thereafter when a task affects authority.

---

## 1. Governing Principle

This file is read from the authority folder. That folder is the authoritative surface for the session -- whether accessed from the Google Drive boot surface mirror or the canonical disk root. Every file in the folder is byte-identical across both surfaces and verified by the RGA boot manifest / autohasher trust chain. Treat the files you read from this folder as real, current, and binding.

Do NOT treat these files as reference, examples, or memory. If a file conflicts with chat history, model memory, examples, receipts, or any other source, the authority folder wins.

Do not infer a path, version, file identity, ticket field, runtime state, or authority result -- use the file directly from the folder you read this from.

---

## 2. Authority Folder Location

This file lives in the authority folder. That folder exists on two surfaces:

- **Google Drive (window lane):** `G:\My Drive\RetroFuse_Backup\DailyBundles\boot_contracts\authority\`
- **Canonical disk (host/CLI lane):** `D:\RETROFUSE_OPS\RGA\authority\`

Both surfaces are byte-identical and authoritative. Use whichever surface you have access to. All file references in this document are relative to the authority folder you read this file from -- the folder containing this `README_FIRST.md`.

---

## 3. Authority Load

Load the authority stack from `boot_contracts\authority\` in this binding order. This order is declared by `OPS_CANONICAL_INDEX.md` and is not redefined here.

"Loading" means establishing that each document is present, current, and authoritative -- NOT reading every document in full. Read individual authority documents in full only when a ticket or decision actually requires their content. Full word-for-word reading of every authority document is not required for boot.

### 3.1 Binding Authority Stack (load in order)

| # | File | Role |
|---|------|------|
| 1 | `README_FIRST.md` | Orientation (this file) |
| 2 | `RetroFuse_SAFEPOINT_SOP_v3.2.md` | Process law |
| 3 | `RetroFuse_SESSION_HANDOFF_SOP_v1.md` | Session hydration and handoff |
| 4 | `Governance_RetroFuse_v3.3.1.md` | Governance authority |
| 5 | `AI_Contract_Safepoint_v3.2.json` | AI constraints |
| 6 | `RetroFuse_OPS_StartupContract_OPSCOO_v1.md` | OPS role binding |
| 7 | `OPS_CANONICAL_INDEX.md` | Authoritative path resolution |
| 8 | `RetroFuse_CR_Schemas_v3.1.1.json` | CR schemas |

### 3.2 Operational Role Files (load after binding stack)

| # | File | Role |
|---|------|------|
| 1 | `OPS_Handoff_Pack_v1.4.md` | OPS handoff pack |
| 2 | `RGA_LANE_AUTHORITY_REGISTRY_v1.json` | Lane authority registry |
| 3 | `RGA_CLI_LAUNCHER_CONTRACT_v2.md` | CLI launcher contract |

### 3.3 Lane Roles

- **ChatGPT** -- authority/QC/final seal
- **CLI** -- sole routing and aggregation authority
- **Gemini** -- advisory mechanics/DOM validation
- **DeepSeek** -- advisory reasoning/architecture review
- **Copilot/Codex/Claude worker lanes** -- bounded implementation only when authorized

No model lane self-routes.

### 3.4 Host-Only Files (not on Drive, not required for window boot)

The following are referenced by `OPS_CANONICAL_INDEX.md` but live on the host disk only. A Drive-only window cannot load them. They are consumed by host-side processes and are not required for authority boot from the window lane:

- `OPS_PathRegistry_v1.json` (host: `D:\RETROFUSE_OPS\Registry\OPS_COO\State\`)
- `BLUEPRINT.md` (host: `D:\RETROFUSE_OPS\`, `D:\RETROFUSE_OPS\Registry\OPS_COO\`)
- `RGA_Authority_Bootloader.ps1` (host: `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\`)

Do not halt on their absence from the Drive surface. Do not attempt to infer their contents.

### 3.5 Failure Conditions

If any required authority artifact in sections 3.1 or 3.2 is missing, unreadable, contradictory, or unverifiable, halt with:

- `MISSING_ARTIFACTS`, or
- `AUTHORITY_CONFLICT`

Do not continue on partial authority hydration.

---

## 4. Ticket Contract Ingestion

After the binding authority stack is loaded, ingest the RCD ticket contract family from:

```
boot_contracts\authority\RCD_TICKET_CONTRACT\
```

### 4.1 Required Ingestion (read into working context)

The index alone is NOT sufficient hydration. These field rules must be present in working context:

| File | Role |
|------|------|
| `RCD_TICKET_CONTRACT_INDEX.md` | Contract index and status |
| `RCD_TICKET_ENVELOPE.schema.json` | Envelope schema |
| `RCD_TICKET_ENVELOPE_CLASSES.md` | Envelope classes |
| `RCD_TICKET_FIELD_SEMANTICS.md` | Field semantics |
| `RCD_TICKET_AUTHORITY_EFFECTS.md` | Authority effects |
| `RCD_TICKET_AUTHORING_SOP.md` | Authoring SOP |
| `RCD_TICKET_CONTROL_PLAN.md` | Control plan |
| `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json` | Authority-response schema |
| `RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md` | Authority-response SOP |
| `RCD_AUTHORITY_SEAL.schema.json` | Authority-seal schema |

### 4.2 Canary (mandatory, before reporting READY)

Validate the contract fixtures in `boot_contracts\authority\RCD_TICKET_CONTRACT\_fixtures\` against the loaded authority-response schema (`RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`):

- `terminal_valid.json` -- MUST validate
- `nonterminal_valid.json` -- MUST validate
- `missing_classification.json` -- MUST be rejected
- `malformed_json.txt` -- MUST be rejected
- `natural_language_only.txt` -- MUST be rejected

Report each fixture's PASS/REJECT. If the schema or fixtures cannot be loaded, or validation cannot be performed from the loaded contract contents, halt:

`HALT_OPERATIONAL_HYDRATION`

---

## 5. Host-Side Deferrals

The following are host-lane responsibilities. A Drive-only window must NOT claim to have performed them. Record them as deferred and proceed when the Drive authority set is complete and hash-consistent.

| Item | Status | Owner |
|------|--------|-------|
| Bootloader admission (`RGA_Authority_Bootloader.ps1`) | `HOST_BOOTLOADER_ADMISSION_DEFERRED` | CLI lane |
| Runtime control verification | `HOST_RUNTIME_CONTROL_DEFERRED` | CLI lane |
| RCD health check (`Invoke-RCDHealthCheck.ps1`) | `HOST_RUNTIME_DEFERRED` | CLI lane |
| Conductor invocation (`Invoke-RCDConductor.ps1`) | `HOST_RUNTIME_DEFERRED` | CLI lane |
| CR and Ledger surfaces | `HOST_CONTINUITY_DEFERRED` | CLI lane |

ChatGPT must not claim host-disk verification unless explicit tool, connector, CLI, receipt, or operator evidence is present.

---

## 6. Authority Load Report

After successful authority load and ticket contract ingestion, report:

`--AUTHORITY LOAD COMPLETE--`

Include:

- full paths of loaded authority files;
- ticket contract ingestion result (canary PASS/REJECT per fixture);
- host-side deferrals recorded;
- any warnings or nonblocking gaps.

A missing required report is an invalid boot under the OPS Startup Contract.

---

## 7. Next Steps (separate procedures)

The following are separate procedures that run after the authority load is acknowledged. They are NOT part of this authority boot:

- **Daily Bundle Load:** Locate the current Daily Bundle ZIP and follow the instructions inside its `DAILY_BUNDLE_SESSION_BOOT.md` end-to-end. Session continuity (`plan.md`) is hydrated as part of the daily bundle load. The ZIP is at:
  - Google Drive: `G:\My Drive\RetroFuse_Backup\DailyBundles\Latest\OPS_DailyBundle_<opsDay>.zip`
  - Canonical disk: `D:\RETROFUSE_OPS\_DailyBundles\OPS_DailyBundle_<opsDay>.zip`
- **Hybrid Hydration:** After both authority and daily bundle are loaded, load `CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.1.md` for the RCD authority-response contract and Daily Bundle identity verification. Required before emitting any Conductor continuation response.

---

## 8. Reference: Authority-Response Contract

Before responding to a Conductor continuation request, load and verify the active contract family under:

`boot_contracts\authority\RCD_TICKET_CONTRACT\`

Required references:

- `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`
- `RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md`
- `RCD_TICKET_CONTRACT_INDEX.md`

Every authority response must be strict JSON only and include these top-level fields:

- `schema_version`
- `classification`
- `status`
- `ticket_id`
- `chain_root_id`
- `stage_id`

The response schema FILE is `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json` (schema_id `RCD-AUTHORITY-RESPONSE-SCHEMA-v3`, schema_version `3.0.0`). Its `required_top_level_fields` mandate that the emitted `schema_version` FIELD MUST equal `RCD-ENVELOPE-v3` (must_equal). Do NOT emit `RCD-AUTHORITY-RESPONSE-v3` as the field value -- that is the schema's identifier, not the field value, and will fail strict validation.

A terminal response must additionally include:

- `authority_effect: "SEALED_TERMINAL"`
- `terminal_seal: "GRANTED"`

Do not use natural-language fallback, keyword inference, fuzzy seal recognition, or parser relaxation.

---

## 9. Reference: Canonical Tool Rule

Before implementing routing, CDP discovery, authority-surface resolution, context hydration, delivery, readback, authority admission, startup orchestration, or synchronization:

1. Discover the canonical tool.
2. Resolve its exact canonical path.
3. Invoke the canonical tool before proposing a replacement.

Do not copy, wrap, fork, duplicate, or locally reimplement canonical tool internals before the canonical entry point is invoked.

If the canonical tool cannot satisfy the active ticket, halt with:

`CANONICAL_TOOL_CONTRACT_GAP`

Include the exact tool path, invoked command, observed result, and missing contract capability.

Canonical tool paths are declared by:

- `boot_contracts\authority\OPS_CANONICAL_INDEX.md`
- `boot_contracts\authority\RGA_CANONICAL_TOOLCHAIN_REGISTRY_v1.json`

---

## 10. Reference: Canonical Roots

For host-side context, the canonical disk roots are:

- **OPS root:** `D:\RETROFUSE_OPS`
- **RGA authority root:** `D:\RETROFUSE_OPS\RGA\authority`
- **RCD operational desk:** `D:\RETROFUSE_OPS\Tools\RCD`
- **OPS registry:** `D:\RETROFUSE_OPS\Registry\OPS_COO`
- **RGA receipts:** `D:\RETROFUSE_OPS\RGA\receipts`
- **Google Drive Daily Bundle mirror:** `G:\My Drive\RetroFuse_Backup\DailyBundles`

Google Drive is a verified access mirror. It is not a replacement for local runtime authority and must not become a dependency of local CLI, Cold Lane, Conductor, or provider execution.

---

## 11. Reference: Failure Rules

Halt rather than infer when any of the following occurs:

- required authority file missing or unreadable;
- authority conflict;
- canonical path unresolved;
- hash or identity mismatch;
- stale or conflicting Drive pointer;
- missing authority-response contract;
- missing required ticket fields;
- absent `cdp_targets`;
- failed authority admission;
- failed RCD runtime readiness when runtime execution is required;
- project file conflicts with canonical disk authority.

Use the narrowest accurate failure classification and include direct evidence.

---

## 12. Reference: Do Not Load as Current Authority

Do not treat any of the following as current authority unless the canonical index explicitly reclassifies them:

- `Tools\RGA\_boot`
- retired GEN7 roots or artifacts
- stale project copies
- files named `Copy`, backup, old, retired, historical, candidate, or staging-only
- chat transcripts, model memory, DOM history, or uncited summaries
- capsules as runtime or production authority
- Google Drive duplicates not bound by exact identity

---

## 13. Reference: Required Posture

- No inference-based execution.
- No manual reconstruction of authoritative artifacts.
- No CR or Ledger rewrites.
- No unsupported disk-verification claims.
- No self-routing.
- No parser relaxation.
- No restart of completed work.
- No Drive dependency for local runtime boot.
- No broad search when exact IDs and hashes are available.
- Halt on missing or ambiguous authority.