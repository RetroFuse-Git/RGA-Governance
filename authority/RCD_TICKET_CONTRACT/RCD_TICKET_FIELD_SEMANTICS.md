# RCD Ticket Field Semantics v1.1

## Field Ownership
RGA owns: schema_version, authority_effect, authority posture, acceptance rules.
RCD owns: routing_mode, delivery_mode, cdp_targets, git_closeout_policy, mutation_rules.
Shared: ticket_id, chain_root_id, stage_id, mission.
Selector authority (v1.1+): `RCD_SELECTOR_MANIFEST_v1` (generated artifact,
`RCD_TICKET_CONTRACT/RCD_SELECTOR_MANIFEST_v1.json`) owns the legal-value sets
for every control-plane selector. No selector-critical value exists only in
implementation constants.

`stage_id` is REQUIRED on every ticket envelope (round-local, per RCD_TICKET_AUTHORING_SOP §3).
`cdp_targets` is REQUIRED and MUST be a non-empty list drawn only from {chatgpt, gemini, deepseek}.
`rcd_cli` is the execution lane, not a CDP delivery target; it MUST NOT appear in cdp_targets.

## Selector-Era Construction (v1.1, pre-authorized 2026-08-18)
- New envelopes MUST stamp `selector_manifest_version` and MUST use only legal
  values from the selector manifest. The shared validator
  (`RCD Tools/selector/validate_selector_envelope.py`) is the single fail-closed
  gate; required-unset and illegal values REFUSE submission.
- `git_closeout_policy` legal set (reconciled to Conductor runtime):
  report_only | defer_until_product_boundary | commit_if_authorized |
  push_if_authorized | enforce_clean_sync.
  Unknown values REFUSE -- never silent default to report_only.
  `bounded_local_commit_authorized` / `bounded_local_commit_authorized_no_push`
  are historical ticket-text artifacts, NOT legal selector values.
- `push_authorized` is DERIVED from git_closeout_policy. Explicit contradiction
  is refused (PUSH_POLICY_CONTRADICTION).
- POSITIVE legacy qualification: envelopes WITHOUT `selector_manifest_version`
  qualify as legacy ONLY when carrying `legacy_provenance` (source_kind in
  {intake_artifact, exchange_round_artifact} + source_path that exists).
  Absence of the stamp is NOT legacy by itself; new unstamped envelopes REFUSE.

## Duplication Rule
ticket_id and chain_root_id may appear at top-level and inside payload for consumer compatibility. Values MUST be identical. Any divergence is a BLOCKED validation error.

## Nullability
Optional fields must be accessed through safe presence checks. Missing optional fields normalize to null, not empty string. StrictMode consumers require explicit null guards.

## Immutable Fields
chain_root_id and prior_round_id are immutable once set. stage_id is round-local.

## Forbidden Combinations
- authority_effect=NONE with mutation_rules containing non-empty allowed list
- git_closeout_policy=report_only with commit in authorized actions
- git_closeout_policy in {report_only, defer_until_product_boundary, commit_if_authorized} with push_authorized=true (selector validator refuses)
- terminal_verdict=SEALED_TERMINAL with non-null next_expected_stage
- classification=WORKER_RETURN/CLOSEOUT_REQUEST/EXECUTION_RETURN with mutation_rules present (class contract forbids)
- prior_round_id / correction_target on INITIAL_TICKET (class contract forbids)

## Pending-Push Obligation (v1.2, registered by
OPS-20260902-AUTHORITY-GIT-CONTINUITY-PUSH-FIRST-CONTRACT-REPAIR-001)

A repository left `ahead N` with a tracked-clean tree by an authorized or
sealed governed commit carries a PENDING-PUSH OBLIGATION, not a completed
disposition:

- It MUST be surfaced in every subsequent ticket's Git-state evidence as
  `ahead N (authorized pending push)`; describing it as `synchronized` is a
  validation-level misrepresentation (see AUTHORING_SOP §5.1 precedence).
- `git_closeout_policy=report_only` governs the CURRENT round's mutations
  only; it never discharges or suppresses an inherited pending-push
  obligation. A report_only ticket authored while an eligible authorized
  pending push exists must still place bounded push reconciliation first
  (AUTHORING_SOP §5.1 precedence B).
- Explicit NO_PUSH remains legal but requires a concrete authority
  source/reason recorded in the ticket; "no push authorization was granted"
  alone is not a standing prohibition.
- Obligations persist across rounds and chains until discharged by a proven
  0/0 state (HEAD == origin and clean tracked tree) or an explicit NO_PUSH
  authority source.
