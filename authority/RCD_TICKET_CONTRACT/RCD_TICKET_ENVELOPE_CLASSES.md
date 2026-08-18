# RCD Ticket Envelope Classes v1.0

| Class | Required | Forbidden | Purpose |
|-------|----------|-----------|---------|
| INITIAL_TICKET | schema_version, ticket_id, chain_root_id, title, task_class, authority_effect, mission, path_block, acceptance_rules, hard_stops | prior_round_id, correction_target | Starts a governed chain |
| IMPLEMENTATION_ROUND | schema_version, ticket_id, chain_root_id, parent_round_id, stage_id, authority_effect, single_task_boundary, required_return | -- | Executes a bounded stage |
| CORRECTIVE_ROUND | schema_version, ticket_id, chain_root_id, parent_round_id, correction_target, authority_effect | -- | Repairs a specific failure |
| WORKER_RETURN | schema_version, ticket_id, chain_root_id, parent_round_id, round_status, evidence, next_stage_recommendation | mutation_rules | Returns execution evidence |
| CLOSEOUT_REQUEST | schema_version, ticket_id, chain_root_id, evidence, persistence_proof | mutation_rules | Requests authority QC |
| AUTHORITY_DECISION | schema_version, ticket_id, chain_root_id, decision, accepted_evidence, next_authorized_stage | -- | Returns authority ruling |
| AUTHORITY_SEAL | schema_version, ticket_id, chain_root_id, authority_effect, terminal_verdict, chain_status, sealed_findings | -- | Closes a chain |
