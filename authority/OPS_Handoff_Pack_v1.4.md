# OPS Handoff Pack v1.4 — RGA/RCD Operations Re-entry

**Status:** Authoritative handoff
**Scope:** RGA-governed, RCD-operated OPS continuity
**Date:** 2026-07-06 — RGA cutover
**Supersedes:** OPS_Handoff_Pack_v1.3 (GEN7-era; archived, historical reference only)

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

All OPS actions are bound by the active authority stack declared in `OPS_CANONICAL_INDEX.md`:

1. Governance_RetroFuse_v3.3.0.md — system authority
2. AI_Contract_Safepoint_v3.2.json — AI constraints
3. RetroFuse_SAFEPOINT_SOP_v3.2.md — SAFEPOINT process law
4. RetroFuse_CR_Schemas_v3.1.1.json — CR schema
5. OPS_CANONICAL_INDEX.md — authoritative path resolution
6. RetroFuse_OPS_StartupContract_OPSCOO_v1.md — role binding
7. OPS_Handoff_Pack_v1.4.md — this document

If any required authority artifact is missing or conflicting → HALT: MISSING_ARTIFACTS or AUTHORITY_CONFLICT.

## 2. Authority State (Current)

- **RGA (RetroFuse Governance Authority):** ACTIVE — canonical root `D:\RETROFUSE_OPS\RGA\authority`
- **GEN7:** RETIRED/HISTORICAL — `D:\RETROFUSE_OPS\_Archive\LegacyBoot\GEN7_RETIRED_20260705`
- **RCD (RetroFuse Command Desk):** ACTIVE — `D:\RETROFUSE_OPS\Tools\RCD`
- **Tools\RGA\_boot:** ARCHIVED — not active authority
- **_BOOT\GEN7:** NOT CURRENT — do not use as active boot root

## 3. OPS Rehydration Order

Proceed in this exact order after authority stack load:

1. Confirm RGA authority root is present: `D:\RETROFUSE_OPS\RGA\authority`
2. Confirm CUTOVER_RECEIPT.json is present: `D:\RETROFUSE_OPS\RGA\CUTOVER_RECEIPT.json`
3. Confirm RCD health check: `Invoke-RCDHealthCheck.ps1`
   - PASS → proceed
   - WARN → proceed with caution logged
   - FAIL → HALT (CDP bridge not operational)
4. Load CR/Ledger as append-only recording surfaces when required by current authority
5. Run `OpsCOO_Bootstrap.ps1` only if declared by Canonical Index or explicit operator instruction
6. Report: --OPS BOOTSTRAP COMPLETE--

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
- Cross-lane contradictions are surfaced, not flattened
- Aggregate verdict gates chain progress

## 7. Prohibited Actions

- No GEN7-first boot authority
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

## 9. Historical

- OPS_Handoff_Pack_v1.3: GEN7-era predecessor — archived, non-authoritative
- GEN7 Boot Root: Retired to `D:\RETROFUSE_OPS\_Archive\LegacyBoot\`
- All pre-RGA handoff documents should not be loaded as current authority
