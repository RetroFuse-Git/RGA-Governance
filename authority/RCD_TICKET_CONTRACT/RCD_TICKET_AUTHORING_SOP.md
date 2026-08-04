# RCD Ticket Authoring SOP v1.0

## 1. Before You Start
- Read RCD_TICKET_CONTRACT_INDEX.md for the active contract version.
- Verify the schema hash against the authority manifest.
- Use governed lookup (Get-RetroFuseMountEntry.py) before declaring any path.
- Only RESOLVED_CANONICAL paths may authorize mutation.

## 2. Envelope Class Selection
Choose the correct envelope class: INITIAL_TICKET, IMPLEMENTATION_ROUND, CORRECTIVE_ROUND, WORKER_RETURN, CLOSEOUT_REQUEST, AUTHORITY_DECISION, or AUTHORITY_SEAL.

## 3. Required Fields
Every ticket requires: schema_version, ticket_id, chain_root_id, task_class, authority_effect, stage_id.
INITIAL_TICKET additionally requires: mission, path_block, acceptance_rules, hard_stops.
`cdp_targets` is REQUIRED and MUST contain only CDP-capable browser windows: `chatgpt`, `gemini`, or `deepseek`.
`rcd_cli` is the execution lane and MUST NOT appear in cdp_targets; it is expressed as the round's execution
owner, never as a CDP delivery target.

## 4. Paths
Replace PATHS_UNKNOWN with governed lookup results. Use RESOLVED_CANONICAL for mutation-authorizing paths. Mark unresolved paths explicitly with lookup-attempted evidence.

## 5. Git Authority
git_closeout_policy=report_only prohibits commits. push_authorized=false prohibits push. Be explicit.

## 6. Terminal Closeout
A seal must have next_expected_stage=null. A closeout request must include persistence_proof. A worker return must include evidence.

## 7. Emission
Emit via canonical Conductor/CDP path. Do not manually paste tickets. Do not use in-chat fallback when multi_cdp is required.
