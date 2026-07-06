# RetroFuse CR Event Classification Doctrine v1

Status: Active doctrine
Scope: OPS CR, project CR, Ledger parity, and derived narrative classification

## Purpose
CR entries are classified by effect, not by the lane that observed them. A CLI capture, HeartBundle, SecretaryOutbox narrative, tool observation, or human phrase can all become OPS-relevant when the content changes authority, governance, incident posture, paths, ports, scheduled tasks, watchdog behavior, restart behavior, SAFEPOINT handling, or continuity state.

## Required Fields
New direct CR entries should include these fields when available:

- CaptureType: HUMAN_INTENT | CLI_OBSERVATION | TOOL_OBSERVATION | MODEL_DERIVED | SYSTEM_RUNTIME | GOVERNANCE_EVENT
- AuthorityEffect: NONE | CONTINUITY_ONLY | PROJECT_STATE | OPS_STATE | GOVERNANCE_STATE | INCIDENT_STATE
- EvidencePath: absolute path when available; otherwise unknown
- Derived: yes | no
- LedgerRequired: yes | no | context

## Record That Semantics
`record that` is a human-intent capture signal. It is not a source lane and does not automatically define OPS authority.

The CR writer must resolve lane and authority from the captured content, evidence path, and authority effect. HeartBundles and CLI captures may be OPS-relevant when their content affects OPS state, governance, incident state, scheduled tasks, paths, ports, watchdogs, restart behavior, or SAFEPOINT handling.

## Authority Hierarchy
Direct CR entries with concrete evidence outrank derived narratives.

NarrativeEngine or SecretaryOutbox summaries must remain marked as derived, for example:

- CaptureType: MODEL_DERIVED
- AuthorityEffect: CONTINUITY_ONLY unless explicitly promoted by evidence
- Derived: yes

Derived summaries may inform continuity but must not override direct CR entries, Ledger entries, determiners, manifest evidence, or SAFEPOINT authority artifacts.

## Ledger Parity
A Ledger entry is required when the CR event affects any of these surfaces:

- OPS authority or governance
- path roots or canonical paths
- scheduled tasks
- ports or service binds
- watchdog, restart, or recovery behavior
- SAFEPOINT intake or SAFEPOINT authority
- incident state

Project-only or narrative-only continuity records may remain CR-only unless promoted by authority effect.
