# OPS Handoff Pack v1.3

**Status:** Authoritative handoff / seal-candidate  
**Scope:** OPS Continuity / GEN7 rehydration  
**Date:** 2026-01-04  
**Corrected:** 2026-05-03  
**Supersedes:** None (additive)  
**Historical Packs:** Archived, non-authoritative  

---

## 0. Purpose (Read First)

This document is the authoritative OPS handoff pack for cold-lane rehydration, successor AI resumption, and human re-entry.

It does not supersede the authority stack declared in `OPS_CANONICAL_INDEX.md`. Authority artifacts, paths, and boot law are resolved by the Canonical Index.

This handoff answers only:

- What authority stack governs OPS
- What rehydration anchors to load
- What actions are allowed
- What actions are forbidden
- How to resume safely without inference

It does **not** explain history.  
It does **not** justify decisions.  
It does **not** teach architecture.  
It does **not** create new authority paths.

---

## 1. Authority Boundary (Hard Binding)

All OPS actions are bound by the active authority stack declared in `OPS_CANONICAL_INDEX.md`, including:

1. `README_FIRST.md` for orientation
2. `RetroFuse_SAFEPOINT_SOP_v3.2.md` for SAFEPOINT process law
3. `Governance_RetroFuse_v3.3.0.md` and `AI_Contract_Safepoint_v3.2.json` for system authority and AI constraints
4. `RetroFuse_OPS_StartupContract_OPSCOO_v1.md` for OPS COO role binding
5. `OPS_CANONICAL_INDEX.md` for authoritative path resolution

If any required authority artifact is missing, ambiguous, unverifiable, or conflicting, the AI must halt with the appropriate failure code, such as `MISSING_ARTIFACTS` or `AUTHORITY_CONFLICT`.

Explicit human instruction controls the active session only unless captured into authoritative disk artifacts through the required continuity process.

---

## 2. OPS Rehydration Order (Do Not Deviate)

This is the OPS rehydration order, not the authority boot order. Authority boot order is declared by `OPS_CANONICAL_INDEX.md`.

1. Load `README_FIRST.md` for orientation.
2. Load `OPS_CANONICAL_INDEX.md` for path resolution and authority stack.
3. Load OPS Path Registry if declared present by the Canonical Index.
4. Load today’s OPS COO Ledger.
5. Load today’s CR-OPS.
6. Apply the WTD-First Continuity Anchor Rule:
   a. Load `OPS_COLDLANE_CONTEXT_PATCH_Latest.md` for WTD continuity anchor.
   b. If WTD anchor is present: use WTD as primary anchor; apply CR and
      OPS Ledger deltas after WTD timestamp; skip capsule load.
   c. If WTD anchor is absent: load `LATEST_ACCEPTED_CAPSULE` as fallback
      anchor; apply CR and OPS Ledger deltas after capsule timestamp.
   d. If neither is available: HALT with `MISSING_CONTINUITY_ANCHOR`.
7. Record anchor selection in boot receipt:
   - `anchor_used`: "WTD" | "CAPSULE" | "NONE"
   - `anchor_timestamp`: ISO 8601 timestamp of the selected anchor
   - `delta_start`: ISO 8601 timestamp from which deltas are applied
   - `wtd_present`: true/false
   - `capsule_used`: true/false

If any required artifact is missing, halt with `MISSING_ARTIFACTS`. Do not infer substitute paths.

---

## 3. OPS Root — Disk Truth Pointer

**Path:** `D:\RETROFUSE_OPS\`

This path is authoritative only because it is declared by the Canonical Index.

It must not be pruned, renamed, reinterpreted, regenerated, or replaced without explicit human authorization and required CR-OPS continuity recording.

Folder contents may be validated by tooling and ledgered events, but runtime validation does not supersede Canonical Index authority.

---

## 4. Current Continuity Anchors (Pointers Only)

Do not restate volatile state. Use disk truth and declared canonical paths.

- **OPS COO Ledger:**  
  `D:\RETROFUSE_OPS\Registry\OPS_COO\Ledger\OPS_COO_Ledger_YYYY-MM-DD.md`

- **CR-OPS daily append-only record:**  
  `D:\RETROFUSE_OPS\Registry\OPS_COO\CR_OPS\CR_OPS_YYYY-MM-DD.md`

- **OPS Capsules:**  
  `D:\RETROFUSE_OPS\_Capsules\`

- **OPS Root:**  
  `D:\RETROFUSE_OPS\`

If uncertain, halt and request the missing artifact or path confirmation. Do not infer.

---

## 5. Allowed Actions

The following actions are permitted only when they stay inside the Canonical Index, Governance, SOP, AI Contract, Startup Contract, and active CR schema boundaries:

- Append entries to today’s OPS COO Ledger.
- Append entries to today’s CR-OPS file.
- Verify disk state using read-only checks.
- Run existing OPS scripts and tools only when they are declared by the Canonical Index, Path Registry, active CR, or explicit human instruction.
- Emit new CR-OPS entries for OPS-level changes.
- Report project status/events to the OPS Ledger using explicit project tags.

All writes must be append-only unless the human operator explicitly authorizes a different action and that action is captured in CR-OPS when OPS scope is affected.

---

## 6. Forbidden Actions (Critical)

The following actions are forbidden without explicit written/session authorization from the human operator:

- Regenerating OPS structure.
- Rewriting or deleting OPS Ledger entries.
- Rewriting or deleting CR-OPS entries.
- Resealing SAFEPOINTs.
- Creating new authority artifacts ad hoc.
- Creating new roots, alternate roots, or parallel structures.
- Cleaning up, pruning, moving, or deleting historical or archived material.
- Inferring missing authority, missing files, missing paths, system state, or validation results.
- Treating chat memory, model memory, or prior examples as disk truth.

If unsure, halt.

---

## 7. SAFEPOINT Intake Posture (Summary)

SAFEPOINT intake behavior is governed by `RetroFuse_SAFEPOINT_SOP_v3.2.md`, `AI_Contract_Safepoint_v3.2.json`, and Canonical Index intake pointers.

- SAFEPOINTs are ZIP-only.
- SAFEPOINTs must conform to SOP v3.2 bundle layout and CR-S determiner requirements.
- Intake is performed through the declared watcher/engine path.
- Valid SAFEPOINT ZIPs are filed by the Engine.
- Noncompliant ZIPs are skipped or marked according to SOP/Engine behavior.
- Quarantine is reserved for corrupt or unreadable ZIPs.
- OPS folders must not be used as SAFEPOINT capture roots.

Do not alter intake behavior without CR-OPS and Ledger entry when OPS scope is affected.

---

## 8. Temporal Rehydration Rule

Chat/session context is non-authoritative and disposable.

OPS continuity is restored by declared disk anchors only:

- OPS COO Ledger
- CR-OPS
- OPS Capsules when applicable
- Canonical disk state as declared by `OPS_CANONICAL_INDEX.md`

Context pruning is allowed only when disk anchors are current and verified by explicit evidence or human assertion.

---

## 9. History and Archives (Non-Authoritative)

Historical, narrative, or forensic documents may live under:

```text
D:\RETROFUSE_OPS\_BOOT\GEN7\Archived\
```

These are reference-only. They must not be treated as authority, boot requirements, or veto sources against GEN7 action unless explicitly promoted into authority through Canonical Index and CR-OPS.

---

## 10. Failure Codes

Use these failure codes when applicable:

- `MISSING_ARTIFACTS` — required authority or continuity artifacts are absent or inaccessible.
- `AUTHORITY_CONFLICT` — authoritative documents conflict and no explicit human override resolves the active session.
- `DETERMINERS_MISSING` — required SAFEPOINT/CR-S determiners are missing or implicit.
- `UNKNOWN_PATH` — a required path is not declared in the Canonical Index, Path Registry, active CR, or explicit human instruction.

Do not continue through these states by inference.

---

## 11. Seal

This document ends here.

Nothing below this point is authoritative.
