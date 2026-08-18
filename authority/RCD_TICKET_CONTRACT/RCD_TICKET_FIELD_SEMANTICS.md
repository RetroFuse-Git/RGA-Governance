# RCD Ticket Field Semantics v1.0

## Field Ownership
RGA owns: schema_version, authority_effect, authority posture, acceptance rules.
RCD owns: routing_mode, delivery_mode, cdp_targets, git_closeout_policy, mutation_rules.
Shared: ticket_id, chain_root_id, stage_id, mission.
`stage_id` is REQUIRED on every ticket envelope (round-local, per RCD_TICKET_AUTHORING_SOP §3).
`cdp_targets` is REQUIRED and MUST be a non-empty list drawn only from {chatgpt, gemini, deepseek}.
`rcd_cli` is the execution lane, not a CDP delivery target; it MUST NOT appear in cdp_targets.

## Duplication Rule
ticket_id and chain_root_id may appear at top-level and inside payload for consumer compatibility. Values MUST be identical. Any divergence is a BLOCKED validation error.

## Nullability
Optional fields must be accessed through safe presence checks. Missing optional fields normalize to null, not empty string. StrictMode consumers require explicit null guards.

## Immutable Fields
chain_root_id and prior_round_id are immutable once set. stage_id is round-local.

## Forbidden Combinations
- authority_effect=NONE with mutation_rules containing non-empty allowed list
- git_closeout_policy=report_only with commit in authorized actions
- terminal_verdict=SEALED_TERMINAL with non-null next_expected_stage
