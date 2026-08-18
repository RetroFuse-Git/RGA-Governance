# RCD Ticket Envelope Classes v1.1

Selector-era class contracts (authoritative machine-readable form:
`RCD_SELECTOR_MANIFEST_v1` `class_contracts`; this table is the human-readable
rendering). EXECUTION_RETURN and EXECUTION_TICKET are proven operational
classes (198x / 131x in ExchangeRounds evidence).

| Class | Required | Forbidden | Purpose |
|-------|----------|-----------|---------|
| INITIAL_TICKET | schema_version, ticket_id, chain_root_id, title, task_class, authority_effect, mission, path_block, acceptance_rules, hard_stops, stage_id, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | prior_round_id, correction_target | Starts a governed chain |
| EXECUTION_TICKET | schema_version, ticket_id, chain_root_id, task_class, authority_effect, stage_id, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | -- | Authorizes execution of a bounded stage (operational class) |
| IMPLEMENTATION_ROUND | schema_version, ticket_id, chain_root_id, parent_round_id, stage_id, authority_effect, single_task_boundary, required_return, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | -- | Executes a bounded stage |
| CORRECTIVE_ROUND | schema_version, ticket_id, chain_root_id, parent_round_id, correction_target, authority_effect, stage_id, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | -- | Repairs a specific failure |
| WORKER_RETURN | schema_version, ticket_id, chain_root_id, parent_round_id, round_status, evidence, next_stage_recommendation, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | mutation_rules | Returns execution evidence |
| CLOSEOUT_REQUEST | schema_version, ticket_id, chain_root_id, evidence, persistence_proof, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | mutation_rules | Requests authority QC |
| EXECUTION_RETURN | schema_version, ticket_id, chain_root_id, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy, stage_id, evidence | mutation_rules | Returns governed execution evidence for authority QC (operational class) |
| AUTHORITY_DECISION | schema_version, ticket_id, chain_root_id, decision, accepted_evidence, next_authorized_stage, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | -- | Returns authority ruling |
| AUTHORITY_SEAL | schema_version, ticket_id, chain_root_id, authority_effect, terminal_verdict, chain_status, sealed_findings, classification, status, execution_lane, delivery_mode, routing_mode, cdp_targets, git_closeout_policy | -- | Closes a chain |
