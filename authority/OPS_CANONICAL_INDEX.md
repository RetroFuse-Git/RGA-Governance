# OPS_CANONICAL_INDEX.md
## RGA -- Canonical Index v2.2 (LAW + POINTERS ONLY)

> **Purpose:** Declare what is authoritative *now* and where it lives.  
> **Non-purpose:** This file does **not** carry runtime "state" (ports/PIDs/health), history, or prose.  
> **Continuity rule:** If an operational change is not recorded in CR-OPS, it is considered non-existent.

---

## Canonical Disk Authority (Authoritative)

This document defines the ONLY authoritative on-disk locations for OPS.

- Any path not explicitly listed here is NON-AUTHORITATIVE.
- AI creation of new roots, alternates, or parallel structures is forbidden.
- If an intended path is not present in this index, the AI MUST halt and request clarification.

Disk truth overrides conversational context, memory, or prior examples.

---

## 0) Continuity Rule (Hard)

- Disk artifacts are authoritative.
- Chat context / AI memory is non-authoritative and disposable.
- If any required artifact is missing or unverifiable -> **HALT** (no inference).

---

## 1) Authoritative Roots (OPS)

- **OPS Root:** `D:\RETROFUSE_OPS`
- **RGA Authority Root:** `D:\RETROFUSE_OPS\RGA\authority`
- **Registry Root:** `D:\RETROFUSE_OPS\Registry\OPS_COO`
- **Logs Root:** `D:\RETROFUSE_OPS\Logs`
- **Status Root:** `D:\RETROFUSE_OPS\Status`
- **RCD Root:** `D:\RETROFUSE_OPS\Tools\RCD`
- **RGA Receipt Root:** `D:\RETROFUSE_OPS\RGA\receipts`

### 1.6 OPS BLUEPRINT Contract
- **Path:** `D:\RETROFUSE_OPS\BLUEPRINT.md`
- **Authority:** Workspace startup contract declaring workspace_root, project_paths, lane, authority, continuity_role, and escalation_paths.
- **Rule:** Read on startup for bounded orientation. Does not override OPS_CANONICAL_INDEX.md for path authority.

### 1.7 OPS_COO BLUEPRINT Contract
- **Path:** `D:\RETROFUSE_OPS\Registry\OPS_COO\BLUEPRINT.md`
- **Authority:** Registry sub-workspace startup contract. Inherits CR/Ledger semantics from OPS.
- **Rule:** Read on startup for bounded orientation. Subordinate to OPS BLUEPRINT and OPS_CANONICAL_INDEX.md.

### 1.8 RetroFuse.net BLUEPRINT Contract
- **Path:** `D:\PORTTORETRO_ARCHIVE\PROJECTS\RetroFuse.net\BLUEPRINT.md`
- **Authority:** Active live website project startup contract. Declares workspace_root, project_paths, hosting method (Cloudflare Tunnel to localhost:8080), public domains (retrofuse.net, www.retrofuse.net), and git remote (RetroFuse-Git/RetroFuse.net.git).
- **Rule:** Read on startup for bounded orientation. Does not modify DNS, deploy, tunnel, or live hosting behavior. Does not override OPS_CANONICAL_INDEX.md for path authority.

### 1.9 RGA Receipt Root (Authorized)
- **Path:** `D:\RETROFUSE_OPS\RGA\receipts`
- **Authority:** Append-only boot and admission receipts. Created by RGA_Authority_Bootloader.ps1.
- **Rule:** Receipt files are operational evidence, not authority. They do not override governance, manifest, or canonical index.

### 1.10 RGA Provider Capability State (Authorized)
- **Path:** `D:\RETROFUSE_OPS\Registry\OPS_COO\State\RGA_PROVIDER_CAPABILITY_REGISTRY_v1.json`
- **Authority:** Operational state tracking provider availability and capabilities. Does not define lane authority (see RGA_LANE_AUTHORITY_REGISTRY_v1.json).
- **Rule:** Update when provider availability changes. Does not require governance amendment.

## 2) Boot Authority Order (Binding)

This section is the sole authority for boot order. All other documents reference it; none redefine it.

1. `README_FIRST.md` (orientation only)
2. `RetroFuse_SAFEPOINT_SOP_v3.2` (process law)
3. `RetroFuse_SESSION_HANDOFF_SOP_v1` (session hydration and handoff)
4. `Governance v3.3.1 + AI Contract v3.2` (authority)
5. `OPS COO Startup Contract` (role binding)
6. `OPS_CANONICAL_INDEX.md` (authoritative path resolution)

If any of the above is missing -> **HALT: MISSING_ARTIFACTS**

---

## 3) Canonical Boot Artifacts (Explicit Paths)

### 3.1 README_FIRST (Orientation Only)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\README_FIRST.md`
- **Authority:** Orientation only (non-authoritative)

### 3.2 SAFEPOINT SOP v3.2 (Process Law)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_SAFEPOINT_SOP_v3.2.md`
- **Authority:** Binding process law

### 3.2b SESSION HANDOFF SOP v1 (Session Lifecycle)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_SESSION_HANDOFF_SOP_v1.md`
- **Authority:** Binding session hydration, resumption, and retirement rules
- **Rule:** Every project root MUST contain a `plan.md`. Every session MUST read it first. No session may restart completed work or retire without updating the plan.

### 3.3 Governance v3.3.1 (System Authority)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\Governance_RetroFuse_v3.3.1.md`
- **Authority:** Binding

### 3.4 AI Contract v3.2 (AI Constraints)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\AI_Contract_Safepoint_v3.2.json`
- **Authority:** Binding AI constraints

### 3.5 CR Schemas v3.1.1 (Schema Authority)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_CR_Schemas_v3.1.1.json`
- **Authority:** Binding Schema reference for CR generation/verification

### 3.6 OPS COO Startup Contract (Role Binding)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_OPS_StartupContract_OPSCOO_v1.md` 
- **Authority:** Role binding (OPS COO)

---

## 4) Operational Modules (Authoritative Locations)


### 4.1 OPS Handoff Pack (Reorientation Capsule)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\OPS_Handoff_Pack_v1.4.md`
- **Authority:** Required for clean OPS-level resumption

### 4.2 Render DailyCheck (Human Readable)
- **Path:** `D:\RETROFUSE_OPS\MODULES\Render_DailyCheck_To_MD.ps1`
- **Authority:** Renders DailyCheck JSON (non-destructive)

### 4.3 RGA Governance Assembler
- **Status:** MIGRATION_COMPLETE
- **Canonical Path:** `D:\RETROFUSE_OPS\Tools\RGA`
- **Git Remote:** `https://github.com/RetroFuse-Git/RGA.git`
- **Bolt Fallback:** `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\rga` -- empty (holding pen cleared)
- **Rule:** RGA is an OPS tool, not a Bolt tool. Bolt may call RGA; Bolt does not own RGA.

---

## 5) Continuity Records (Append-Only)

### 5.1 OPS COO Ledger (Append-Only Log of Record)
- **Folder:** `D:\RETROFUSE_OPS\Registry\OPS_COO\Ledger\`
- **Convention:** `OPS_COO_Ledger_YYYY-MM-DD.md`
- **Authority:** Disk truth for operational events and integrity evidence

### 5.2 CR-OPS (Daily Continuity Records)
- **Folder:** `D:\RETROFUSE_OPS\Registry\OPS_COO\CR_OPS\`
- **Convention:** `CR_OPS_YYYY-MM-DD.md` *(single file per day; append-only)*
- **Authority:** Mandatory continuity record for any operational wiring change  
- **Rule:** Creating multiple CR files per day is non-standard; correct is **one** daily file.

## 6) Continuity Record Cadence (Authoritative)

OPS uses exactly ONE Continuity Record (CR) per calendar day.

- CR files are named: `CR_OPS_YYYY-MM-DD.md`
- All OPS continuity events for that day MUST be appended to the same file.
- Creating multiple CR files for the same date is forbidden.
- If a CR file for the current date exists, the AI MUST append to it.

If uncertainty exists, the AI MUST locate the existing CR before proceeding.

## 7) Continuity Locations (Canonical)

### 7.1 OPS Ledger (single sink)
- Path: `D:\RETROFUSE_OPS\Registry\OPS_COO\Ledger\`
- Rule: OPS Ledger is the ONLY ledger.
- Project reporting: every project event/status MUST be tagged, e.g. `[PROJECT:<ProjectKey>]`.

### 7.2 OPS CR (append-only daily record)
- Path: `D:\RETROFUSE_OPS\Registry\OPS_COO\CR_OPS\`
- Naming: `CR_OPS_YYYY-MM-DD.md` (append-only)

### 7.3 Project CRs (append-only change stream)
- Path convention: `<ProjectRoot>\CR\`
- Rolling/current: `CR_<ProjectKey>_CURRENT.md` (append-only)
- Rule: One active append-only CR per project or declared project change stream. Do not create one CR per ticket.
- Project CRs record project-local continuity deltas only. They do not replace OPS CR or OPS Ledger.
- If project work crosses OPS/RGA/RCD authority boundary, emit OPS_CAPTURE_REQUIRED handoff or route to OPS/RGA intake per existing authority.
- Projects have no project ledger; OPS Ledger is the ONLY ledger (S7.1).
- Resume: load project capsule first (S7.6), then apply project CR deltas after capsule EncapsulationTimestamp.

### 7.4 OPS Capsules
- Path: `D:\RETROFUSE_OPS\_Capsules\`
- Rolling/current: `CAPSULE_OPS_CURRENT.md` (append-only)
- Sealed: `CAPSULE_OPS_YYYYMMDD_YYYYMMDD.md` (optional; if used)

### 7.5 Project Capsules
- Path convention: `<ProjectRoot>\_Capsules\`
- Rolling/current: `CAPSULE_<ProjectKey>_CURRENT.md` (append-only)
- Sealed: `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD.md`
  - Collision: `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD__HHMMSS.md`

### 7.6 Truth checkpoint / Resume rule
- Load capsule first (OPS or Project).
- Then apply only deltas after the capsule EncapsulationTimestamp:
  - OPS: OPS CR + OPS Ledger deltas
  - Project: project CR deltas (no project ledger)

---

### 7.7 Project BLUEPRINT Discovery Convention
- **Convention:** Each governed project root may declare a `BLUEPRINT.md` with a JSON header.
- **Discovery:** Walk up from current directory to find `BLUEPRINT.md`; parse JSON header.
- **Authority:** Project BLUEPRINTs are authoritative for project-local paths only.
- **Rule:** Project BLUEPRINTs do not override OPS_CANONICAL_INDEX.md. If conflict exists, OPS_CANONICAL_INDEX.md wins.

---

## 8) SAFEPOINT Intake & Engine Wiring (Authoritative Pointers)

### 8.1 Pickup Root (Inbound)
- **Pickup:** `C:\Users\Portt\Downloads`
- **Rule:** SAFEPOINTs arrive as ZIP archives here.

### 8.2 Engine Drop Root (Filed by Project)
- **Engine SAFEPOINTS Root:** `D:\PORTTORETRO_ARCHIVE\SAFEPOINT_ENGINE\SAFEPOINTS\<project>`
- **Rule:** Project naming must resolve to canonical folders (aliases allowed; see Path Registry).

### 8.3 Quarantine Root (Rare; investigate immediately)
- **Quarantine Root:** `D:\PORTTORETRO_ARCHIVE\SAFEPOINT_ENGINE\quarantine\`
- **Rule:** Quarantine is exceptional; do not normalize it.

### 8.4 Engine Watcher Task (Scheduled)
- **TaskName:** `PorttoRetro_Safepoint_Intake`
- **Exec:** `powershell.exe`
- **Args:** `-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "D:\PORTTORETRO_LIBRARY\System\Safepoint_Watcher_Intake_v3.ps1"`
- **Authority:** This scheduled task is the canonical inbound SAFEPOINT ingestion mechanism.

### 8.5 OPS Path Registry (Routing Truth)
- **Path:** `D:\RETROFUSE_OPS\Registry\OPS_COO\State\OPS_PathRegistry_v1.json`
- **Purpose:** Canonical routing for SAFEPOINT intake, engine, quarantine, and aliases.
- **Authority:** Deterministic filesystem routing; referenced at boot.

### 8.6 ScriptPaths:
- D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_Ledger_Today.ps1
- D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_CR_Today.ps1

### 8.7 ScheduledTasks
- TaskPath: `\`; Name: `RetroFuse_OPS_COO_Ledger_DailyOpen`
- TaskPath: `\`; Name: `RetroFuse_OPS_COO_Ledger_DayOpen_OnLogon`
- TaskPath: `\`; Name: `RetroFuse_OPS_COO_CR_DailyOpen`
- TaskPath: `\`; Name: `RetroFuse_OPS_COO_CR_DayOpen_OnLogon`

### 8.8 TaskActions (Execute + Args):
- RetroFuse_OPS_COO_Ledger_DailyOpen: Execute: powershell.exe, Args: -NoProfile -ExecutionPolicy Bypass -File D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_Ledger_Today.ps1
- RetroFuse_OPS_COO_Ledger_DayOpen_OnLogon: Execute: powershell.exe, Args: -NoProfile -ExecutionPolicy Bypass -File D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_Ledger_Today.ps1
- RetroFuse_OPS_COO_CR_DailyOpen: Execute: powershell.exe, Args: -NoProfile -ExecutionPolicy Bypass -File "D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_CR_Today.ps1"
- RetroFuse_OPS_COO_CR_DayOpen_OnLogon: Execute: powershell.exe, Args: -NoProfile -ExecutionPolicy Bypass -File "D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_CR_Today.ps1"

### 8.9 Triggers (IMPLEMENTATION -- NON-AUTHORITY)
- RetroFuse_OPS_COO_Ledger_DailyOpen: Daily @ 04:05 (StartBoundary 2025-12-29T04:05:00)
- RetroFuse_OPS_COO_CR_DailyOpen:     Daily @ 04:05 (StartBoundary 2025-12-29T04:05:00)
- RetroFuse_OPS_COO_Ledger_DayOpen_OnLogon: OnLogon (StartBoundary 2025-12-29T13:48:00)
- RetroFuse_OPS_COO_CR_DayOpen_OnLogon:     OnLogon (StartBoundary 2025-12-29T13:48:00)

Hard Rule:
- If any path in this module is unknown or changed: output UNKNOWN_PATH and ASK. Never infer.

---

## 9) Canonical Toolchain Registry

All canonical tools are listed below with exact paths, purpose, invocation guidance, and prohibited substitutes. The machine-readable registry lives at `RGA_CANONICAL_TOOLCHAIN_REGISTRY_v1.json`.

### 9.1 RGA Authority Bootloader
- **Path:** `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\RGA_Authority_Bootloader.ps1`
- **Purpose:** Verify RGA authority artifacts and initialize daily truth anchors.
- **Invocation:** `& "D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\RGA_Authority_Bootloader.ps1"`
- **Prohibited:** Do not reimplement manifest hashing, artifact verification, or trust-anchor validation.

### 9.2 RGA Authority Admission
- **Path:** `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Invoke-RGAAuthorityAdmission.ps1`
- **Purpose:** Admit, preview, or roll back RGA authority artifacts. Handles manifest amendment, sidecar hash updates, and consumer rewiring.
- **Invocation:** `Invoke-RGAAuthorityAdmission.ps1 -Mode Preview` or `-Mode Admit`
- **Prohibited:** Do not manually edit RGA_BOOT_MANIFEST.json or RGA_BOOT_MANIFEST.sha256.

### 9.3 RCD Conductor (Cross-Lane Routing — Single Canonical Entry Point)
- **Path:** `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDConductor.ps1`
- **Purpose:** Dynamic multi-round orchestration. Reads ticket, runs pre-flight, runs preamble guard, routes to ExchangeRound or ChainLoop. Write a ticket with CDP_TARGETS and invoke the Conductor for all cross-lane CDP delivery.
- **Invocation:** `Invoke-RCDConductor.ps1 -PayloadPath <ticket.txt>`
- **Prohibited:** Do not implement new page discovery, nonce correlation, bridge invocation, or readback logic. Do not call inject_and_observe functions directly from non-canonical scripts.

### 9.4 RCD ExchangeRound (CDP Dispatch Primitive)
- **Path:** `D:\RETROFUSE_OPS\Tools\RCD\Tools\Invoke-RCDExchangeRound.ps1`
- **Purpose:** One CDP exchange round — inject, observe, classify, write receipt. Supports chatgpt, gemini, and deepseek targets.
- **Invocation:** Called by the Conductor. For standalone use: `Invoke-RCDExchangeRound.ps1 -Mode handoff -PayloadInline <text> -CdpTargets @("deepseek") -WaitSec 60`

### 9.5 RCD CDP Bridge (Last-Mile Transport)
- **Path:** `D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD\Tools\bridge\rcd_cdp_return.py`
- **Purpose:** Python CDP WebSocket bridge used by ExchangeRound. Exports inject_and_observe_response, inject_and_observe_gemini_response, inject_and_observe_deepseek_response.
- **Invocation:** Called by ExchangeRound via Invoke-RCDFileBackedPython. Do not call directly from non-canonical scripts.
- **Prohibited:** Do not import or call bridge functions directly from outside the RCD Tools tree.

### 9.6 Context Cache Builder
- **Path:** `D:\RETROFUSE_OPS\ContextCache\Build-RCDContextCache.ps1`
- **Purpose:** Validate RGA authority, Daily Bundle, and Cold Lane before building context cache. Publishes cache + manifest + Drive replication.
- **Invocation:** `& "D:\RETROFUSE_OPS\ContextCache\Build-RCDContextCache.ps1"` or with `-Force`

### 9.7 DeepSeek Cache Startup (Conductor Consumer, NOT a Replacement)
- **Path:** `D:\RETROFUSE_OPS\ContextCache\Invoke-DeepSeekCacheStartup.ps1`
- **Purpose:** Orchestrates RGA boot, cache build, page discovery, and Conductor invocation for DeepSeek cache hydration.
- **Invocation:** `& "D:\RETROFUSE_OPS\ContextCache\Invoke-DeepSeekCacheStartup.ps1"` or with `-SkipDelivery`
- **Rule:** This script is a consumer of the Conductor, not a replacement. It may be superseded by direct Conductor invocation patterns.

### 9.8 Bolt Wrapper (Copilot/Codex/Claude Lanes)
- **Path:** `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\bolt-copilot.ps1`
- **Purpose:** Governed CLI wrapper for Copilot lane with cache-startup integration.
- **Invocation:** See `Bolt_CLI_Shortcuts.ps1` for bc/bcw/bcp/bcpw etc.

### 9.9 RCD CDP Handoff GUI
- **Path:** `D:\RETROFUSE_OPS\Tools\RCD\Tools\RCD_CDP_Handoff_GUI.ps1`
- **Purpose:** Operator WPF GUI for CDP handoff and browser management across all three provider lanes.

---

## 10) Runtime / State (Explicitly Non-Authority)

Runtime state (ports, PIDs, watcher status, health checks, "latest DailyCheck") is **not authority**.

### Canonical locations for state outputs:
- **RFCC Status Root:** `D:\RETROFUSE_OPS\Status\RFCC`
- **Example DailyCheck JSON (non-authoritative state):** `D:\RETROFUSE_OPS\Status\RFCC\DailyCheck_*.json`
- **Dashboard Root (implementation, not authority):** `D:\RETROFUSE_OPS\Dashboard`
- **Dashboard server:** `D:\RETROFUSE_OPS\Dashboard\server.py`

---

## 11) Artifact State Semantics (OPS)

OPS artifacts are classified as:

- **ACTIVE** -- execution authority (tools, watchers, gates)
- **FROZEN** -- reference-stable (review permitted; execution not implied)
- **HISTORICAL** -- archival continuity (never used to veto active operations)

RGA governance artifacts supersede pre-RGA execution guidance.

---

## 12) Change Control (Hard)

- This Canonical Index is **append-only**.
- Any change MUST be recorded in:
  - `CR_OPS_YYYY-MM-DD.md`
  - `OPS_COO_Ledger_YYYY-MM-DD.md` (when integrity evidence needed)

If unsure:
- Identify artifact state (ACTIVE/FROZEN/HISTORICAL)
- Propose a new artifact
- Declare via CR-OPS (or SAFEPOINT when applicable)
- Proceed only after declaration

---

## 13) Seal Footer (Optional; Informational)

Artifact: `OPS_CANONICAL_INDEX.md`  
Canonical Path: `D:\RETROFUSE_OPS\RGA\authority\OPS_CANONICAL_INDEX.md`  
Status: Append-only (may be sealed via tooling; sealing does not change authority order)

---

## 14) Pipeline Architecture (Append-Only Pointers)

### 14.1 RetroFuse Pipeline Architecture v1 (Human-Readable)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_PIPELINE_ARCHITECTURE_v1.md`
- **SHA-256:** `240911C06782CF257429712977BD3EB9347D824B947FFFE8C80ACEE802FD4778`
- **Size:** 34,056 bytes
- **Authority:** Declares end-to-end pipeline architecture.
- **Status:** ACTIVE

### 14.2 RetroFuse Pipeline Registry v1 (Machine-Readable)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_PIPELINE_REGISTRY_v1.json`
- **SHA-256:** `2915D6A375B873204B0CD37AA987AFA603A1626F66C99ECAA891EE4F1C09CE3C`
- **Size:** 34,054 bytes
- **Authority:** Machine-readable canonical registry.
- **Status:** ACTIVE

### 14.3 Plan Discovery (Startup Continuity Step)
- **Rule:** After authority hydration (Section 2) and before any mutation, discover the nearest plan.md as primary active-work state.
- **Algorithm:** Walk upward from working directory to nearest governed project root. Load nearest plan.md as primary. Load enclosing workspace plan.md only as supplemental cross-project context. Never allow workspace plan to replace project-local plan.
- **Missing fixture rule:** If no applicable plan exists, classify PLAN_NOT_FOUND. Do not fabricate.
- **Test cases:**
  - `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools` -> `Bolt\plan.md` primary, `PROJECTS\plan.md` supplemental
  - `D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD\Tools\bridge` -> `RCD\plan.md` primary, `PROJECTS\plan.md` supplemental
  - `D:\RETROFUSE_OPS\Registry\OPS_COO\Tools` -> `OPS\plan.md` primary, null supplemental

---

## 15) Missing Artifact Protocol

The following RCD support artifacts are not present in the authority root. They are located at their canonical operational paths under `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\`:
- RCD-CLI-ROUTING-CONTRACT (v1.2): `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CLI-ROUTING-CONTRACT-v1.2.md`
- RCD-CROSSLANE-ENVELOPE (v3.1): `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CROSSLANE-ENVELOPE-v3.1.md`
- RCD-TICKET-GATE (Phase 7 SEALED): `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-TICKET-GATE-V2-PHASE7-ROUND-MODE-SPEC.md`
- RCD-FEEDBACK-ATTACHMENT-RULES: `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-FEEDBACK-ATTACHMENT-RULES-v1.md`
- MINI_UNITY_FEEDBACK_LOOP_AMENDMENT: `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\MINI_UNITY_FEEDBACK_LOOP_AMENDMENT.md`
- RCD_MINI_UNITY_DATA_GATHERING_METHOD: `D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD_MINI_UNITY_DATA_GATHERING_METHOD_v1.md`

These are operational contracts, not governance authority. Their absence from the authority root is expected and correct.

---

## 16) Precedence Order (Binding)

When authority artifacts conflict, precedence is:

1. Human operator (session-valid override only; must be captured to CR/Ledger for persistence)
2. Governance_RetroFuse_v3.3.1
3. RetroFuse_SAFEPOINT_SOP_v3.2
4. AI_Contract_Safepoint_v3.2
5. RetroFuse_CR_Schemas_v3.1.1
6. OPS_CANONICAL_INDEX.md (path authority)
7. RetroFuse_OPS_StartupContract_OPSCOO_v1.md (role binding)
8. All other operational contracts (Handoff Pack, Pipeline Architecture, RCD contracts)

Higher precedence wins. This section is the sole authority for precedence order. All other documents reference it; none redefine it.
---

## RCD Ticket Contract Authority

**Canonical index:** RCD_TICKET_CONTRACT\RCD_TICKET_CONTRACT_INDEX.md
**Status:** INSTALLED_NOT_ACTIVATED
**Rule:** RGA defines the normative ticket contract. RCD validates and executes. This family defines the authoritative ticket format. Runtime admission continues on the legacy path until Ticket 4 validator activation.

### 1.9 ChatGPT Hybrid-Hydration Bootstrap
- **Path:** D:\RETROFUSE_OPS\RGA\authority\CHATGPT_HYBRID_HYDRATION_BOOTSTRAP_v1.1.md
- **SHA-256:** 958E29B2EDE5D3F93E7481FE1242088FE409579D2BEA7BBD13C89945FB52C4DB
- **Authority:** Subordinate ChatGPT hydration gate (NOT BOOT_CRITICAL)
- **Load placement:** After full authority boot, before Conductor continuation responses
- **Rule:** Resolves Drive-based authority-response contract and Daily Bundle pointer. Does not override OPS_CANONICAL_INDEX.md, SAFEPOINT SOP, Session Handoff SOP, or full authority boot order.

## 17) Plan Authority and Retention Contract (Registered R04)

- **Status:** ACTIVE (registered by OPS-20260801-GOVERNOR-UNITY-TRANSPARENCY-AND-CONTINUITY-REPAIR-004-R04)
- **Contract path:** D:\RETROFUSE_OPS\Registry\OPS_COO\Policy\OPS_PlanAuthorityAndRetentionContract_v1.md
- **Contract SHA-256:** 23A6F1BAAF8EE43F0AF9C604FE8709C0FE02161B40C2D4E950D8BD1AB6198F1B
- **Role:** Defines bounded plan roles, ownership, retention/compaction thresholds, immutable snapshots, and closeout-reference format.
- **Binding rule:** No plan.md is globally canonical. No plan acquires OPS or all-project authority by implication. Plans do not outrank OPS_CANONICAL_INDEX, BLUEPRINT, CR, Ledger, Capsule, Receipt, or Commit.
- **Per-plan roles:** PROJECTS\plan.md = WORKSPACE_COORDINATION; Tools\plan.md / RCD\plan.md / Bolt\plan.md = PROJECT_LOCAL; OPS root plan.md = NONAUTHORITATIVE_HISTORICAL (frozen pending R05 disposition).
- **Retention thresholds:** Warning 30KB/300 lines; mandatory compaction 50KB/500 lines.
- **Precedence note:** This registration is a discoverability pointer. It does not grant global plan authority and does not amend boot order.
