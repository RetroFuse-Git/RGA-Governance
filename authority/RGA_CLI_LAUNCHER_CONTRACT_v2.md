# RGA CLI Launcher Contract v2

**Status:** Authoritative
**Scope:** All governed CLI sessions (ChatGPT, Gemini, DeepSeek, Copilot, Claude, Codex, Ollama, OpenClaw, Cursor)
**Date:** 2026-07-16

## 0. DISCOVER -> RESOLVE -> INVOKE (Mandatory Preamble)

Before implementing any routing, CDP discovery, authority-surface resolution, cache hydration, delivery, readback, authority admission, or startup orchestration logic:

1. **DISCOVER** — Consult the canonical toolchain registry (`RGA_CANONICAL_TOOLCHAIN_REGISTRY_v1.json`) and `OPS_CANONICAL_INDEX.md` Section 9 for the exact canonical tool matching the task.
2. **RESOLVE** — Read the canonical tool's interface. Do not infer or reconstruct its behavior from memory.
3. **INVOKE** — Call the canonical tool. Do not copy, wrap, fork, or reimplement its internals.
4. **GAP** — If the canonical tool cannot satisfy the ticket, stop and emit `CANONICAL_TOOL_CONTRACT_GAP` with evidence. Do not create a parallel implementation.

**Prohibition:** Direct reimplementation of page discovery, nonce correlation, bridge invocation, or readback logic is explicitly prohibited. The Conductor (`Invoke-RCDConductor.ps1`) is the only canonical cross-lane routing entry point. Every session starts by invoking the bootloader, resolving the canonical tool, and calling it — never by reimplementing what exists.

## 1. Boot Sequence (Mandatory)

All RGA-governed launchers must follow this exact sequence before establishing an interactive session:

### 1.1 Path Resolution
Resolve absolute paths for authority artifacts using OPS_CANONICAL_INDEX.md.

### 1.2 Static Authority Admission (no network, no processes)
Execute `RGA_Authority_Bootloader.ps1`. The bootloader must:
- Load and verify `RGA_BOOT_MANIFEST.sha256` against bootstrap trust anchor.
- Load and verify `RGA_BOOT_MANIFEST.json` against trust anchor.
- Hash-verify all BOOT_CRITICAL artifacts (missing or mismatch -> HALT).
- Hash-verify all BINDING_CONTRACT artifacts (missing or mismatch -> HALT).
- Warn on SUPPORTING_REFERENCE mismatches.
- Log HISTORICAL_EXCLUSION status.
- **Hard Stop:** If the bootloader fails admission, the launch MUST abort.

### 1.3 plan.md Discovery (no network, file read only)
- Walk from working directory to nearest governed project root.
- Load plan.md as primary active-work state per RetroFuse_SESSION_HANDOFF_SOP_v1.
- If plan.md absent: record PLAN_NOT_FOUND, continue (do not fabricate).
- Report plan.md path or PLAN_NOT_FOUND.

### 1.4 Runtime Readiness (may involve network/processes after explicit authorization)
- CDP bridge health check: Invoke-RCDHealthCheck.ps1 (separate diagnosis ticket).
- Daily Bundle hydration: Rehydrate_ColdLane.ps1.
- CR/Ledger initialization.
- HALT if runtime readiness fails.

### 1.5 Wrapper Injection
Launch the AI executable through `Bolt_CLI_Capture_Wrapper.py` to enforce governance and log all telemetry.

## 2. Allowed Roots (Execution Boundary)

Governed sessions are strictly limited to:
- `D:\RETROFUSE_OPS` (Primary Operational Root)
- `D:\PORTTORETRO_ARCHIVE` (Artifact & Archive Root)
- `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt` (Codebase Root)

Any attempt to read or write outside these roots must trigger a governance block.

## 3. Read-Only Session Rules

- Sessions are **Read-Only by default**.
- The `--allow-write` flag must be explicitly passed.
- Even in Write-Mode, canonical files under Canonical Guard remain locked.


## 4. Mutation-Fail Behavior

The Canonical Guard performs a post-session hash check. If a protected file was mutated:
1. **Revert:** Attempt to restore from pre-session snapshot.
2. **Alert:** Emit `GOVERNANCE_BLOCK` error.
3. **Audit:** Log violation to session capture and CR-OPS.
4. **Exit:** Return exit code `125`.

## 5. Boot Receipt Requirement

Every successful launch must generate a boot receipt conforming to RGA_BOOT_RECEIPT_SCHEMA.json in the authorized RGA receipt root (`D:\RETROFUSE_OPS\RGA\receipts`).

## 6. Workforce Orchestration Rule

When the operator asks for tools, Symphony, floor, workforce, local workers, or orchestration, the launcher must preserve that intent and must not replace it with direct senior-model labor.

- For scans, use local scripts first.
- For large recovery and reconstruction jobs, use batch manifests and floor-submit / floor-task handoff primitives.
- floor-submit is the generic explicit-source / batch-oriented handoff primitive.
- floor-task is plain-language, intent-driven.
- floor-submit resolves source refs and hands bounded work to local workers.
- Supervisors review compact reports and escalation packets, not raw bulk inventory.
- Direct model scanning of broad filesystem surfaces is forbidden unless explicitly authorized.
- If the orchestration tool is missing, propose or build the tool. Do not silently become the tool.

## 7. Operational Disciplines

The following disciplines are active by default in all governed CLI sessions:
- AUTHORITY_QC: authority verification, manifest integrity, seal validation.
- GOVERNANCE_ENGINEERING: lane boundary enforcement, path authority, Canonical Guard.

Additional disciplines (RELIABILITY_SRE, LEAN_SIX_SIGMA, CONTINUOUS_IMPROVEMENT, RECORDS_LIFECYCLE) may be activated by ticket scope or explicit operator instruction per Governance_RetroFuse_v3.3.1 S2.3.