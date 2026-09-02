# RCD Ticket Authoring SOP v1.1

## 1. Before You Start
- Read RCD_TICKET_CONTRACT_INDEX.md for the active contract version.
- Verify the schema hash against the authority manifest.
- Use governed lookup (Get-RetroFuseMountEntry.py) before declaring any path.
- Only RESOLVED_CANONICAL paths may authorize mutation.
- **Selector era (v1.1+):** obtain every control-plane value from
  `RCD_SELECTOR_MANIFEST_v1.json` (the machine-readable selector authority).
  Do not invent authority-bearing vocabulary. The shared validator
  (`D:\RETROFUSE_OPS\Tools\RCD\Tools\selector\validate_selector_envelope.py`)
  refuses required-unset and illegal selector values. New envelopes MUST stamp
  `selector_manifest_version`.

## 2. Envelope Class Selection
Choose the envelope class from the selector manifest `class_contracts`:
INITIAL_TICKET, EXECUTION_TICKET, IMPLEMENTATION_ROUND, CORRECTIVE_ROUND,
WORKER_RETURN, CLOSEOUT_REQUEST, EXECUTION_RETURN, AUTHORITY_DECISION, or
AUTHORITY_SEAL. Classification determines the legal status set and the legal
authority_effect set (class-dependent; see manifest).

## 3. Required Fields
Every selector-era ticket requires: schema_version, ticket_id, chain_root_id,
task_class, authority_effect, stage_id, classification, status,
execution_lane, delivery_mode, routing_mode, cdp_targets,
git_closeout_policy, selector_manifest_version.
Class-required fields (mission/path_block/acceptance_rules/hard_stops for
INITIAL_TICKET; evidence for EXECUTION_RETURN; etc.) are enforced by the
selector manifest class contract.
`cdp_targets` is REQUIRED and MUST contain only CDP-capable browser windows:
`chatgpt`, `gemini`, or `deepseek`.
`rcd_cli` is the execution lane and MUST NOT appear in cdp_targets; it is
expressed as the round's execution owner, never as a CDP delivery target.

## 4. Paths
Replace PATHS_UNKNOWN with governed lookup results. Use RESOLVED_CANONICAL for mutation-authorizing paths. Mark unresolved paths explicitly with lookup-attempted evidence.

## 5. Git Authority
Selector-era legal values: report_only | defer_until_product_boundary |
commit_if_authorized | push_if_authorized | enforce_clean_sync.
Unknown values REFUSE -- never silent default.
report_only / defer_until_product_boundary / commit_if_authorized imply
push_authorized=false; push_if_authorized / enforce_clean_sync imply
push_authorized=true. Do not supply a contradictory explicit push_authorized;
the selector validator refuses it.

### 5.1 Push-First Pending-Push Precedence (v1.2, registered by
OPS-20260902-AUTHORITY-GIT-CONTINUITY-PUSH-FIRST-CONTRACT-REPAIR-001)

When authoring any ticket (initial, next-round, corrective, or terminal), the
author MUST evaluate pending-push state for every governed repository the
chain touches, in this precedence:

(A) Explicit NO_PUSH authority: a governing artifact (sealed finding, SOP
    clause) or direct operator instruction requires the commit to remain
    unpushed -> preserve the unpushed state, cite the authority source in the
    ticket, and record the obligation for carry-forward. NO_PUSH requires a
    concrete reason/source; absence of push authorization is NOT itself a
    standing prohibition and must not propagate indefinitely.
(B) Known verified already-authorized pending push: a tracked-clean,
    ahead-of-origin repository whose outgoing commits are proven
    authorized/sealed governed work -> the next executable ticket MUST place
    bounded push reconciliation (verify identities, fast-forward push, prove
    0/0) as its FIRST action, before new implementation/discovery work. A
    clean-but-ahead repository is NOT "synchronized"; it must be surfaced as
    `ahead N (authorized pending push)`, never as synchronized, and never
    treated as harmless housekeeping while subsequent governed work is being
    emitted.
(C) No eligible pending push -> normal ticket-specific git_closeout_policy
    applies.

Carry-forward rule: ticket-authoring logic MUST carry known pending-push
state across rounds and chains until discharged. A later report_only ticket
MUST NOT erase, shadow, or silently defer that obligation; if the current
round's task is report_only but an inherited eligible push exists, the ticket
must still lead with (B)'s bounded push reconciliation. Distinguish a
clean-ahead repository from a dirty working tree: both are surfaced; only the
clean-ahead state is push-eligible under this precedence. If any outgoing
commit cannot be tied to authorized governed work, HALT the push and return
the exact commit list for authority adjudication (never push a partial range
past an unverified commit).

## 6. Terminal Closeout
A seal must have next_expected_stage=null. A closeout request must include persistence_proof. A worker return must include evidence.

## 7. Legacy Qualification
Envelopes WITHOUT `selector_manifest_version` qualify as legacy ONLY with
positive `legacy_provenance` (source_kind in {intake_artifact,
exchange_round_artifact} + an existing source_path). Absence of the stamp is
NOT legacy by itself; new unstamped envelopes refuse at the gate.

## 8. Emission
Emit via canonical Conductor/CDP path. Do not manually paste tickets. Do not use in-chat fallback when multi_cdp is required. Selector-era envelopes pass through Submit-RCDTicket.ps1, which runs the selector gate before Conductor dispatch. Direct RF/operator prose authority is never constrained by selector validation.
