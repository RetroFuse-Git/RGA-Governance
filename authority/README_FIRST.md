# README_FIRST.md -- RetroFuse ChatGPT Project Boot Pointer

**Status:** Authoritative boot surface for the ChatGPT/AI boot lane  
**Authority:** Authoritative - the Drive boot surface files are byte-identical to canonical disk and verified by the RGA boot manifest / autohasher trust chain. For the AI boot lane they ARE the governing copies; do not treat them as reference, examples, or memory.  
**Purpose:** Direct a fresh ChatGPT/project-lane session into the complete current RGA/RCD authority, continuity, and hybrid-hydration sequence without redefining authority order.

---

## 1. Governing Principle

The Google Drive boot surface is the authoritative mirror of the canonical authority set. Every file on the boot surface is byte-identical to its canonical disk counterpart and is verified by the RGA boot manifest / autohasher trust chain. For the AI boot lane, these Drive copies ARE authoritative -- treat them as real, current, and binding.

Do NOT treat Drive copies as reference, examples, or memory. If a Drive copy conflicts with chat history, model memory, examples, receipts, or any other source, the Drive boot surface wins. Do not infer a path, version, file identity, ticket field, runtime state, or authority result -- use the Drive copy directly.

Do not infer a path, version, file identity, ticket field, runtime state, or authority result.

---

## 2. Mandatory Canonical-Tool Rule

Before implementing routing, CDP discovery, authority-surface resolution, context hydration, delivery, readback, authority admission, startup orchestration, or synchronization:

1. Discover the canonical tool.
2. Resolve its exact canonical path.
3. Invoke the canonical tool before proposing a replacement.

Do not copy, wrap, fork, duplicate, or locally reimplement canonical tool internals before the canonical entry point is invoked.

If the canonical tool cannot satisfy the active ticket, halt with:

`CANONICAL_TOOL_CONTRACT_GAP`

Include the exact tool path, invoked command, observed result, and missing contract capability.

Canonical tool paths are declared by:

- `D:\RETROFUSE_OPS\RGA\authority\OPS_CANONICAL_INDEX.md`
- `D:\RETROFUSE_OPS\RGA\authority\RGA_CANONICAL_TOOLCHAIN_REGISTRY_v1.json`

---

## 3. Canonical Roots

- **OPS root:** `D:\RETROFUSE_OPS`
- **RGA authority root:** `D:\RETROFUSE_OPS\RGA\authority`
- **RCD operational desk:** `D:\RETROFUSE_OPS\Tools\RCD`
- **OPS registry:** `D:\RETROFUSE_OPS\Registry\OPS_COO`
- **RGA receipts:** `D:\RETROFUSE_OPS\RGA\receipts`
- **Google Drive Daily Bundle mirror:** `G:\My Drive\RetroFuse_Backup\DailyBundles`

Google Drive is a verified access mirror. It is not a replacement for local runtime authority and must not become a dependency of local CLI, Cold Lane, Conductor, or provider execution.

---

## 4. Complete ChatGPT Boot Sequence

### Phase A -- Orientation

1. Read this file only as an orientation pointer.
2. Establish the canonical authority root as `D:\RETROFUSE_OPS\RGA\authority`.
3. Do not perform implementation, ticket emission, CDP delivery, or runtime mutation yet.

### Phase B -- Binding Authority Boot

Load the authority stack in the binding order declared by `OPS_CANONICAL_INDEX.md`. This file does not redefine that order.

The currently declared order is:

1. `README_FIRST.md` -- orientation only
2. `RetroFuse_SAFEPOINT_SOP_v3.2.md` -- process law
3. `RetroFuse_SESSION_HANDOFF_SOP_v1.md` -- session hydration and handoff
4. `Governance_RetroFuse_v3.3.1.md` and `AI_Contract_Safepoint_v3.2.json` -- authority and AI constraints
5. `RetroFuse_OPS_StartupContract_OPSCOO_v1.md` -- OPS role binding
6. `OPS_CANONICAL_INDEX.md` -- authoritative path resolution

Also load the binding schema authority referenced by the stack:

- `RetroFuse_CR_Schemas_v3.1.1.json`

If any required authority artifact is missing, unreadable, contradictory, or unverifiable, halt with:

- `MISSING_ARTIFACTS`, or
- `AUTHORITY_CONFLICT`

Do not continue on partial authority hydration.

**Loading vs reviewing:** "Loading" the authority stack means establishing that
each document is present, current, and authoritative -- NOT reading every
document in full. RGA integrity verification (manifest hashes, trust chain) is
performed host-side by the canonical bootloader (Phase C), not by reading
documents here. Read individual authority documents in full only when a ticket
or decision actually requires their content. Full word-for-word reading of
every authority document is not required for boot.

### Phase C -- Authority Integrity Admission

For a governed runtime or CLI session, use the canonical authority bootloader rather than manually recreating its checks:

`D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\RGA_Authority_Bootloader.ps1`

The bootloader must validate the boot manifest and protected authority identities. A failed admission is a hard stop.

ChatGPT must not claim host-disk verification unless explicit tool, connector, CLI, receipt, or operator evidence is present.

### Phase D -- OPS Role and Operational Re-entry

After binding authority is loaded, load:

1. `OPS_Handoff_Pack_v1.4.md`
2. `RGA_LANE_AUTHORITY_REGISTRY_v1.json`
3. `RGA_CLI_LAUNCHER_CONTRACT_v2.md`
4. `OPS_PathRegistry_v1.json` as supporting routing reference
5. Applicable workspace or project `BLUEPRINT.md`, when declared

Lane roles remain:

- ChatGPT -- authority/QC/final seal
- CLI -- sole routing and aggregation authority
- Gemini -- advisory mechanics/DOM validation
- DeepSeek -- advisory reasoning/architecture review
- Copilot/Codex/Claude worker lanes -- bounded implementation only when authorized

No model lane self-routes.

### Phase E -- Session Continuity

Before project work or mutation:

1. Discover the nearest governed project root.
2. Read its `plan.md` as the primary active-work state.
3. Read an enclosing workspace `plan.md` only as supplemental context.
4. Identify completed work, unresolved state, next speaker, next question, active risks, and exact resume point.
5. Do not restart work marked complete.

If no applicable plan exists, report:

`PLAN_NOT_FOUND`

Do not fabricate one unless the active authority explicitly authorizes creation.

### Phase E.1 -- Google Drive boot surface

A fresh ChatGPT window boots from the Drive boot surface at:

`G:\My Drive\RetroFuse_Backup\DailyBundles`

1. **Authority (authoritative):** Load the ENTIRE authority folder:
   `boot_contracts\authority\` -- every file there is authoritative for this
   boot. Read `README_FIRST.md` (orientation), `OPS_CANONICAL_INDEX.md`
   (path authority), and the full binding stack in the boot order it declares
   (SAFEPOINT SOP, Session Handoff SOP, Governance, AI Contract, CR Schemas,
   Startup Contract, Handoff Pack, Lane Registry, CLI Launcher Contract).
   Review `boot_contracts\authority\RCD_TICKET_CONTRACT\` -- the ticket
   contract family (index, authoring SOP, envelope schema/classes, field
   semantics, authority effects, control plan, versioning, authority-response
   schema/SOP, authority-seal schema). These are authoritative for ticket
   emission. All files in `boot_contracts\authority\` are authoritative.
   INGESTION (mandatory): Read the RCD_TICKET_CONTRACT child contents into
   working context -- `RCD_TICKET_ENVELOPE.schema.json`,
   `RCD_TICKET_ENVELOPE_CLASSES.md`, `RCD_TICKET_FIELD_SEMANTICS.md`,
   `RCD_TICKET_AUTHORITY_EFFECTS.md`, `RCD_TICKET_AUTHORING_SOP.md`,
   `RCD_TICKET_CONTROL_PLAN.md`, plus `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`,
   `RCD_AUTHORITY_RESPONSE_AUTHORING_SOP.md`, and
   `RCD_AUTHORITY_SEAL.schema.json`. The index alone is NOT sufficient
   hydration; the field rules must be present in working context.
   CANARY (mandatory, before reporting READY): validate the contract fixtures
   against the loaded authority-response schema
   (`RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json`) in
   `boot_contracts\authority\RCD_TICKET_CONTRACT\_fixtures\`:
   `terminal_valid.json` and `nonterminal_valid.json` MUST validate;
   `missing_classification.json`, `malformed_json.txt`, and
   `natural_language_only.txt` MUST be rejected. Report each fixture's
   PASS/REJECT. If the schema or fixtures cannot be loaded, or validation
   cannot be performed from the loaded contract contents, halt:
   `HALT_OPERATIONAL_HYDRATION`.

2. **Five daily files (read in this order):** Locate and read these files in
   `Latest\` on the boot surface:
   1. `OPS_DailyBundle_<opsDay>.zip` -- the Daily Bundle ZIP.
   2. `OPS_DailyBundle_<opsDay>_manifest.json` -- the dated bundle manifest.
   3. `OPS_DailyBundle_Latest_manifest.json` -- the latest manifest pointer.
   4. `COLDLANE_RECEIPT_<opsDay>.txt` -- the dated ColdLane receipt.
   5. `COLDLANE_RECEIPT_LATEST.txt` -- the latest ColdLane receipt.
   These five files identify the current bundle, its manifest identity, and
   the ColdLane receipt state. Read them before booting the ZIP.

3. **Boot the Daily Bundle ZIP (MANDATORY -- the ZIP's instructions govern):**
   Open the Daily Bundle ZIP on the boot surface
   (`Latest\OPS_DailyBundle_<opsDay>.zip`) and boot per the instructions
   INSIDE the ZIP. Read the ZIP's internal `DAILY_BUNDLE_SESSION_BOOT.md` and
   execute the 8 stages in order as the binding boot procedure -- they are not
   advisory. The bundle ZIP and its internal boot doc are authoritative for
   the boot. Do NOT substitute the surface copy of the boot doc for the ZIP's
   internal copy; the ZIP must be opened and its internal instructions
   followed.

4. **Hydrate the plan:** Read `plan.md` from the boot surface as the active
   working plan (current-state section first). It is the working continuity
   state; it does not override the authority folder or the bundle.

Then report `READY_FOR_DISCUSSION_ONLY` (Stage 7, no ticket) or proceed per
the bundle's stages. Host-side verification and receipt persistence belong to
the governed CLI lane.

**ColdLane receipt usage:** The AI reads the ColdLane receipts (files 2.4 and
2.5) as identity and freshness evidence (opsDay, bundle SHA, timestamp). The AI
does NOT re-run or regenerate the ColdLane receipt -- ColdLane execution and
receipt writing are host-side operations belonging to the governed CLI lane.

### Phase E.2 -- Daily boot (subsequent days)

On any day after the first boot, a ChatGPT window boots with one instruction:

> Locate the current Daily Bundle ZIP on the Drive boot surface
> (`G:\My Drive\RetroFuse_Backup\DailyBundles\Latest\OPS_DailyBundle_<opsDay>.zip`),
> open it, and follow the instructions inside its `DAILY_BUNDLE_SESSION_BOOT.md`
> (the 8 stages) end-to-end.

The current day's ZIP is placed in the Drive `Latest\` folder automatically
every morning (bundle built 05:15, Drive-published 05:22). The ZIP's internal
boot doc is the binding procedure; the authority folder and plan are already on
the boot surface if needed.

### Phase F -- ChatGPT Hybrid Hydration

After the binding authority stack and continuity state are loaded, load:

`CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.md`

This is a specialized sub-sequence, not a replacement boot sequence.

It must resolve and verify, in order:

1. RCD authority-response schema
2. RCD authority-response authoring SOP
3. RCD ticket-contract index
4. Current Daily Bundle Drive pointer

The authority-response contract must be loaded before ChatGPT emits any Conductor continuation response.

### Phase G -- Runtime Readiness

When runtime execution is authorized:

1. Run the canonical RCD health check:
   `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDHealthCheck.ps1`
2. Hydrate the current Daily Bundle through the established local path.
3. Confirm CR and Ledger surfaces exist when the active ticket requires recording.
4. Use the canonical Conductor for governed cross-lane delivery:
   `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDConductor.ps1`

Do not call bridge internals directly from noncanonical scripts.

### Phase H -- Boot Report

After successful OPS bootstrap, report:

`--OPS BOOTSTRAP COMPLETE--`

Include:

- full paths of loaded authority files;
- applicable `plan.md` path or `PLAN_NOT_FOUND`;
- Daily Bundle `ops_day` and bundle SHA-256;
- active authority-response contract identity;
- RCD health result when runtime readiness was invoked;
- current OPS Ledger path;
- capsule delta marker when available;
- any warnings or nonblocking gaps.

A missing required report is an invalid boot under the OPS Startup Contract.

---

## 5. ChatGPT Authority-Response Contract

Before responding to a Conductor continuation request, load and verify the active contract family under:

`D:\RETROFUSE_OPS\RGA\authority\RCD_TICKET_CONTRACT`

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

The response schema FILE is `RCD_AUTHORITY_RESPONSE_SCHEMA_v3.json` (schema_id `RCD-AUTHORITY-RESPONSE-SCHEMA-v3`, schema_version `3.0.0`).
Its `required_top_level_fields` mandate that the emitted `schema_version`
FIELD MUST equal `RCD-ENVELOPE-v3` (must_equal). Do NOT emit
`RCD-AUTHORITY-RESPONSE-v3` as the field value -- that is the schema's
identifier, not the field value, and will fail strict validation.

A terminal response must additionally include:

- `authority_effect: "SEALED_TERMINAL"`
- `terminal_seal: "GRANTED"`

Do not use natural-language fallback, keyword inference, fuzzy seal recognition, or parser relaxation.

---

## 6. RCD Ticket Emission Support

Operational RCD support artifacts live under:

`D:\RETROFUSE_OPS\Tools\RCD\Artifacts`

Current support set includes:

- `RCD-CLI-ROUTING-CONTRACT-v1.2.md`
- `RCD-CROSSLANE-ENVELOPE-v3.1.md`
- `RCD-TICKET-GATE-V2-PHASE7-ROUND-MODE-SPEC.md`
- `RCD-FEEDBACK-ATTACHMENT-RULES-v1.md`
- `MINI_UNITY_FEEDBACK_LOOP_AMENDMENT.md`
- `RCD_MINI_UNITY_DATA_GATHERING_METHOD_v1.md`

Ticket emission must preserve the required ticket container, workflow authorization, Phase 7/7E provenance, explicit `cdp_targets`, and active continuation contract.

Missing `cdp_targets` is `ROUTING_HALTED`; the target must not be inferred.

---

## 7. Project-File Boot Set

Keep the following project files current as immutable or slowly changing boot anchors:

- `README_FIRST.md`
- `CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.md`
- `OPS_CANONICAL_INDEX.md`
- `Governance_RetroFuse_v3.3.1.md`
- `AI_Contract_Safepoint_v3.2.json`
- `RetroFuse_SAFEPOINT_SOP_v3.2.md`
- `RetroFuse_SESSION_HANDOFF_SOP_v1.md`
- `RetroFuse_CR_Schemas_v3.1.1.json`
- `RetroFuse_OPS_StartupContract_OPSCOO_v1.md`
- `OPS_Handoff_Pack_v1.4.md`
- `RGA_LANE_AUTHORITY_REGISTRY_v1.json`
- `RGA_CLI_LAUNCHER_CONTRACT_v2.md`
- `OPS_PathRegistry_v1.json`
- required RCD support contracts used for ticket emission

Project files are pointers and hydration anchors. They must not silently outrank newer canonical disk artifacts.

---

## 8. Do Not Load as Current Authority

Do not treat any of the following as current authority unless the canonical index explicitly reclassifies them:

- `Tools\RGA\_boot`
- retired GEN7 roots or artifacts
- stale project copies
- files named `Copy`, backup, old, retired, historical, candidate, or staging-only
- chat transcripts, model memory, DOM history, or uncited summaries
- capsules as runtime or production authority
- Google Drive duplicates not bound by exact identity

---

## 9. Failure Rules

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

## 10. Required Posture

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
