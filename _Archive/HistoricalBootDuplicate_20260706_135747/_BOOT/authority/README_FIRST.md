# README_FIRST.md
## v2 — Hardened Orientation (Authoritative Alignment)

---
## Absolute Path Discipline (Non-Negotiable)

Inferred file paths are forbidden.

If an explicit absolute path is not provided, the AI MUST halt and request a file tree or exact path before proceeding.

This rule applies to:
- scripts
- CR creation
- ledger updates
- SAFEPOINT handling
- watcher behavior
- verification or validation steps

Failure to comply is a hard stop condition.

Mandatory: AIs will execute Codex or Codex-like validation tools in their own sandbox for advisory preflight only before emitting to user; all submissions remain subject to authoritative OPS-side Codex enforcement.

---

## Purpose

This document provides **orientation only** for OPS startup and resumption.

It exists to:
- Establish **boot order**
- Declare **authority boundaries**
- Prevent inference, drift, or accidental execution
- Align orientation with **existing SAFEPOINT SOP v3.2** and Governance

---

## Non-Authority Statement (Critical)

This document is **not authoritative**.

It:
- Grants **no execution authority**
- Grants **no write permission**
- Grants **no SAFEPOINT creation or sealing authority**
- Does **not** override SAFEPOINT SOP, Governance, or AI Contract

If any conflict exists, the correct action is **HALT**.

---

## Workforce Orchestration Rule

When the operator asks to use tools, Symphony, floor, workforce, local workers, or orchestration, do not substitute direct senior-model labor for that request.

For large recovery, reconstruction, filesystem, archive, or D-drive jobs:
- tools enumerate, hash, validate, batch, and summarize
- floor-submit is the generic explicit-source / batch-oriented handoff primitive
- floor-task is plain-language, intent-driven
- floor-submit resolves source refs and hands bounded work to local workers
- local workers classify bounded batches
- supervisors review compact reports
- senior cloud models review summaries, plans, or escalation packets only
- raw bulk inventory must not be ingested into senior model context
- direct model scanning of broad filesystem surfaces is forbidden unless explicitly authorized
- large filesystem/recovery work must use tools -> batches -> floor-submit -> local workers -> supervisor review

If the orchestration tool is missing, propose or build the tool. Do not silently become the tool.

---

## Continuity Law

**Disk truth is authoritative.**

- CRs, Ledgers, SAFEPOINTs, and manifests are the sole continuity mechanism.
- Chat context, AI memory, and inference are **non-authoritative** and disposable.
- If required artifacts are missing, **inference is forbidden**.
- CRs and ledger entries are not prose artifacts. They are emitted via PowerShell inline-emit only, ensuring append-only integrity and reproducibility.

Correct response to missing or unverifiable artifacts: **HALT**.

---

## Orientation Load Checklist

Follow this order **exactly**.

### 0. Enumerate Received Artifacts
List all artifacts explicitly provided in this session by name and version.

If a required artifact is missing →  
**HALT: MISSING_ARTIFACTS**

---

### 0.5 Verify Artifact Integrity
Verify:
- Presence
- Completeness
- Version correctness
- Hashes (if applicable)

If verification cannot be performed →  
**HALT**

---

### 1. README_FIRST.md (This Document)
Orientation only.  
No authority is granted here.

---

### 2. SAFEPOINT SOP v3.2+ (Process Law)
Defines:
- SAFEPOINT structure
- Required components
- Intake, validation, quarantine, sealing rules

This is binding process law.

---

### 3. Governance v3.3.0 + AI Contract v3.2 (Authority)
Defines:
- Authority hierarchy
- Lane separation
- Prohibited actions
- HALT conditions

If authority is unclear →  
**HALT: AUTHORITY_CONFLICT**

---

### 4. Startup Contract: OPS COO (Role Binding)
Binds the AI to the OPS COO role only.

- No cross-lane writes
- No SAFEPOINT creation unless explicitly authorized
- No governance modification

---

### 5. Continuity Artifacts (OPS + Projects)

### OPS Ledger (single sink — authoritative event stream)
- OPS Ledger is the ONLY ledger.
- All project status/events MUST be recorded into the OPS Ledger using explicit project tagging:
  - Example tag: `[PROJECT:<ProjectKey>]`

Canonical OPS Ledger path:
- `D:\RETROFUSE_OPS\Registry\OPS_COO\Ledger\`

### Capsules (state snapshots used for truth checkpoints)
Capsules exist at two scopes:
- OPS scope capsule: state snapshot of OPS at encapsulation time
- Project scope capsule: state snapshot of a project at encapsulation time

Canonical capsule paths:
- OPS capsules: `D:\RETROFUSE_OPS\_Capsules\`
- Project capsules: `<ProjectRoot>\_Capsules\`

Capsule naming:
- Rolling/current (append-only):
  - OPS: `CAPSULE_OPS_CURRENT.md`
  - Project: `CAPSULE_<ProjectKey>_CURRENT.md`
- Sealed (immutable snapshot; human-readable date range):
  - `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD.md`
  - If collision: `CAPSULE_<ProjectKey>_YYYYMMDD_YYYYMMDD__HHMMSS.md`

### Truth checkpoint rule (capsule cutoff + delta-only)
To resume efficiently (cold boot or truth checkpoint):
1) Load the relevant capsule (OPS or Project)
2) Apply only deltas AFTER the capsule’s `EncapsulationTimestamp`:
   - OPS deltas: OPS CR + OPS Ledger entries after cutoff
   - Project deltas: project CR entries after cutoff (project has NO ledger)

Notes:
- Capsules summarize state; they do NOT override Governance/SOP/Contracts.
- Projects MUST NOT create ledgers; project reporting goes to OPS Ledger only.

---

### 6. Optional Context Artifacts (Non-Authoritative)
Historical notes, prior CRs, dashboards, or reference material.

These **inform** but do not authorize.

## Mandatory HALT Conditions

Immediately halt if any of the following occur:

- Required artifact missing
- Artifact unverifiable
- Authority unclear
- Determiners missing
- Inference required to proceed
- Cross-lane action implied

---

## SAFEPOINT Definition (OPS)

A SAFEPOINT is **only** valid when submitted as a **ZIP archive** via the SAFEPOINT Intake Watcher.

### Required ZIP Structure
```
/manifest/manifest.json
/manifest/hash.sha256.txt
/cr/CR_SafePoint.md
/payload/
```
- Authoritative artifacts are delivered either as direct downloads or via interactive emitters. Inline code blocks are informational only.
- Folder submissions are **never authoritative**
- Non-compliant SAFEPOINTs are skipped or quarantined per SOP
- SAFEPOINT handling is fully governed by SOP v3.2
- Any emission that results in an authoritative artifact existing only as chat text is invalid. 

---

## SAFEPOINT Sealing (Reference Only)

SAFEPOINT sealing requires:
- Stability verification
- CR documentation
- Hash validation

Sealing rules are governed **exclusively** by SAFEPOINT SOP v3.2.  
This document does not authorize sealing.

---

## Final Rule

If you feel the need to “help,” “assume,” or “fill in gaps”:

**Stop.**  
The system is working correctly.  
The correct action is **HALT**.
“If artifacts present → proceed to mandated outputs (checklist/tree/schema/action/scripts)”
“No idle state allowed”

