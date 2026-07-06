# OPS_CANONICAL_INDEX.md
## RGA — Canonical Index v2.1 (LAW + POINTERS ONLY)

> **Purpose:** Declare what is authoritative *now* and where it lives.  
> **Non-purpose:** This file does **not** carry runtime “state” (ports/PIDs/health), history, or prose.  
> **Continuity rule:** If an operational change is not recorded in CR-OPS, it is considered non-existent.

---

## Canonical Disk Authority (Authoritative)

This document defines the ONLY authoritative on-disk locations for OPS.

- Any path not explicitly listed here is NON-AUTHORITATIVE.
- AI creation of new roots, alternates, or parallel structures is forbidden.
- If an intended path is not present in this index, the AI MUST halt and request clarification.

Disk truth overrides conversational context, memory, or prior examples.

**GEN7 Status:** RETIRED/HISTORICAL. Active authority lives at `D:\RETROFUSE_OPS\RGA\authority`. Pre-RGA `_BOOT\GEN7` paths are reference-only.

---

## 0) Continuity Rule (Hard)

- Disk artifacts are authoritative.
- Chat context / AI memory is non-authoritative and disposable.
- If any required artifact is missing or unverifiable → **HALT** (no inference).

---

## 1) Authoritative Roots (OPS)

- **OPS Root:** `D:\RETROFUSE_OPS`
- **RGA Authority Root:** `D:\RETROFUSE_OPS\RGA\authority`
- **Registry Root:** `D:\RETROFUSE_OPS\Registry\OPS_COO`
- **Logs Root:** `D:\RETROFUSE_OPS\Logs`
- **Status Root:** `D:\RETROFUSE_OPS\Status`
- **RCD Root:** `D:\RETROFUSE_OPS\Tools\RCD`

---


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
- **Rule:** Read on startup for bounded orientation. Does not modify DNS, deploy, tunnel, or live hosting behavior. Does not override OPS_CANONICAL_INDEX.md for path authority.## 2) Boot Authority Order (Binding)

1. `README_FIRST.md` (orientation only)
2. `RetroFuse_SAFEPOINT_SOP_v3.2` (process law)
3. `Governance v3.3.0 + AI Contract v3.2` (authority)
4. `OPS COO Startup Contract` (role binding)
5. `OPS_CANONICAL_INDEX.md` (authoritative path resolution)

If any of the above is missing → **HALT: MISSING_ARTIFACTS**

---

## 3) Canonical Boot Artifacts (Explicit Paths)

### 3.1 README_FIRST (Orientation Only)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\README_FIRST.md`
- **Authority:** Orientation only (non-authoritative)

### 3.2 SAFEPOINT SOP v3.2 (Process Law)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_SAFEPOINT_SOP_v3.2.md`
- **Authority:** Binding process law

### 3.3 Governance v3.3.0 (System Authority)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\Governance_RetroFuse_v3.3.0.md`
- **Authority:** Binding

### 3.4 AI Contract v3.2 (AI Constraints)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\AI_Contract_Safepoint_v3.2.json`
- **Authority:** Binding AI constraints

### 3.5 CR Schemas v3.1.1 (Schema Authority)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\RetroFuse_CR_Schemas_v3.1.1.json`
- **Authority:** Binding Schema reference for CR generation/verification

### 3.6 OPS COO Startup Contract (Role Binding)
- **Path:** `D:\RETROFUSE_OPS\_BOOT\GEN7\RetroFuse_OPS_StartupContract_OPSCOO_v1.md` 
- **Authority:** Role binding (OPS COO)

---

## 4) Operational Modules (Authoritative Locations)

### 4.1 GEN7 Operations Kernel
- **Path:** `D:\RETROFUSE_OPS\_BOOT\GEN7\Gen7_Operations_Kernel_v1.3.md`
- **Authority:** GEN7 operational kernel (guidance + constraints)

### 4.2 OPS Handoff Pack (Reorientation Capsule)
- **Path:** `D:\RETROFUSE_OPS\RGA\authority\OPS_Handoff_Pack_v1.4.md`
- **Authority:** Required for clean OPS-level resumption

### 4.3 Render DailyCheck (Human Readable)
- **Path:** `D:\RETROFUSE_OPS\MODULES\Render_DailyCheck_To_MD.ps1`
- **Authority:** Renders DailyCheck JSON (non-destructive)

### 4.4 RGA Governance Assembler (Authorized Target)
- **Executable Target:** `D:\RETROFUSE_OPS\Tools\RGA` (not yet created — authorized target for migration)
- **Current Holding:** `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\rga` (MVP/prototype, untracked in Bolt git)
- **Ownership:** OPS-owned cross-cutting governance assembler
- **Status:** `AUTHORIZED_TARGET_NOT_YET_MIGRATED`
- **Git Boundary:** Standalone git repo after scaffold/copy validation
- **Bolt Fallback:** Preserved until post-migration validation
- **Rule:** RGA is an OPS tool, not a Bolt tool. Bolt may call RGA; Bolt does not own RGA. Migration must be curated and clean, not a dump of every prototype receipt.

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

### 7.3 OPS Capsules
- Path: `D:\RETROFUSE_OPS\_Capsules\`
- Rolling/current: `CAPSULE_OPS_CURRENT.md` (append-only)
- Sealed: `CAPSULE_OPS_YYYYMMDD_YYYYMMDD.md` (optional; if used)

### 7.4 Project Capsules
- Path convention: `<ProjectRoot>\_Capsules\`
- Rolling/current: `CAPSULE_<ProjectKey>_CURRENT.md` (append-only)
- Sealed: `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD.md`
  - Collision: `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD__HHMMSS.md`

### 7.5 Truth checkpoint / Resume rule
- Load capsule first (OPS or Project).
- Then apply only deltas after the capsule EncapsulationTimestamp:
  - OPS: OPS CR + OPS Ledger deltas
  - Project: project CR deltas (no project ledger)

---


### 7.6 Project BLUEPRINT Discovery Convention
- **Convention:** Each governed project root may declare a `BLUEPRINT.md` with a JSON header.
- **Discovery:** Walk up from current directory to find `BLUEPRINT.md`; parse JSON header.
- **Authority:** Project BLUEPRINTs are authoritative for project-local paths only.
- **Rule:** Project BLUEPRINTs do not override OPS_CANONICAL_INDEX.md. If conflict exists, OPS_CANONICAL_INDEX.md wins.

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

- RetroFuse_OPS_COO_Ledger_DailyOpen:
  Execute: powershell.exe
  Args:    -NoProfile -ExecutionPolicy Bypass -File D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_Ledger_Today.ps1
- RetroFuse_OPS_COO_Ledger_DayOpen_OnLogon:
  Execute: powershell.exe
  Args:    -NoProfile -ExecutionPolicy Bypass -File D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_Ledger_Today.ps1
- RetroFuse_OPS_COO_CR_DailyOpen:
  Execute: powershell.exe
  Args:    -NoProfile -ExecutionPolicy Bypass -File "D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_CR_Today.ps1"
- RetroFuse_OPS_COO_CR_DayOpen_OnLogon:
  Execute: powershell.exe
  Args:    -NoProfile -ExecutionPolicy Bypass -File "D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\Ensure_OPS_COO_CR_Today.ps1"

### 8.9 Triggers (IMPLEMENTATION — NON-AUTHORITY)

- RetroFuse_OPS_COO_Ledger_DailyOpen: Daily @ 04:05 (StartBoundary 2025-12-29T04:05:00)
- RetroFuse_OPS_COO_CR_DailyOpen:     Daily @ 04:05 (StartBoundary 2025-12-29T04:05:00)
- RetroFuse_OPS_COO_Ledger_DayOpen_OnLogon: OnLogon (StartBoundary 2025-12-29T13:48:00)
- RetroFuse_OPS_COO_CR_DayOpen_OnLogon:     OnLogon (StartBoundary 2025-12-29T13:48:00)

Hard Rule:
- If any path in this module is unknown or changed: output UNKNOWN_PATH and ASK. Never infer.

---

## 9) Runtime / State (Explicitly Non-Authority)

Runtime state (ports, PIDs, watcher status, health checks, “latest DailyCheck”) is **not authority**.

### Canonical locations for state outputs:
- **RFCC Status Root:** `D:\RETROFUSE_OPS\Status\RFCC`
- **Example DailyCheck JSON (non-authoritative state):** `D:\RETROFUSE_OPS\Status\RFCC\DailyCheck_*.json`
- **Dashboard Root (implementation, not authority):** `D:\RETROFUSE_OPS\Dashboard`
- **Dashboard server:** `D:\RETROFUSE_OPS\Dashboard\server.py`

---

## 10) Artifact State Semantics (OPS)

OPS artifacts are classified as:

- **ACTIVE** — execution authority (tools, watchers, gates)
- **FROZEN** — reference-stable (review permitted; execution not implied)
- **HISTORICAL** — archival continuity (never used to veto GEN7 actions)

GEN7 boot artifacts supersede execution guidance from earlier generations.

---

## 11) Change Control (Hard)

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

## 12) Seal Footer (Optional; Informational)

Artifact: `OPS_CANONICAL_INDEX.md`  
Canonical Path: `D:\RETROFUSE_OPS\RGA\authority\OPS_CANONICAL_INDEX.md`  
Status: Append-only (may be sealed via tooling; sealing does not change authority order)







