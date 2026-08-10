# RetroFuse Pipeline Architecture v1

**Authority:** RGA Canonical
**Canonical Path:** D:\RETROFUSE_OPS\RGA\authority\RetroFuse_PIPELINE_ARCHITECTURE_v1.md
**Date:** 2026-07-14
**Status:** ACTIVE
**Supersedes:** None (new artifact)

> **Purpose:** Human-readable end-to-end architecture for the distributed RetroFuse continuity, bundle, transport, feedback, authority, and handoff pipeline.
> **Non-purpose:** This document does not carry runtime state, port/PID assignments, or per-session health. It declares architecture and ownership boundaries only.

---

## 1. Authority and Ownership Boundaries

### 1.1 Authority Hierarchy

```
RGA Governance (Governance_RetroFuse_v3.3.1)
  +-- AI_Contract_Safepoint_v3.2 (AI constraints)
  +-- RetroFuse_SAFEPOINT_SOP_v3.2 (process law)
  +-- RetroFuse_SESSION_HANDOFF_SOP_v1 (session lifecycle)
  +-- OPS_CANONICAL_INDEX.md (path authority)
  +-- RetroFuse_PIPELINE_ARCHITECTURE_v1.md (pipeline architecture)  [THIS]
  +-- RetroFuse_PIPELINE_REGISTRY_v1.json (machine registry)         [SIBLING]
```

### 1.2 Ownership Boundaries

| Domain | Owner | Authority Root |
|--------|-------|----------------|
| Governance & Authority | RGA | D:\RETROFUSE_OPS\RGA\authority |
| Pipeline Operations | OPS COO | D:\RETROFUSE_OPS\Registry\OPS_COO |
| CDP Bridge & Transport | RCD | D:\RETROFUSE_OPS\Tools\RCD |
| Cold Lane Boot | OPS _BOOT | D:\RETROFUSE_OPS\_BOOT\DAILY |
| Secretary & Continuity | Bolt Tools | D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools |
| Archive Projects | Bolt/RCD Archive | D:\PORTTORETRO_ARCHIVE\PROJECTS |

### 1.3 Cross-Boundary Rules

- RGA governance artifacts supersede all pre-RGA execution guidance.
- OPS_CANONICAL_INDEX.md is the sole path authority — no project BLUEPRINT or plan.md overrides it.
- RCD transport contracts (Routing v1.2, Envelope v3.1) govern transport selection and round closure.
- CLI is the sole routing and aggregation authority — no model self-routes.
- Bolt Tools are OPS-owned cross-cutting tools hosted in the Bolt repo for historical reasons. RGA migration is AUTHORIZED_TARGET_NOT_YET_MIGRATED.

---

## 2. Workspace and Project Startup

### 2.1 Boot Authority Order (Binding)

Per OPS_CANONICAL_INDEX.md Section 2:

1. `README_FIRST.md` (orientation only)
2. `RetroFuse_SAFEPOINT_SOP_v3.2` (process law)
3. `RetroFuse_SESSION_HANDOFF_SOP_v1` (session hydration and handoff)
4. `Governance v3.3.1 + AI Contract v3.2` (authority)
5. `OPS COO Startup Contract` (role binding)
6. `OPS_CANONICAL_INDEX.md` (authoritative path resolution)

If any of the above is missing -> **HALT: MISSING_ARTIFACTS**

### 2.2 Workspace BLUEPRINT Discovery

Each governed project root may declare a `BLUEPRINT.md` with a JSON header. Walk up from current directory to find `BLUEPRINT.md`; parse JSON header. Project BLUEPRINTs are authoritative for project-local paths only and do not override OPS_CANONICAL_INDEX.md.

### 2.3 OPS BLUEPRINT

- **Path:** D:\RETROFUSE_OPS\BLUEPRINT.md
- **Authority:** Workspace startup contract declaring workspace_root, project_paths, lane, authority, continuity_role, and escalation_paths.
- **Rule:** Read on startup for bounded orientation. Does not override OPS_CANONICAL_INDEX.md.

---

## 3. Nearest-Plan Discovery and Enclosing Workspace-Plan Supplementation

### 3.1 Algorithm (Deterministic)

```
1. Start at the declared working directory.
2. Walk upward to the nearest governed project or workspace root.
3. Load the nearest plan.md as the primary active-work state.
4. Load an enclosing workspace plan.md only as supplemental cross-project context.
5. Never allow a workspace plan to replace a project-local plan.
6. If no applicable plan exists, classify PLAN_NOT_FOUND.
7. Create plan.md only under explicit authority.
```

### 3.2 Test Cases

| Working Directory | Expected Primary | Expected Supplemental |
|-------------------|------------------|----------------------|
| D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools | D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\plan.md | D:\PORTTORETRO_ARCHIVE\PROJECTS\plan.md |
| D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD\Tools\bridge | D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD\plan.md | D:\PORTTORETRO_ARCHIVE\PROJECTS\plan.md |
| D:\RETROFUSE_OPS\Registry\OPS_COO\Tools | D:\RETROFUSE_OPS\plan.md | null |

### 3.3 Missing Fixture Rule

If an expected project plan does not yet exist, record PLAN_NOT_FOUND as a test outcome. Do not fabricate or create it under this ticket unless separately authorized.

### 3.4 Startup Continuity Sequence

After authority hydration (Section 2), before any mutation:

1. Discover nearest plan.md
2. Load primary plan state
3. Load supplemental workspace plan if present
4. Report what was found
5. Identify exact unresolved state, next speaker, next question
6. Proceed only after plan state is known

---

## 4. Cold Lane Hydration

### 4.1 Purpose

Hydrate a new session from the latest Daily Bundle, restoring CR, Ledger, and continuity state to the point of the last verified bundle.

### 4.2 Implementation

- **Script:** D:\RETROFUSE_OPS\_BOOT\DAILY\Rehydrate_ColdLane.ps1
- **Owner:** OPS _BOOT
- **Git status:** NOT TRACKED (durability risk)

### 4.3 Bundle Selection Precedence

```
continuity_latest > production_latest > signal_latest > bootstrap_default
```

| Pointer | Definition | Current (2026-07-14) |
|---------|-----------|---------------------|
| canonical_latest | Newest bundle accepted by disk authority with valid manifest/hash | 2026-07-13 |
| continuity_latest | Newest bundle with latest continuity state (updated daily) | 2026-07-13 |
| signal_latest | Newest signal-producing bundle | 2026-07-14 |
| production_latest | Newest PRODUCTION-classified bundle | 2026-07-14 |

### 4.4 Hydration Outputs

- CR file for the bundle's opsDay
- Ledger file for the bundle's opsDay
- Continuity state (capsules, sidecars)
- Production pointer advancement

### 4.5 Failure States

| Condition | Classification | Recovery |
|-----------|---------------|----------|
| No bundle found | COLD_LANE_EMPTY | Create bootstrap bundle |
| Bundle hash mismatch | COLD_LANE_HASH_FAIL | HALT, operator intervention |
| Manifest missing | COLD_LANE_MANIFEST_MISSING | HALT, operator intervention |
| CR/Ledger extraction fail | COLD_LANE_EXTRACT_FAIL | HALT, operator intervention |

---

## 5. Secretary Continuity Extraction and Sidecars

### 5.1 Purpose

Extract structured continuity evidence from CLI session HeartBundles into machine-readable JSON sidecars for deterministic classification, supersession, and bundle inclusion.

### 5.2 Implementation

- **Secretary:** D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\Ollama_Secretary.py
- **Continuity Extractor:** D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\cli_continuity_extractor.py
- **Continuity Classifier:** D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\cli_continuity_classifier.py
- **Schema:** D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\schemas\cli_continuity_record.schema.json
- **Owner:** Bolt Tools (OPS cross-cutting)
- **Git status:** Bolt repo, dirty (staged + unstaged)

### 5.3 Sidecar Format

Each HeartBundle `.md` file produces a `.continuity.json` sidecar with:
- 18 deterministic fields (commit_hash, ticket_ids, test_files, push_state, authority_tokens, supersession links)
- 7 bounded interpretive fields (activity_type, continuity_significance, authority_state, capability_built, operator_significance, continuity_priority, resume_relevance)

### 5.4 Current Scale

- 5953 records extracted
- 1959 superseded by terminal evidence
- 1066 terminal (MAJOR+) records
- 26 unique terminal achievements visible
- Bundle size impact: ~5% growth (under 6% target)

### 5.5 Failure States

| Condition | Classification | Recovery |
|-----------|---------------|----------|
| HeartBundle parse fail | SIDECAR_PARSE_FAIL | Logged, non-blocking |
| Schema validation fail | SIDECAR_SCHEMA_FAIL | Logged, non-blocking |
| Sidecar write fail | SIDECAR_WRITE_FAIL | Logged, non-blocking |

---

## 6. Terminal and Supersession Classification

### 6.1 Purpose

Classify CLI records by terminality and supersede lower-ranked records with higher-ranked evidence.

### 6.2 Supersession Hierarchy

```
TERMINAL_SEALED (rank 100) > AUTHORITY_ACCEPTED (rank 90) >
RESOLVED_OR_CLEAN (rank 70) > FAILED_OR_BLOCKED (rank 40) >
INTERMEDIATE (rank 20) > START (rank 10)
```

### 6.3 Activity Classification

| Activity Type | Description |
|---------------|-------------|
| ADMIN | Administrative operations |
| MAINTENANCE | System maintenance |
| REPAIR | Bug fixes and defect correction |
| BUILD | Feature construction |
| VALIDATION | Testing and verification |
| CLOSEOUT | Ticket/round closure |
| CAPABILITY_CREATION | New capability introduction |

### 6.4 Continuity Significance

| Significance | Description |
|--------------|-------------|
| TRIVIAL | Low-impact activity |
| USEFUL | Moderate-impact activity |
| MAJOR | High-impact activity |
| TERMINAL | Round/chain-terminating activity |
| CAPABILITY_DEFINING | New capability introduction |

### 6.5 Implementation

- **Extractor:** cli_continuity_extractor.py (supersession engine)
- **Classifier:** cli_continuity_classifier.py (deterministic two-axis)
- **WriteSessionCloseout.py:** Replaced FIRST-CLASSIFICATION-WINS with supersession-aware classification

---

## 7. Momentum Generation

### 7.1 Purpose

Generate a structured sky-high operational summary from structured continuity sidecars for Daily Bundle inclusion and session orientation.

### 7.2 Implementation

- **Generator:** D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt\Tools\cli_momentum_generator.py
- **Caller:** D:\RETROFUSE_OPS\_BOOT\DAILY\Emit-MomentumFromChainState.ps1
- **Owner:** Bolt Tools (generator) + OPS _BOOT (caller)
- **Git status:** Generator staged in Bolt repo; caller NOT TRACKED

### 7.3 Momentum Contract

The Momentum contract includes:
- Sky-high architecture view
- Terminal achievements visible (9 as of 2026-07-14)
- Current blockers (separated: current vs historical)
- Last seal and receipt
- NextStep and ResumeAt
- SourceTimestamp and SourceTicketOrEvent

### 7.4 Failure States

| Condition | Classification | Recovery |
|-----------|---------------|----------|
| No sidecars found | MOMENTUM_NO_SIDECARS | Fall back to Watcher DB |
| Sidecar parse fail | MOMENTUM_PARSE_FAIL | Fall back to Watcher DB |
| Watcher DB unavailable | MOMENTUM_DB_UNAVAILABLE | Emit minimal contract |

---

## 8. Daily Bundle Construction

### 8.1 Purpose

Assemble all operational evidence (CR, Ledger, continuity sidecars, momentum, receipts) into a single verifiable bundle for distribution.

### 8.2 Implementation

- **Builder:** D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\OpsCOO_Build_DailyBundle_v1.ps1
- **Owner:** OPS COO
- **Git status:** NOT TRACKED (durability risk)

### 8.3 Bundle Contents

- CR file for opsDay
- Ledger file for opsDay
- Structured CLI continuity sidecars
- Momentum contract
- Manifest (SHA-256 sealed)
- All 12 required tools validated
- No SAFEPOINT leakage
- Authority roles valid

### 8.4 Bundle Identity

- **Naming:** OPS_DailyBundle_YYYY-MM-DD.zip
- **SHA-256:** Recorded in manifest and CR
- **Validation:** seal-check PASS required

### 8.5 Failure States

| Condition | Classification | Recovery |
|-----------|---------------|----------|
| Tool validation fail | BUNDLE_TOOL_MISSING | HALT, operator intervention |
| Manifest seal fail | BUNDLE_SEAL_FAIL | HALT, operator intervention |
| SAFEPOINT leakage detected | BUNDLE_SAFEPOINT_LEAK | HALT, operator intervention |
| Authority role invalid | BUNDLE_AUTHORITY_FAIL | HALT, operator intervention |

---

## 9. Provider-Specific Bundle Formatting

### 9.1 Purpose

Format the canonical Daily Bundle into provider-specific formats for each governed AI lane.

### 9.2 DeepSeek

- **Script:** D:\RETROFUSE_OPS\Tools\RCD\Providers\DeepSeek\Scripts\Format-DailyBundleForDeepSeek.ps1
- **Version:** Rev 5.1 (hardened)
- **Owner:** RCD
- **Git status:** Dirty (unstaged changes)
- **Key features:**
  - Construction-only default (no delivery without -Deliver)
  - -DryRun flag (zero dispatch proof)
  - -SkipChatGPT restored as default
  - Invoke-Expression removed (replaced with Start-Process)
  - Stale Rev 2 retired to _Archive

### 9.3 Gemini

- **Status:** No dedicated formatter identified. Gemini receives bundles via CDP bridge or WebMCP.
- **Format:** Standard bundle format, no provider-specific transformation.

### 9.4 ChatGPT

- **Status:** No dedicated formatter identified. ChatGPT receives bundles via CDP bridge.
- **Format:** Standard bundle format, no provider-specific transformation.

### 9.5 Duplicate Paths

| Path | Status | Disposition |
|------|--------|-------------|
| D:\RETROFUSE_OPS\Tools\RCD\Providers\DeepSeek\Scripts\Format-DailyBundleForDeepSeek.ps1 | ACTIVE_CANONICAL | Canonical Rev 5.1 |
| D:\RETROFUSE_OPS\Tools\RCD\Tools\Format-DailyBundleForDeepSeek.ps1 | RETIRED_STUB | Fail-closed stub (exit 1) |
| D:\RETROFUSE_OPS\Tools\RCD\Tools\_Archive\Format-DailyBundleForDeepSeek_Rev2_RETIRED_20260714.ps1 | FROZEN_REFERENCE | Historical Rev 2 |

---

## 10. Transport Selection

### 10.1 Governed Transports

| Transport | Status | Selection Rule |
|-----------|--------|----------------|
| CDP | ACTIVE_CANONICAL | Default for all authority rounds |
| WebMCP | ACTIVE_WHERE_PROVEN | Capability-selected, not universal |
| Backend | CONDITIONALLY_ADMITTED | Explicit admission required per task |
| Manual Relay | DEGRADED_EMERGENCY_FALLBACK_ONLY | Operator authorization required |

### 10.2 Deterministic Transport Decision Table

Per RCD-CLI-ROUTING-CONTRACT-v1.2, the CLI selects transport deterministically based on task type, not model preference. The 8-task matrix covers: authority dispatch, advisory routing, bundle delivery, feedback return, seal return, inspection, recovery, and bootstrap.

### 10.3 Anti-Routing Rules

1. No model may self-select transport.
2. WebMCP is not the universal successor to CDP.
3. Manual relay is degraded only, never normal completion.
4. Transport may not be silently changed mid-round.

### 10.4 Transport Policy (Envelope v3.1)

Per RCD-CROSSLANE-ENVELOPE-v3.1, each ticket may declare a `transport_policy` block:
- `allowed_transports`: subset of [cdp, webmcp, backend]
- `selected_transport`: must be in allowed_transports
- `transport_selection_reason`: required when policy present
- `webmcp_universal_replacement`: must be false
- `backend_transport_admitted`: must be explicitly true

When absent, CDP is the default for all round legs.

---

## 11. Serialized Dispatch, Provider Cooldowns, Lockouts, and Circuit Breakers

### 11.1 Serialized Dispatch

Per the backend architecture (RCD-20260714-RICH-RESPONSE-MULTI-AGENT-BACKEND-DELIVERY-DESIGN-024):
- Per-provider locks prevent concurrent dispatch to the same provider.
- Cooldown windows between dispatches to the same provider.
- Sequential dispatch order: ChatGPT -> Gemini -> DeepSeek (or as specified by ticket).

### 11.2 Provider Lockout

- After 3 consecutive failures (429, timeout, connection error), the provider enters PROVIDER_LOCKOUT.
- Lockout duration: Retry-After header value, or default 60 seconds.
- Operator-visible halt: lockout state is recorded in the receipt and surfaced in momentum.

### 11.3 Circuit Breaker

Pseudocode per architecture design (not yet implemented as executable):
- Track consecutive failures per provider.
- Open circuit after threshold (3 failures).
- Half-open after cooldown (1 successful probe).
- Closed after successful probe.

### 11.4 Gaps (per Gemini critique)

- No pre-dispatch health check implemented.
- No auto-recovery window after lockout (requires operator intervention).

---

## 12. Bundle Identity, Idempotency, and Resume-from-Receipt

### 12.1 Bundle Identity

Each bundle is uniquely identified by:
- **Name:** OPS_DailyBundle_YYYY-MM-DD.zip
- **SHA-256:** Recorded in manifest and CR
- **opsDay:** The operational day the bundle represents

### 12.2 Idempotency

- Bundle construction is idempotent: rebuilding the same opsDay produces the same content (same inputs -> same SHA-256).
- Bundle delivery is idempotent: delivering the same bundle twice is a no-op (receipt check).
- Receipt writing is idempotent: same receipt SHA-256 -> no duplicate.

### 12.3 Resume-from-Receipt

Per backend architecture:
- Each emission produces a receipt with: bundle_id, target, transport, timestamp, SHA-256, status.
- Receipts are persisted and retrievable.
- On resume, the Cold Lane reads the latest receipt to determine the last successful delivery point.
- Resume skips completed deliveries and continues from the first incomplete.

---

## 13. Universal Per-Artifact Feedback Obligation

### 13.1 Binding Statement

Per RCD-CLI-ROUTING-CONTRACT-v1.2:
Every governed artifact emitted to any lane creates a mandatory feedback obligation for that lane. Feedback is not optional, cannot be disabled by omission of a flag, and cannot be replaced by a summary.

### 13.2 Per-Artifact Lifecycle (16 Stages)

```
1. ARTIFACT_REGISTERED
2. TARGET_AND_TRANSPORT_SELECTED
3. EMISSION_RECEIPT_WRITTEN
4. TARGET_DELIVERY_CONFIRMED
5. RESPONSE_OBSERVED
6. FULL_RESPONSE_CAPTURED
7. RESPONSE_COMPLETENESS_VERIFIED
8. RAW_RESPONSE_PERSISTED
9. RESPONSE_HASHED
10. RESPONSE_CLASSIFIED
11. RESPONSE_ATTACHED_TO_FEEDBACK_BUNDLE
12. FEEDBACK_RETURNED_TO_ORIGIN_AUTHORITY
13. AUTHORITY_CONSUMPTION_RECORDED
14. AUTHORITY_VERDICT_RETURNED
15. CLI_ACK_CAPTURED
16. ARTIFACT_ROUND_TERMINAL
```

### 13.3 Response Completeness Contract

Required per response:
- artifact_id, target_lane, transport
- response_full_path, raw_response_full_path, response_sha256
- source_observed_char_count, captured_char_count, persisted_byte_count
- capture_segments, final_segment_seen
- truncation_detected, completeness_verified, verification_method

### 13.4 Failure Classifications

RESPONSE_MISSING, RESPONSE_EMPTY, RESPONSE_TIMEOUT, RESPONSE_PARTIAL, RESPONSE_TRUNCATED, RESPONSE_STALE, RESPONSE_COMPLETENESS_UNVERIFIED, RESPONSE_ARTIFACT_MISSING, RESPONSE_HASH_MISMATCH, RESPONSE_NOT_RETURNED_TO_AUTHOR, RESPONSE_NOT_CONSUMED_BY_AUTHORITY.

### 13.5 Terminal Gate

Terminal blocked when: any emitted artifact lacks a complete response record, completeness_verified is not true for any response, truncation_detected is true for any response, any advisory/reasoning lane response is missing without explicit operator waiver.

---

## 14. Full Response Capture, Persistence, Retrieval, and Authority Consumption

### 14.1 Capture Method

- **CDP:** Segmented expanding readback until response terminator or stable complete boundary observed. Line-count stabilization is the primary completion detector. Timers/sensors are fallback only.
- **WebMCP:** Full structured response extraction. Record object size, pagination state, completion marker.
- **Backend:** Complete provider response body + finish_reason + token counts + byte length + hash.
- **Manual relay:** DEGRADED_MANUAL_RELAY. Operator confirms entire response relayed.

### 14.2 Persistence

- Full response texts persisted to immutable `.txt` artifacts alongside JSON metadata.
- JSON artifact includes: full_response_text, full_response_chars, full_response_bytes, full_response_sha256, full_response_path.
- Historical regression fixed: artifact save code no longer truncates to 500 characters.

### 14.3 Retrieval

- Responses are retrievable by SHA-256 from the artifact path.
- Operator retrieval proof: full text available at persisted path with matching hash.

### 14.4 Authority Consumption

- Authority (ChatGPT) receives the full feedback bundle.
- Authority consumes each response, issues disposition (ACCEPT, REJECT, NEEDS_MORE_EVIDENCE).
- Authority verdict is physically returned through governed transport.
- CLI reads back and ACKs the authority seal.

---

## 15. Cross-Agent and CLI Round-Table Lifecycle

### 15.1 Round Legs (Mandatory)

Per RCD-CROSSLANE-ENVELOPE-v3.1 closure_contract:

1. TICKET_VALIDATED
2. TRANSPORT_SELECTED_AND_RECEIPTED
3. ALL_DECLARED_TARGETS_ROUTED
4. EACH_RESPONSE_OBSERVED
5. EACH_RESPONSE_CLASSIFIED
6. EACH_RESPONSE_ARTIFACT_PRESERVED
7. FEEDBACK_BUNDLE_AGGREGATED
8. FEEDBACK_BUNDLE_RETURNED_TO_AUTHOR
9. AUTHORITY_VERDICT_EMITTED
10. AUTHORITY_VERDICT_PHYSICALLY_RETURNED_TO_CLI
11. CLI_READBACK_CAPTURED
12. CLI_ACK_EMITTED
13. TERMINAL_RECEIPT_WRITTEN

### 15.2 Round Roles

| Role | Lane | Responsibility |
|------|------|----------------|
| Architecture | DeepSeek Pro | Primary architecture and implementation |
| Critique | Gemini | Advisory review and gap identification |
| Implementation Review | CLI | Runtime enforceability critique |
| Authority QC | ChatGPT | Final authority disposition and seal |

### 15.3 Round Closure Rules

- Terminal allowed only when: all mandatory round legs PASS or operator-waived, all declared advisory/reasoning lanes have response artifacts or failure classifications, authority seal physically returned through governed transport, CLI observed and ACKed the seal, terminal receipt contains all evidence paths and hashes.
- Terminal forbidden when: advisory response missing without waiver, feedback bundle not returned to author, authority seal exists only in UI text, CLI ACK absent, manual relay without DEGRADED_MANUAL_RELAY, transport silently changed, required round artifact absent.
- Incomplete classification: ROUND_INCOMPLETE.

---

## 16. ACTIVE_INCOMPLETE_CHAIN Preservation

### 16.1 Purpose

Preserve the active incomplete chain across session boundaries so that successor sessions can resume from the exact unresolved state.

### 16.2 Mechanism

- The plan.md at the active project root records the current round-table state, unresolved questions, next speaker, and missing legs.
- The Cold Lane hydrates from the latest Daily Bundle, which contains the most recent continuity state.
- The Secretary sidecars preserve terminal and supersession evidence across sessions.

### 16.3 Rules

- No active incomplete chain may disappear into quiet-day classification.
- The plan.md must be updated before session retirement with the exact unresolved state.
- Successor sessions must read plan.md first and resume from the exact unresolved state.
- No session may restart completed work when a verified handoff exists.

### 16.4 Failure States

| Condition | Classification | Recovery |
|-----------|---------------|----------|
| plan.md missing | PLAN_NOT_FOUND | Create plan.md before retirement |
| plan.md stale | PLAN_STALE | Hydrate from latest bundle, reconcile |
| Chain state lost | CHAIN_STATE_LOST | HALT, operator intervention |

---

## 17. Authority Seal Return and CLI ACK

### 17.1 Seal Contract

Per the SEAL_CONTRACT block in each RCD-ENVELOPE ticket:
- seal_authority: The authority lane that issues the seal (typically ChatGPT).
- full_source_artifact_review_required: true.
- all_material_adversarial_findings_dispositioned: true.
- seal_return_transport: The governed transport for seal return (typically cdp).
- cli_ack_required: true.
- terminal_only_after_cli_ack: true.

### 17.2 Seal Return Flow

1. Authority (ChatGPT) reviews all feedback and issues disposition.
2. Authority seal is physically returned through governed transport (CDP).
3. CLI observes the seal and reads back the verdict.
4. CLI emits ACK.
5. Terminal receipt is written with all evidence paths and hashes.
6. Round is classified TERMINAL.

### 17.3 CLI ACK Requirements

- CLI must read back the exact authority verdict.
- CLI must confirm all material adversarial findings have disposition.
- CLI must confirm the seal was physically returned through governed transport.
- CLI ACK must be captured in the terminal receipt.

---

## 18. Session Retirement and Successor Hydration

### 18.1 Retirement Requirements

Per RetroFuse_SESSION_HANDOFF_SOP_v1:

Before retirement, the AI MUST:
1. Update plan.md with current round-table state, newly completed work, updated unresolved questions, next speaker assignment, new risks/findings/deferred items, updated artifact paths and hashes, successor rehydration instructions.
2. Read back the exact canonical path of the written plan.
3. Report file size, modification time, and SHA-256 hash.
4. Confirm the plan contains unresolved state and successor instructions.
5. Confirm no temp-only or sandbox copy was treated as authoritative.

### 18.2 Successor Hydration

On every new session startup, the AI MUST:
1. Read plan.md from the active project root before taking any action.
2. Load the authority stack declared in the plan or canonical index.
3. Hydrate from the latest Daily Bundle.
4. Identify the exact unresolved state, next speaker, and next question.
5. Report what was found in the plan before proposing any action.

### 18.3 No-Restart Rule

Work marked COMPLETE in the plan must not be restarted, re-audited, re-implemented, or re-proven. If evidence conflicts with the plan, surface the contradiction as a finding — do not silently redo the work.

---

## 19. Failure States, Halt Conditions, and Recovery Boundaries

### 19.1 Global Halt Conditions

| Condition | Source | Recovery |
|-----------|--------|----------|
| MISSING_ARTIFACTS | Boot authority order | Operator intervention |
| PLAN_NOT_FOUND | Plan discovery | Create plan.md under authority |
| CHAIN_STATE_LOST | Chain preservation | Operator intervention |
| COLD_LANE_HASH_FAIL | Cold Lane hydration | Operator intervention |
| COLD_LANE_MANIFEST_MISSING | Cold Lane hydration | Operator intervention |
| COLD_LANE_EXTRACT_FAIL | Cold Lane hydration | Operator intervention |
| BUNDLE_TOOL_MISSING | Bundle construction | Operator intervention |
| BUNDLE_SEAL_FAIL | Bundle construction | Operator intervention |
| BUNDLE_SAFEPOINT_LEAK | Bundle construction | Operator intervention |
| BUNDLE_AUTHORITY_FAIL | Bundle construction | Operator intervention |
| PROVIDER_LOCKOUT | Serialized dispatch | Operator intervention or auto-recovery |
| ROUND_INCOMPLETE | Round closure | Complete missing legs |

### 19.2 Recovery Boundaries

- **Cold Lane failures:** HALT at boot. No session proceeds without valid hydration.
- **Bundle construction failures:** HALT at build. No bundle emitted without valid seal.
- **Transport failures:** Degrade to next available transport. Manual relay only with operator authorization.
- **Provider lockout:** Operator-visible halt. Auto-recovery window not yet implemented.
- **Round incomplete:** Session continues but cannot close. Missing legs must be completed.

---

## 20. Git Ownership, Rollback, and Durability Risks

### 20.1 Git Repository Map

| Path | Git Repo | Remote | Status |
|------|----------|--------|--------|
| D:\PORTTORETRO_ARCHIVE\PROJECTS\Bolt | YES | RetroFuse-Git/Bolt.git | Dirty (staged + unstaged) |
| D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD | NO | N/A | Not tracked |
| D:\RETROFUSE_OPS\Tools\RCD | YES | None configured | Dirty (unstaged) |
| D:\RETROFUSE_OPS\Registry\OPS_COO | NO | N/A | Not tracked |
| D:\RETROFUSE_OPS\_BOOT | NO | N/A | Not tracked |
| D:\RETROFUSE_OPS (root) | NO | N/A | Not tracked |

### 20.2 Durability Risks (Critical)

The following critical OPS executables are NOT version-controlled:

| Component | Path | Risk |
|-----------|------|------|
| Cold Lane | D:\RETROFUSE_OPS\_BOOT\DAILY\Rehydrate_ColdLane.ps1 | Single point of failure, no rollback |
| Momentum Emitter | D:\RETROFUSE_OPS\_BOOT\DAILY\Emit-MomentumFromChainState.ps1 | Single point of failure, no rollback |
| Daily Bundle Builder | D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\OpsCOO_Build_DailyBundle_v1.ps1 | Single point of failure, no rollback |
| OPS COO Tools | D:\RETROFUSE_OPS\Registry\OPS_COO\Tools\ | No version history |

### 20.3 Rollback Capability

- **Bolt repo:** Full rollback via git (remote: RetroFuse-Git/Bolt.git). Commits: e1f498e, 241d0d9.
- **OPS RCD repo:** Local git only, no remote. Rollback possible but not distributed.
- **OPS _BOOT, OPS COO Registry:** No rollback capability. Manual restore from Daily Bundle archives.

### 20.4 Git Governance Rules

- Exact-file staging only — never `git add .` or `git add -A`.
- Push is operator-authorized — declared at the top of the ticket or granted by explicit operator request. The operator may authorize push at any time (Authority Rule #1 is senior). Structural prohibitions (force push, history rewrite, `git clean`) require an RF-level operator override.
- Bolt: commit/push only through `Tools\Bolt_Promote_MirrorChanges.ps1 -OperatorAuthorized`.

---

## 21. Canonical-Copy Enforcement and Duplicate Retirement Policy

### 21.1 Canonical Copy Rules

- Each executable stage has exactly one canonical path.
- All other copies are classified and dispositioned.
- No duplicate executable implementation may remain silently authoritative.
- Canonical paths are recorded in the Pipeline Registry.

### 21.2 Duplicate Classification

| Classification | Definition | Action |
|----------------|------------|--------|
| CANONICAL | The authoritative implementation | Preserve |
| COMPATIBILITY_STUB | Thin wrapper calling canonical | Preserve, document |
| FROZEN_REFERENCE | Historical snapshot, not executable | Preserve, document |
| HISTORICAL | Retired/archived version | Preserve in _Archive |
| CORRUPTED | Damaged or divergent copy | Quarantine |
| UNKNOWN | Cannot classify | HALT, operator intervention |

### 21.3 Known Duplicates

| Stage | Canonical Path | Duplicate Path | Classification |
|-------|---------------|----------------|----------------|
| rcd_cdp_return.py | D:\RETROFUSE_OPS\Tools\RCD\Tools\bridge\rcd_cdp_return.py (84,261 bytes, 8B4F768E) | D:\PORTTORETRO_ARCHIVE\PROJECTS\RCD\Tools\bridge\rcd_cdp_return.py (83,100 bytes, 983BB931) | FROZEN_REFERENCE (archive copy, 1,161 byte delta) |
| rcd_five_file_delivery.cjs | D:\RETROFUSE_OPS\Tools\RCD\Tools\bridge\rcd_five_file_delivery.cjs (24,846 bytes, 86551C26) | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\P0_BASELINE_FREEZE_20260712\rollback\bridge\rcd_five_file_delivery.cjs (24,776 bytes) | FROZEN_REFERENCE (baseline freeze) |
| Format-DailyBundleForDeepSeek.ps1 | D:\RETROFUSE_OPS\Tools\RCD\Providers\DeepSeek\Scripts\Format-DailyBundleForDeepSeek.ps1 (29,638 bytes) | D:\RETROFUSE_OPS\Tools\RCD\Tools\Format-DailyBundleForDeepSeek.ps1 (743 bytes) | COMPATIBILITY_STUB (fail-closed) |
| Format-DailyBundleForDeepSeek.ps1 | D:\RETROFUSE_OPS\Tools\RCD\Providers\DeepSeek\Scripts\Format-DailyBundleForDeepSeek.ps1 (29,638 bytes) | D:\RETROFUSE_OPS\Tools\RCD\Tools\_Archive\Format-DailyBundleForDeepSeek_Rev2_RETIRED_20260714.ps1 (18,044 bytes) | HISTORICAL (retired Rev 2) |
| RCD-CLI-ROUTING-CONTRACT | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CLI-ROUTING-CONTRACT-v1.2.md (3,476 bytes) | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CLI-ROUTING-CONTRACT-v1.1.md | HISTORICAL (superseded) |
| RCD-CLI-ROUTING-CONTRACT | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CLI-ROUTING-CONTRACT-v1.2.md (3,476 bytes) | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CLI-ROUTING-CONTRACT-v1.md | HISTORICAL (superseded) |
| RCD-CROSSLANE-ENVELOPE | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CROSSLANE-ENVELOPE-v3.1.md (4,594 bytes) | D:\RETROFUSE_OPS\Tools\RCD\Artifacts\RCD-CROSSLANE-ENVELOPE-v1.md | HISTORICAL (superseded) |

### 21.4 Duplicate Retirement Policy

- Duplicates classified as HISTORICAL or FROZEN_REFERENCE are preserved but not authoritative.
- Duplicates classified as COMPATIBILITY_STUB are preserved as fail-closed wrappers.
- No duplicate may be deleted without separate authorization.
- The Pipeline Registry records all known duplicates and their dispositions.

---

## Appendix A: Pipeline Stage Summary

| # | Stage | Implementation | Owner | Git |
|---|-------|---------------|-------|-----|
| 1 | Authority Hydration | OPS_CANONICAL_INDEX.md + boot order | RGA | Tracked |
| 2 | Plan Discovery | Nearest-plan.md walk | CLI | N/A (algorithm) |
| 3 | Cold Lane Hydration | Rehydrate_ColdLane.ps1 | OPS _BOOT | NOT TRACKED |
| 4 | Secretary Extraction | Ollama_Secretary.py + cli_continuity_extractor.py | Bolt Tools | Tracked (dirty) |
| 5 | Supersession | cli_continuity_classifier.py + WriteSessionCloseout.py | Bolt Tools | Tracked (dirty) |
| 6 | Momentum Generation | cli_momentum_generator.py + Emit-MomentumFromChainState.ps1 | Bolt Tools + OPS _BOOT | Partial |
| 7 | Bundle Construction | OpsCOO_Build_DailyBundle_v1.ps1 | OPS COO | NOT TRACKED |
| 8 | Provider Formatting | Format-DailyBundleForDeepSeek.ps1 | RCD | Tracked (dirty) |
| 9 | Transport Selection | CLI (per Routing Contract v1.2) | CLI | N/A (contract) |
| 10 | Serialized Dispatch | Backend architecture (design) | RCD | Design only |
| 11 | Feedback Capture | CDP bridge + artifact persistence | RCD | Tracked |
| 12 | Round Closure | Envelope v3.1 closure_contract | CLI | N/A (contract) |
| 13 | Authority Seal | ChatGPT QC + seal return | ChatGPT | N/A (external) |
| 14 | Session Retirement | plan.md update + handoff | CLI | N/A (process) |
| 15 | Successor Hydration | plan.md read + bundle hydrate | CLI | N/A (process) |

## Appendix B: Cross-Stage Invariants

1. No silent path inference.
2. No silent transport switching.
3. No terminal closure before required feedback consumption and CLI ACK.
4. No active incomplete chain may disappear into quiet-day classification.
5. No duplicate executable implementation may remain silently authoritative.
6. No plan.md may override canonical authority.
7. No session may restart completed work when a verified handoff exists.
8. No advisory challenge may be treated as resolved without a response and disposition.
9. CLI remains sole routing and aggregation authority.
