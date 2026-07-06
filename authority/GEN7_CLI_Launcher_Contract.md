# GEN7 CLI Launcher Contract v1.0
**Status**: Authoritative
**Scope**: All Governed CLI Sessions (Gemini, Codex, Ollama)

## 1. Boot Sequence (Mandatory)
All GEN7-governed launchers must follow this exact sequence before establishing an interactive session:
1.  **Path Resolution**: Resolve absolute paths for the `Bolt_CLI_Capture_Wrapper.py` and `OpsCOO_GEN7_Bootloader.ps1`.
2.  **Bootloader Execution**: Execute the `OpsCOO_GEN7_Bootloader.ps1`. 
    - **Integrity Check**: The bootloader must verify SHA256 hashes against `GEN7_BOOT_MANIFEST.json`.
    - **Truth Initialization**: The bootloader must ensure today's Ledger and CR-OPS are initialized.
    - **Hard Stop**: If the bootloader returns a non-zero exit code or integrity drift is detected, the launch **MUST** abort.
3.  **Reference-Only Capsule Hydration**: Emit a boot hydration preflight via `capsule_engine.py boot-hydrate` before the interactive surface launches.
    - **Disable Switch**: If `RETROFUSE_BOOT_HYDRATION_DISABLED=1`, skip hydration and continue with normal launch sequencing.
    - **Budget Policy**: Default `NORMAL` for GEN7/operator boot surfaces. Fast CLI launchers may set `RETROFUSE_BOOT_HYDRATION_BUDGET=LIGHT`. `EXPANDED` remains manual only.
    - **Authority Boundary**: Hydration is reference-only memory. It must not grant runtime authority or load raw source bodies by default.
4.  **Canonical Guard**: Snapshot protected files (Controller, Start Scripts, Narrative Builders).
5.  **Mirroring (Optional)**: If `$UseMirror` is active, sync the canonical root to the mirror root using `Initialize-MirrorWorkspace`.
6.  **Boot Continuity Bridge Advisory Overlay**: If the shadow bridge pointer is active and validated, consume the derived continuity overlay after Canonical Guard and before wrapper handoff. The overlay is read-only, derived, and must not elevate a Local Context Pack to authority.
7.  **Wrapper Injection**: Launch the AI executable through the `Bolt_CLI_Capture_Wrapper.py` to enforce governance and log all telemetry.

## 2. Allowed Roots (Execution Boundary)
Governed sessions are strictly limited to the following roots:
- `D:\RETROFUSE_OPS` (Primary Operational Root)
- `D:\PORTTORETRO_ARCHIVE` (Artifact & Archive Root)
- `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt` (Codebase Root)

Any attempt to read or write outside these roots must trigger a governance block.

## 3. Read-Only Session Rules
- Sessions are **Read-Only by default**.
- The `--allow-write` flag must be explicitly passed (e.g., `bg w`).
- Even in Write-Mode, canonical files under the **Canonical Guard** remain locked.

## 4. Mirror Policy
- **Canonical Mode**: Direct operation on the primary codebase. Reserved for low-risk architectural work.
- **Mirror Mode**: [RETIRED 2026-06-16] Copy-on-write operation previously targeted `D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt_MIRROR` (directory deleted). Mirror mode is deprecated; all work now lands directly in canonical project roots via access-boundary shortcuts.
- **Promotion**: [RETIRED] `Bolt_Promote_MirrorChanges.ps1` is obsolete. Mirror promotion workflow is retired.

## 5. Mutation-Fail Behavior
- The **Canonical Guard** performs a post-session hash check.
- If a protected file was mutated during a session (even with `--allow-write`), the launcher must:
    1.  **Revert**: Attempt to restore the file from the pre-session binary snapshot.
    2.  **Alert**: Emit a `GOVERNANCE_BLOCK` error to STDOUT.
    3.  **Audit**: Log the violation to the session capture and the CR-OPS.
    4.  **Exit**: Return exit code `125`.

## 6. Boot Receipt Requirement
Every successful launch must generate a **Shared Boot Receipt** in the session log and the CR-OPS, capturing the full operational context.

## 7. Workforce Orchestration Rule
When the operator asks for tools, Symphony, floor, workforce, local workers, or orchestration, the launcher must preserve that intent and must not replace it with direct senior-model labor.

- For scans, use local scripts first.
- For large recovery and reconstruction jobs, use batch manifests and floor-submit / floor-task handoff primitives.
- floor-submit is the generic explicit-source / batch-oriented handoff primitive.
- floor-task is plain-language, intent-driven.
- floor-submit resolves source refs and hands bounded work to local workers.
- Supervisors review compact reports and escalation packets, not raw bulk inventory.
- Direct model scanning of broad filesystem surfaces is forbidden unless explicitly authorized.

