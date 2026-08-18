# RetroFuse ChatGPT Hybrid-Hydration Bootstrap v1.1

**Status:** ACTIVE CANONICAL — supersedes v1.0 (`CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.md`, retained only as a superseded historical pointer)  
**Authority:** Subordinate to canonical RetroFuse governance and `OPS_CANONICAL_INDEX.md`  
**Canonical disk path:** `D:\RETROFUSE_OPS\RGA\authority\CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.1.md`  
**Purpose:** Give a fresh ChatGPT authority-QC session exact, bounded references for the active RCD authority-response contract and current Daily Bundle identity after the mandatory RetroFuse authority stack has been loaded.

---

## 1. Scope and Preconditions

This document is not the complete RetroFuse boot sequence.

Invoke it only after the mandatory authority, role-binding, and session-continuity layers have been loaded according to `OPS_CANONICAL_INDEX.md`, including:

- `RetroFuse_SAFEPOINT_SOP_v3.2.md`
- `RetroFuse_SESSION_HANDOFF_SOP_v1.md`
- `Governance_RetroFuse_v3.3.1.md`
- `AI_Contract_Safepoint_v3.2.json`
- `RetroFuse_CR_Schemas_v3.1.1.json`
- `RetroFuse_OPS_StartupContract_OPSCOO_v1.md`
- `OPS_CANONICAL_INDEX.md`
- applicable `plan.md`

This sub-bootstrap does exactly two things:

1. Hydrates the strict ChatGPT authority-response contract required for RCD Conductor continuation responses.
2. Resolves the current Daily Bundle identity from the verified Google Drive mirror.

It does not replace canonical disk authority, local runtime hydration, OPS continuity records, project plans, provider workflows, Conductor routing, or Cold Lane boot.

---

## 2. Authority and Precedence

Use this precedence when resolving conflicts:

1. Explicit operator instruction for the active session
2. Canonical governance and process law
3. Canonical disk authority and `OPS_CANONICAL_INDEX.md`
4. Active RCD ticket-contract authority family
5. Verified Google Drive mirrors
6. Project-file copies
7. Chat history or model memory

A lower layer must never override a higher layer.

Google Drive is an access mirror. Local runtime boot must remain functional when Drive is unavailable.

---

## 3. Canonical Local References

### 3.1 Authority-response contract family

Canonical root:

`D:\RETROFUSE_OPS\RGA\authority\RCD_TICKET_CONTRACT`

Required files:

- `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`
- `RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md`
- `RCD_TICKET_CONTRACT_INDEX.md`

### 3.2 Bootstrap artifact

Canonical path (this file):

`D:\RETROFUSE_OPS\RGA\authority\CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.1.md`

This v1.1 file is the active canonical hybrid-hydration bootstrap and supersedes the v1.0 artifact (`CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.md`, retained only as a superseded historical pointer). The admitted SHA-256 of this v1.1 file is supplied by the RGA authority-admission receipt after each corrective revision; do not use a stale hash as the identity of revised content.

### 3.3 Daily Bundle mirror

Drive folder:

`G:\My Drive\RetroFuse_Backup\DailyBundles`

Resolution mode (Option B, 2026-08-06): resolve bundle identity from the ROOT
files by filename. Pointer files (`DAILY_BUNDLE_DRIVE_POINTER_Latest.json`,
`OPS_DailyBundle_ZIP_POINTER.txt`) are nested under `Latest\` and are NOT boot
inputs; do not load or verify them during hydration.

---

## 4. Verified Drive References

The original Chain 089 bootstrap reported the following mirror locations for the authority-response family:

- Schema: `G:\My Drive\RetroFuse_Backup\DailyBundles\boot_contracts\authority\RCD_TICKET_CONTRACT\RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`
- SOP: `G:\My Drive\RetroFuse_Backup\DailyBundles\boot_contracts\authority\RCD_TICKET_CONTRACT\RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md`
- Contract index: `G:\My Drive\RetroFuse_Backup\DailyBundles\boot_contracts\authority\RCD_TICKET_CONTRACT\RCD_TICKET_CONTRACT_INDEX.md`
- Daily Bundle root (resolve by filename): `G:\My Drive\RetroFuse_Backup\DailyBundles`

Accepted identities from sealed Chain 089:

- Authority-response schema SHA-256: `6F462F7711A5DC183DEC3C98D5A3F2F0E8F0EE6A55A1FA246563686164AB0331`
- Authority-response SOP SHA-256: `EEC374ABB1D04A20277B234DA89DB49BFEE4F56B37E2D88563C475C27A42C880`
- Ticket-contract index SHA-256: `461DB2DFD7440BE3F5671953651C3FEF252D0905AC4902D2E25720E0A28511A3`

No pointer SHA-256 pin applies under Option B. Bundle identity is resolved and
verified by filename at the Daily Bundle root per Step 5.

Do not infer a Google Drive file ID. When connector access is available, resolve each exact path to its actual Drive file ID and verify the returned file identity. If a required ID cannot be resolved or more than one conflicting file claims the same canonical identity, halt.

---

## 5. Resolution Order

Execute this exact sub-sequence after full authority boot:

### Step 1 — Resolve the authority-response schema

Load:

`RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`

Verify:

- exact canonical filename;
- exact canonical local or Drive location;
- expected SHA-256 or currently admitted replacement identity;
- parseable JSON schema;
- schema version accepted by the active parser contract.

The required authority-response schema version is:

`RCD-ENVELOPE-v3`

Do NOT emit `RCD-AUTHORITY-RESPONSE-v3` as the `schema_version` field value. The schema's `required_top_level_fields.schema_version.must_equal` is `RCD-ENVELOPE-v3`; `RCD-AUTHORITY-RESPONSE-SCHEMA-v3` is the schema identifier (schema_id), not the field value.

### Step 2 — Resolve the authority-response authoring SOP

Load:

`RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md`

Verify that it requires strict JSON-only output and the current top-level fields.

### Step 3 — Resolve the ticket-contract index

Load:

`RCD_TICKET_CONTRACT_INDEX.md`

Use it to determine active contract status, schema locations, fixtures, authoring requirements, and activation state.

Do not assume the ticket envelope family and the authority-response family use the same `schema_version` value.

### Step 4 — Bind the Conductor response contract

Before emitting any Conductor continuation response, bind these required top-level fields:

- `schema_version`
- `classification`
- `status`
- `ticket_id`
- `chain_root_id`
- `stage_id`

Copy `ticket_id`, `chain_root_id`, and `stage_id` exactly from the request.

Permitted authority effects remain those declared by the active contract. Do not invent compound authority effects.

For terminal closure, include:

- `authority_effect: "SEALED_TERMINAL"`
- `terminal_seal: "GRANTED"`

A terminal response must use:

`schema_version: "RCD-ENVELOPE-v3"`

### Step 5 — Resolve the Daily Bundle by filename at the Drive root

The Daily Bundle root is:

`G:\My Drive\RetroFuse_Backup\DailyBundles`

Resolve the bundle identity from the connector-visible ROOT files by filename.
Do NOT load, pin, or verify `DAILY_BUNDLE_DRIVE_POINTER_Latest.json`; pointer
files are nested under `Latest\` for Drive-ID preservation and audit, and are
NOT boot inputs (Option B, 2026-08-06).

Resolve and verify, by exact filename at the root:

- bundle ZIP: `OPS_DailyBundle_<opsDay>.zip` (read its SHA-256 from the
  dated manifest's `bundle.sha256` field);
- dated manifest: `OPS_DailyBundle_<opsDay>_manifest.json` (authoritative
  for `opsDay`, bundle SHA-256, CR path, and Ledger path);
- latest manifest: `OPS_DailyBundle_Latest_manifest.json` (must be
  byte-identical to the dated manifest);
- dated ColdLane receipt: `COLDLANE_RECEIPT_<opsDay>.txt`;
- latest ColdLane receipt: `COLDLANE_RECEIPT_LATEST.txt` (must be
  byte-identical to the dated receipt);
- provider hydration artifacts: `OPS_DailyBundle_Latest.txt`,
  `OPS_DailyBundle_Latest_deepseek.txt`, `OPS_DailyBundle_Latest_gemini.txt`;
- current-day CR and Ledger: `CR_OPS_<today>.md`, `OPS_COO_Ledger_<today>.md`;
- working plan: `plan.md`.

Verify:

- dated manifest and latest manifest SHA-256 are equal;
- dated receipt and latest receipt SHA-256 are equal;
- the dated manifest `opsDay` matches the receipt `opsDay`;
- the bundle ZIP SHA-256 equals the manifest `bundle.sha256`;
- provider hydration artifacts are present (hash equality with manifest is
  not required; presence and freshness are sufficient).

The Daily Bundle is a prior-day snapshot by design. The `opsDay` may therefore
be the previous calendar day until the next successful rotation. Do not
classify a one-day difference as stale without checking the declared rotation
policy and latest accepted publication evidence.

### Step 6 — Report bounded hydration state

A successful sub-bootstrap report must state:

- authority-response schema filename and SHA-256;
- authoring SOP filename and SHA-256;
- ticket-contract index filename and SHA-256;
- Daily Bundle root path and the resolved bundle/opsDay identity (by filename);
- current `ops_day`;
- current bundle filename and SHA-256;
- whether Drive IDs were directly resolved;
- any nonblocking freshness note;
- whether ChatGPT is ready to emit parser-conformant authority responses.

Do not claim direct Drive retrieval merely because a path is present in a project file. Direct retrieval requires actual connector, mounted-drive, CLI, or operator evidence.

---

## 6. Authority-Response Output Contract

Every ChatGPT Conductor continuation response must be a single strict JSON object with no markdown fence and no trailing prose.

Minimum required shape:

```json
{
  "schema_version": "RCD-ENVELOPE-v3",
  "classification": "<contract-valid classification>",
  "status": "<contract-valid status>",
  "ticket_id": "<copied exactly>",
  "chain_root_id": "<copied exactly>",
  "stage_id": "<copied exactly>"
}
```

Terminal closeout adds:

```json
{
  "authority_effect": "SEALED_TERMINAL",
  "terminal_seal": "GRANTED"
}
```

Nonterminal responses must use only contract-valid classifications, statuses, and authority effects.

Do not:

- scan natural language for authority intent;
- infer omitted fields;
- accept aliases not present in the contract;
- relax parser behavior;
- emit `RCD-AUTHORITY-RESPONSE-v3` as the `schema_version` field value (that is the schema identifier, not the field value);
- add commentary outside the JSON object.

---

## 7. Daily Bundle Identity Contract

One canonical Daily Bundle identity must be consistent across:

- local bundle ZIP;
- local manifest;
- Drive mirror bundle;
- Drive mirror manifest;
- ChatGPT hydration artifact;
- Gemini hydration artifact;
- DeepSeek hydration artifact.

All provider hydration artifacts must reference the same canonical bundle SHA-256.

Provider-specific behavior remains unchanged:

- ChatGPT resolves the bundle and hydration artifact by filename at the Drive root.
- Gemini uses the byte-identical `.zip.txt` artifact plus the required parsing helper and boot text.
- DeepSeek uses the byte-identical `.zip.txt` artifact plus the boot text.

This bootstrap does not authorize provider submission or DOM delivery.

---

## 8. Fail-Closed Conditions

Halt with bounded diagnostics when any of the following occurs:

- full authority boot has not completed;
- required schema, SOP, or contract index is missing;
- Drive path is inaccessible and no verified local canonical copy is available;
- expected hash does not match;
- more than one conflicting Drive item claims the same canonical artifact;
- Drive file ID cannot be resolved when exact ID verification is required;
- schema version is not `RCD-ENVELOPE-v3` for authority responses;
- required response fields are absent or ambiguous;
- required root files (bundle, dated/latest manifests, dated/latest receipts,
  hydration artifacts) are missing or hash-mismatched against the dated
  manifest identity;
- freshness cannot be reconciled against the declared prior-day rotation policy;
- project-file content conflicts with canonical disk authority;
- a response would depend on DOM history, model memory, or inference.

Recommended classifications:

- `MISSING_ARTIFACTS`
- `AUTHORITY_CONFLICT`
- `HARD_HALT`
- `HASH_MISMATCH`
- `DRIVE_IDENTITY_CONFLICT`
- `POINTER_INVALID`
- `CONTRACT_NOT_LOADED`

Use only classifications permitted by the active response contract when emitting through Conductor.

---

## 9. No-Change and Rotation Rules

- A no-change hydration pass must not rewrite Drive files.
- Root files are rotated only when the dated manifest identity changes (new opsDay).
- Do not publish a root set that is partial, stale, missing, mismatched, or unvalidated.
- Pointer files under `Latest\` are audit/Drive-ID records and are not boot inputs.
- Do not delete, rename, move, or deduplicate unrelated Drive files through this bootstrap.

---

## 10. Explicit Non-Authority Boundaries

This bootstrap does not authorize:

- CR or Ledger creation or mutation;
- plan creation or mutation;
- capsule loading as runtime authority;
- SAFEPOINT creation or intake;
- provider submission;
- Conductor invocation;
- ticket emission;
- parser modification;
- project-file replacement;
- Drive cleanup;
- local runtime boot redirection;
- broad dynamic hydration of historical state.

Each action requires its own governing authority or execution ticket.

---

## 11. Success State

The hybrid-hydration sub-bootstrap succeeds only when:

1. Full RetroFuse authority boot has completed.
2. The authority-response schema, SOP, and ticket-contract index are resolved and verified.
3. ChatGPT has bound `RCD-ENVELOPE-v3` as the response schema.
4. The current Daily Bundle identity is resolved by filename at the root and its freshness is reconciled.
5. The resolved bundle and provider hydration identities are mutually consistent.
6. ChatGPT can state the exact current contract and bundle identities without relying on DOM history or inference.
7. Local runtime authority remains unchanged and independent of Drive availability.

Successful state label:

`CHATGPT_HYBRID_HYDRATION_READY`
