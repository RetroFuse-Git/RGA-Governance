# RetroFuse SAFEPOINT SOP v3.2

Authority: Mandatory  
Scope: All projects, all lanes  
Compatibility: SOP v3.0 and v3.1 SAFEPOINTs remain valid. v3.2 formalizes deterministic SAFEPOINT scope, artifact delivery rules, CR-S determiners, and OPS capsule/ledger constraints.

## 1. Terms

**SAFEPOINT**  
A deterministic, self-contained ZIP archive used as sealed authority for resumption and audit. A SAFEPOINT is not “valid” until its SHA-256 verification passes and required components exist.

**CR-S (Continuity Record – SafePoint)**  
Mandatory minimum continuity record inside every SAFEPOINT (`/cr/CR_SafePoint.md`). Defines what was sealed and how to resume.

**CR-FOR (Continuity Record – Forensics/Operations Review)**  
Optional escalated continuity record used only when explicitly requested or when incident/forensic context requires it.

**RC Card**  
A working capsule used to stage changes, move work between AIs/sessions, or perform recovery. RC Cards are **not sealed authority**. If an RC Card conflicts with a sealed SAFEPOINT/CR, the sealed SAFEPOINT/CR wins.

## 2. Required SAFEPOINT Bundle Layout (minimum)

```text
/manifest/
  manifest.json
  hash.sha256.txt
/cr/
  CR_SafePoint.md
  CR_SafePoint.json (optional)
/payload/
  <project-selected artifacts>
/notes/
  README.md (optional)
  Known_Issues.md (optional)
```
If /cr/CR_SafePoint.json is emitted, it MUST validate against the active RetroFuse CR schema.

Minimum required files:
- `manifest/manifest.json`
- `manifest/hash.sha256.txt`
- `cr/CR_SafePoint.md`

---

## 3. SAFEPOINT Scope Boundary (Authoritative)

The term “SAFEPOINT” applies ONLY to sealed ZIP artifacts submitted to the SAFEPOINT Engine.
The AI does not have filesystem access and must not imply otherwise.
Any artifact intended for persistence must be delivered either:
	A) As a direct download, or
	B) Via an explicitly user-executed interactive script that creates the artifact locally.
Emitting content that requires the user to manually reconstruct an authoritative artifact constitutes a contract violation.
Any emission that results in an authoritative artifact existing only as chat text is invalid.

Within OPS:
- OPS may generate SAFEPOINT ZIP artifacts only for Engine intake, but:
- OPS folders MUST NOT be used as capture roots
- OPS does not normally “restore from SAFEPOINT” as an OPS-lane mechanism
- OPS continuity is normally maintained via:
  - Continuity Records (CR)
  - Append-only ledgers
  - Capsules
  - Canonical disk state as defined in OPS_CANONICAL_INDEX.md

---

## 4. Filename and Timestamp Rules

All SAFEPOINT filenames MUST include a timestamp in the form:

`YYYY-MM-DD_HHMMSS`

Example:
- `SAFEPOINT_RetroFuse_OPS_Dashboard_v1.5_SOPv3_2025-12-21_070200.zip`

Notes:
- Timestamp is *local time* (unless your lane explicitly standardizes UTC).
- The ZIP’s `manifest.json` should also contain an authoritative `created_utc`.

## 5. Determinism Rules

- A SAFEPOINT must not include other SAFEPOINT ZIPs.
- A SAFEPOINT must not be created inside its own capture root (anti-recursion).
- Capture routines must exclude vaults, quarantine folders, and mirrors.
- SAFEPOINT content should be reproducible from the same source inputs (no random or interactive prompts).

## 6. Hash and Verification Rules

- `manifest/hash.sha256.txt` MUST contain the SHA-256 hash of the full SAFEPOINT ZIP unless a project-specific engine contract explicitly states otherwise.
- A SAFEPOINT must not be declared valid without a successful verification pass.
- If verification fails, classify it as **quarantined/ghost** and do not load it.

## 7. Manifest Rules (machine routing)

The SOP requires `manifest.json` to exist. v3.2 requires these fields to enable Watcher routing and AI resumption:

- `project` (string)
- `lane` (string)
- `version` (string)
- `created_utc` (ISO8601 string)
- `filename_timestamp_local` (string `YYYY-MM-DD_HHMMSS`)
- `status` (candidate|sealed|verified)
- `contains` (object booleans: manifest/hash/continuity_record/payload)
- optional: `rc_card` metadata (if applicable)

## 8. CR-S Minimum Content Requirements

### 8.1 Determiners (CR-S REQUIRED)

CR-S MUST explicitly list:

- **ScriptPaths**
- **FolderRoots**
- **ScheduledTasks** (TaskPath + Name)
- **TaskActions** (Execute + Args)
- **Triggers**
- **Ports/Binds**
- **Watchdog/Restart behavior**

NOTE: The Watcher will NOT ACCEPT SAFEPOINTs that do not explicitly contain the required determiners above. Non-compliant SAFEPOINTs must be returned for correction/abatement. No exceptions. If a project does not contain an item above, that category must still be explicitly stated. If a category is truly not applicable, the CR must say “None” and must not omit it.

### 8.2 CR-S must also include, at a minimum:

- **Identity**: project, lane, version, timestamp
- **What was sealed**: key artifacts in `/payload/` and why they matter
- **Run/Start instructions**: exact commands and script paths
- **Known issues / risks**: anything that can bite the next AI
- **Resume plan**: the next 3–7 steps, deterministic

## 9. Capsules (OPS + Project)

### Definition
A **Capsule** is an **append-only** summary of a closed time range and the **OPS or Project state at the time of encapsulation**. Capsules exist to support truth checkpoints and resumption without rereading long CR histories.

### Scope and Location
- **OPS Capsules** MUST live at: `D:\RETROFUSE_OPS\_Capsules\`
- **Project Capsules** MUST live at: `<ProjectRoot>\_Capsules\`

### Naming Convention
- **Rolling/current capsule** (append-only):
  - OPS: `CAPSULE_OPS_CURRENT.md`
  - Project: `CAPSULE_<ProjectKey>_CURRENT.md`
- **Sealed capsule** (immutable snapshot; date-range encoded):
  - `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD.md`
  - If multiple sealed capsules are emitted for the same project on the same day-range, append time:
    - `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD__HHMMSS.md`

### Ledger Model
- **OPS Ledger is the ONLY ledger.**
- Projects MUST NOT maintain separate ledgers.
- Project status/events MUST be reported to the OPS Ledger using explicit project tagging (e.g., `[PROJECT:<ProjectKey>] <EventText>`).

### OPS Ledger Contract
LedgerPath: D:\RETROFUSE_OPS\Registry\OPS_COO\Ledger
Daily ledger filename: `OPS_COO_Ledger_YYYY-MM-DD.md`
Format: append-only
TagFormat: [PROJECT:<ProjectKey>] <EventText>
Timestamp: UTC ISO8601
OneLineEvent: true
Method: INLINE PS EMIT

### Capsule Content Rules
A capsule MUST include:
- Scope (OPS or Project) and ProjectKey (if Project scope)
- RangeStart (local) and RangeEnd (local)
- EncapsulationTimestamp (local)
- State at encapsulation time:
  - authoritative paths (explicit)
  - current policies (explicit)
  - scheduled tasks (TaskPath+Name; Action Execute+Args; Triggers)
  - ports/binds (if any)
  - resume rule (truth checkpoint rule)

A capsule MUST NOT:
- duplicate full CR text or ledger text
- define or override Governance/SOP/Contracts
- contain executable instructions that modify system state without explicit authorization

### Truth Checkpoint Rule
Truth checkpoint / resumption is performed as:
1) Load applicable Capsule (OPS or Project)
2) Apply only **CR and OPS Ledger deltas after the capsule’s EncapsulationTimestamp**


## 10. AI Behavioral Contract (SOP-aligned)

When the user asks for SAFEPOINTs or governance outputs:
- Produce downloadable artifacts. Do not require manual copy/paste.
- Do not defer deliverables with “later/tomorrow” placeholders.
- Keep changes in-place unless instructed otherwise.
- If a tool/script is broken, repair it *without* breaking existing folder layout.

## 11. “Last Known Good” sealing moment

Once a lane is boringly stable (reboot + watchdog + scheduled tasks validated):
- Seal a SAFEPOINT marked `status=sealed` (and optionally `verified` after hash verification).
- Record the stability checks performed in CR-S.
- This SAFEPOINT becomes the authoritative restore point.

