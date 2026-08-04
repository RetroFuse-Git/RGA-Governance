# OPS Handoff Pack v1.4 -- RGA/RCD Operations Re-entry

**Status:** Authoritative handoff
**Scope:** RGA-governed, RCD-operated OPS continuity
**Date:** 2026-07-16 -- RGA cutover revision
**Supersedes:** OPS_Handoff_Pack_v1.3

---

## 0. Purpose (Read First)

This document is the authoritative OPS handoff pack for cold-lane rehydration, successor AI resumption, and operator re-entry under RGA governance with RCD operational support.

Authority artifacts, paths, and boot law are resolved by the current RGA-aligned `OPS_CANONICAL_INDEX.md` and `RetroFuse_OPS_StartupContract_OPSCOO_v1.md`.

This handoff answers:
- What authority stack governs OPS
- What rehydration anchors to load
- What actions are allowed and forbidden
- How to resume safely without inference
- How RCD/CDP tools support operations

## 1. Authority Boundary

All OPS actions are bound by the active authority stack. Boot order is declared solely by `OPS_CANONICAL_INDEX.md` Section 2. The following is the current authority boundary:

1. Governance_RetroFuse_v3.3.1.md -- system authority
2. AI_Contract_Safepoint_v3.2.json -- AI constraints
3. RetroFuse_SAFEPOINT_SOP_v3.2.md -- SAFEPOINT process law
4. RetroFuse_CR_Schemas_v3.1.1.json -- CR schema
5. OPS_CANONICAL_INDEX.md -- authoritative path resolution + boot order
6. RetroFuse_OPS_StartupContract_OPSCOO_v1.md -- role binding
7. OPS_Handoff_Pack_v1.4.md -- this document
8. RGA_LANE_AUTHORITY_REGISTRY_v1.json -- lane authority

If any required authority artifact is missing or conflicting -> HALT: MISSING_ARTIFACTS or AUTHORITY_CONFLICT.

## 2. Authority State (Current)

- **RGA (RetroFuse Governance Authority):** ACTIVE -- canonical root `D:\RETROFUSE_OPS\RGA\authority`
- **RCD (RetroFuse Command Desk):** ACTIVE -- `D:\RETROFUSE_OPS\Tools\RCD`
- **Tools\RGA\_boot:** ARCHIVED -- not active authority

## 3. OPS Rehydration Order

Proceed in this exact order after authority stack load:

1. Confirm RGA authority root is present: `D:\RETROFUSE_OPS\RGA\authority`
2. Confirm CUTOVER_RECEIPT.json is present: `D:\RETROFUSE_OPS\RGA\CUTOVER_RECEIPT.json`
3. Load RGA_BOOT_MANIFEST.json for artifact integrity verification
4. Discover and read plan.md from the nearest governed project root (READ FIRST, ACT SECOND per Session Handoff SOP)
5. Confirm RCD health check: `Invoke-RCDHealthCheck.ps1`
   - PASS -> proceed
   - WARN -> proceed with caution logged
   - FAIL -> HALT (CDP bridge not operational)
6. Load CR/Ledger as append-only recording surfaces when required by current authority
7. Run `OpsCOO_Bootstrap.ps1` only if declared by Canonical Index or explicit operator instruction
8. Report: --OPS BOOTSTRAP COMPLETE--

## 4. Operational Surfaces

| Surface | Path | Role |
|---|---|---|
| RGA Governance | `D:\RETROFUSE_OPS\RGA` | Authority root |
| RCD Command Desk | `D:\RETROFUSE_OPS\Tools\RCD` | CDP, exchange, health, templates |
| Bolt | `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt` | Launcher/controller surface |
| Registry (OPS_COO) | `D:\RETROFUSE_OPS\Registry\OPS_COO` | CR/Ledger/Policy |
| SAFEPOINT Engine | `D:\PORTTORETRO_ARCHIVE\SAFEPOINT_ENGINE` | SAFEPOINT intake |
| ModelRouting | `D:\RETROFUSE_OPS\Tools\ModelRouting` | Local model routing |

## 5. Re-entry Aids (RCD)

The following RCD tools are available for governed re-entry:

- **Handoff Desk Templates:** `chatgpt_authority_lane`, `gemini_mechanics_lane`, `deepseek_reasoning_lane`
- **Clone Builder:** `package_builder.py --clone-session`
- **Template Refresh:** `handoff_templates.py --refresh <template_id>`
- **Health Check:** `Invoke-RCDHealthCheck.ps1`
- **CDP Bridge Route:** `D:\RETROFUSE_OPS\CDP_BRIDGE_ROUTE.md`
- **Canonical Map:** `D:\RETROFUSE_OPS\CDP_CANONICAL_MAP.md`

All RCD tools are subordinate to RGA authority. Handoff templates provide role-specific capsules; ChatGPT remains sole authority/final seal lane.

## 6. CDP Multi-Lane Governance

The CDP feedback loop is AUTHORIZED for governed multi-lane exchange:
- CLI is sole routing/aggregation authority
- Models may NOT self-route
- ChatGPT is authority/QC/final seal
- Gemini and DeepSeek are advisory lanes
- Lane authority is declared by RGA_LANE_AUTHORITY_REGISTRY_v1.json
- Cross-lane contradictions are surfaced, not flattened
- Aggregate verdict gates chain progress

## 7. Prohibited Actions

- No raw transcript cloning
- No board-noise trust
- No inference-based execution
- No cross-lane execution outside governed CDP feedback loop
- No CR/Ledger rewrites
- No governance rewrites
- No claiming PASS without receipts

## 8. Failure Codes

| Code | Meaning |
|---|---|
| MISSING_ARTIFACTS | Required authority file not found |
| AUTHORITY_CONFLICT | Two active authority sources disagree |
| CDP_BRIDGE_DOWN | RCD health check FAIL |
| RGA_ROOT_MISSING | Canonical governance root not found |
| BOOT_ORDER_VIOLATION | Rehydration steps executed out of order |
| RGA_BOOT_MANIFEST_MISSING | Manifest not found or trust anchor mismatch |

## 9. Session-Start Decision Table (Canonical Entry Points)

When starting a task, identify the task type and invoke the exact canonical tool. Do not reimplement.

| Task Type | Canonical Entry Point | Exact Path | Prohibited Substitute |
|---|---|---|---|
| Authority boot | RGA_Authority_Bootloader.ps1 | `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\RGA_Authority_Bootloader.ps1` | Manual manifest hashing or artifact verification |
| Authority file changes | Invoke-RGAAuthorityAdmission.ps1 | `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Invoke-RGAAuthorityAdmission.ps1` | Direct manifest.json edits |
| Cross-lane CDP delivery | Invoke-RCDConductor.ps1 | `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDConductor.ps1` | Direct bridge invocation, custom page discovery, custom readback |
| Browser target discovery and readback | Invoke-RCDConductor.ps1 plus canonical bridge | (same as above) | Custom page enumeration, custom WebSocket code |
| Context cache build | Build-RCDContextCache.ps1 | `D:\RETROFUSE_OPS\ContextCache\Build-RCDContextCache.ps1` | Manual JSON construction, manual hash computation |
| DeepSeek cache startup | Invoke-DeepSeekCacheStartup.ps1 | `D:\RETROFUSE_OPS\ContextCache\Invoke-DeepSeekCacheStartup.ps1` | Direct inject_and_observe_deepseek_response calls |
| CDP bridge probe | Invoke-RCDHealthCheck.ps1 | `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDHealthCheck.ps1` | Manual CDP port scanning, raw WebSocket connections |

**Rule:** If the canonical tool does not satisfy the ticket, halt and emit `CANONICAL_TOOL_CONTRACT_GAP` with evidence. Do not create a parallel implementation.

## 10. Historical

- OPS_Handoff_Pack_v1.3: -- archived, non-authoritative
- All pre-RGA handoff documents should not be loaded as current authority

## 11. Current Operational State (2026-07-26)

### Repository Synchronization

| Repo | HEAD | origin/main | Ahead | Behind | Status |
|------|------|-------------|-------|--------|--------|
| Bolt | 83adb0a | 83adb0a | 0 | 0 | SYNCHRONIZED |
| RCD | 69753a8 | 69753a8 | 0 | 0 | SYNCHRONIZED |

### Operational Disposition

- **Next State:** NORMAL_PRIORITY_QUEUE
- **B48 Normal Path:** REPAIRED (commit 83adb0a, pushed)
- **B49 Fallback Path:** INTACT
- **Nightly Matrix v1 Continuity:** PRESERVED (state SHA-256 52B300E9)
- **All Daily Bundle Maintenance Items:** SEALED and CLOSED
- **Open Tickets:** None

### Sealed Tickets This Session

| Ticket | Disposition | Commit | Push | Seal Round |
|--------|-------------|--------|------|------------|
| MAINT-001 | SEALED (STALE_REPORT) | None | N/A | atm-20260726-115048 |
| MAINT-002 | SEALED (DEFERRED_TO_010) | None | N/A | -- |
| MAINT-003 | SEALED (FALSE_POSITIVE) | None | N/A | -- |
| NM-010 | SEALED (SCHEMA_DISCRIMINATION) | 7127f84 | PUSHED | atm-20260726-145905 |
| MAINT-004 | SEALED (PRE_RUN_SNAPSHOT) | e7b0b6b | PUSHED | atm-20260726-161221 |
| R08 | SEALED (INVOCATION_SUCCESS) | 8e55efb | PUSHED | atm-20260726-120732 |
| Conductor-013 | SEALED (SEALED_RECOGNITION) | 69753a8 | PUSHED | atm-20260726-162927 |
| NM-014 | SEALED (CONTINUATION_FUNCTIONING) | None | N/A | atm-20260726-165309 |
| B48-015 | SEALED (EM_DASH_REPAIR) | 83adb0a | PUSHED | atm-20260726-171806 |
| B48-016 | SEALED (PUSH_AND_CLOSEOUT) | None | 83adb0a | atm-20260726-172248 |
## RCD State Update (2026-07-26 22:45Z)

### Repository Synchronization
| Repo | HEAD | origin/main | Ahead | Behind | Status |
|------|------|-------------|-------|--------|--------|
| Bolt | 83adb0a | 83adb0a | 0 | 0 | SYNCHRONIZED |
| RCD | 77110e6 | 77110e6 | 0 | 0 | SYNCHRONIZED |

### Sealed Tickets
- **T018** (OPS-20260726-SELF-HASHER-AUTHORITY-AND-CONSUMPTION-REVIEW-018): SEALED. Self-hasher review complete. CANONICAL_BUT_PARTIALLY_CONSUMED.
- **T019** (RCD-20260726-TERMINAL-SEAL-CLASSIFIER-MAPPING-REPAIR-019): SEALED. Terminal seal classifier repair. Commit 0dd5dbd.
- **T020** (RCD-20260726-TERMINAL-SEAL-CLASSIFIER-PUSH-AND-CLOSEOUT-020): SEALED. Push complete. RCD synchronized.

### Next Queued
- **T021**: OPS-20260726-RGA-AUTOHASHER-MANIFEST-REPIN-AND-TRUST-BOUNDARY-REPAIR-021. Repin 12 identities, establish detached anchor, correct continuity paths, resolve cutover-lock. QUEUED_NOT_AUTHORIZED_BY_THIS_TICKET.

## RGA State Update (2026-07-26 23:52Z)

### Repository Synchronization
| Repo | HEAD | origin/main | Ahead | Behind | Status |
|------|------|-------------|-------|--------|--------|
| Bolt | 83adb0a | 83adb0a | 0 | 0 | SYNCHRONIZED |
| RCD | 77110e6 | 77110e6 | 0 | 0 | SYNCHRONIZED |
| RGA | 8e09254 | 0d803a5 | 1 | 0 | AHEAD (T021, no push) |

### T021 Complete
- Canonical manifest: 11 tools, SHA 2AF14AC7
- Detached anchor: SHA 2454A0A6. Root anchor: SHA FDC77E1A
- Bootloader: SHA B985538A (canonical), verified smoke PASS
- Feature gate: DISABLED. No production transaction.
- Push: NOT AUTHORIZED

### Next: T021 push authorization when operator ready
