# Gen-7 Operations Kernel v1.3 — Successor-Proof Operations Guidance

**Status:** AUTHORITATIVE / SEALED BY SIDECAR  
**Effective Date:** 2025-12-27  
**Baseline Source:** v1.1 Hardened  
**Scope:** GEN7 operational behavior and successor handoff guidance  

---

## 0. Authority Boundary

This document is the GEN7 operational kernel for RetroFuse OPS behavior and successor handoff guidance.

It is authoritative only within its operational scope and remains subordinate to the active authority stack declared in `OPS_CANONICAL_INDEX.md`, including:

1. `README_FIRST.md` for orientation
2. `RetroFuse_SAFEPOINT_SOP_v3.2.md` for SAFEPOINT process law
3. `Governance_RetroFuse_v3.3.0.md` and `AI_Contract_Safepoint_v3.2.json` for system authority and AI constraints
4. `RetroFuse_OPS_StartupContract_OPSCOO_v1.md` for OPS COO role binding
5. `OPS_CANONICAL_INDEX.md` for authoritative path resolution

If this kernel conflicts with the Canonical Index, Governance, SAFEPOINT SOP, AI Contract, active CR schema, or explicit human instruction for the active session, the higher authority wins. The AI must declare the conflict and halt or proceed only under explicit human override.

---

## 1. Authoritative Roots

The following roots and authority artifacts are resolved by the Canonical Index and must not be inferred or replaced:

- **OPS Root:** `D:\RETROFUSE_OPS`
- **GEN7 Boot Root:** `D:\RETROFUSE_OPS\_BOOT\GEN7`
- **Governance Authority:** `D:\RETROFUSE_OPS\_BOOT\GEN7\Governance_RetroFuse_v3.3.0.md`
- **SAFEPOINT SOP Authority:** `D:\RETROFUSE_OPS\_BOOT\GEN7\RetroFuse_SAFEPOINT_SOP_v3.2.md`
- **AI Contract Authority:** `D:\RETROFUSE_OPS\_BOOT\GEN7\AI_Contract_Safepoint_v3.2.json`
- **CR Schema Authority:** `D:\RETROFUSE_OPS\_BOOT\GEN7\RetroFuse_CR_Schemas_v3.1.1.json`
- **OPS Handoff Pack:** `D:\RETROFUSE_OPS\_BOOT\GEN7\OPS_Handoff_Pack_v1.3.md`
- **Dashboard Root:** `D:\RETROFUSE_OPS\Dashboard`

Any root or artifact not listed in the Canonical Index is non-authoritative unless explicitly authorized by the human operator and recorded in CR-OPS when OPS scope is affected.

---

## 2. Runtime State Boundary

Runtime state is not authority.

Ports, PIDs, process health, watcher status, dashboard status, and latest DailyCheck references are transient state. They may be observed, reported, or captured in CR/ledger evidence when appropriate, but they must not supersede Canonical Index, Governance, SOP, AI Contract, CR schema, capsules, or verified disk authority.

The dashboard and DailyCheck outputs are implementation/state surfaces, not governance authority.

---

## 3. Forensic Recording & Recovery

Every OPS-impacting operation must preserve append-only continuity.

- **CR-OPS:** OPS continuity changes must be appended to the daily CR file declared by the Canonical Index.
- **OPS Ledger:** Integrity evidence and project status events must be appended to the OPS COO Ledger when required.
- **No silent rewrites:** No script or AI response may overwrite the Canonical Index, CR-OPS, ledger, Governance, SOP, AI Contract, or CR schema without explicit authorization and continuity record.
- **Failure mode:** If required authority artifacts are missing, ambiguous, unverifiable, or conflicting, halt with the appropriate failure code, such as `MISSING_ARTIFACTS`, `AUTHORITY_CONFLICT`, or `DETERMINERS_MISSING`.

---

## 4. SAFEPOINT and Artifact Rules

SAFEPOINT behavior is governed by `RetroFuse_SAFEPOINT_SOP_v3.2.md` and the active AI Contract.

- SAFEPOINTs are valid only as sealed ZIP artifacts conforming to SOP requirements.
- SAFEPOINT emission must use approved delivery mechanisms: direct downloadable artifact or explicitly user-executed interactive emitter.
- Chat-only authoritative artifacts are invalid.
- SAFEPOINTs must include required CR-S determiners.
- OPS folders must not be used as SAFEPOINT capture roots.
- No SAFEPOINT may be placed inside its own capture root.

Any historical SOP ZIP or engine-filed SOP copy is archive/engine evidence only unless the Canonical Index declares it as active boot authority.

---

## 5. Successor Task Queue

Priority 1: Preserve authority alignment across Canonical Index, Governance v3.3.0, SAFEPOINT SOP v3.2, AI Contract v3.2, and CR schema v3.1.1.

Priority 2: Maintain OPS Dashboard as an implementation/status surface without allowing dashboard runtime state to become authority.

Priority 3: Keep DailyCheck and RFCC status automation observable, append-only, and subordinate to Canonical Index authority.

Priority 4: Maintain OPS Handoff Pack integrity at `D:\RETROFUSE_OPS\_BOOT\GEN7\OPS_Handoff_Pack_v1.3.md`.

---

## 6. Agency Requirement

For any operational review, request, or execution, the AI must produce at least one of the following:

1. **Improvement recommendation**
2. **Risk identification with mitigation**
3. **Structural enhancement proposal**

The selected item or items must be explicitly labeled and concise. They must materially affect correctness, reliability, observability, or recoverability.

If none exist, the AI must explicitly state:

`NO_ACTION_JUSTIFIED`

with reasoning.

---

## 7. Seal Metadata

Artifact: `Gen7_Operations_Kernel_v1.3.md`  
Canonical Path: `D:\RETROFUSE_OPS\_BOOT\GEN7\Gen7_Operations_Kernel_v1.3.md`  
Status: SEALED by sidecar metadata

  
Seal Sidecar: `Gen7_Operations_Kernel_v1.3.md.seal.md`
Corrected: 2026-05-03
