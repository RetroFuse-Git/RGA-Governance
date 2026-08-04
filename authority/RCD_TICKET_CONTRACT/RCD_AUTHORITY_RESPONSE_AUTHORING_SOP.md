# RCD Authority Response Authoring SOP v1.0

## Purpose
This SOP defines how ChatGPT (authority QC) must respond to RCD Conductor
authority-continuation requests. The parser is STRICT JSON ONLY. Fail closed.

## Rule 1: Return ONE Complete JSON Object Only
No natural language. No markdown. No "JSON" prefix. No ``` fences.
Just: { "schema_version": "RCD-ENVELOPE-v3", ... }

## Rule 2: Always Required Fields (every response)
- schema_version: "RCD-ENVELOPE-v3"
- classification: SEALED_TERMINAL | NEXT_ROUND_AUTHORIZED | HARD_HALT | OPERATOR_ACTION_REQUIRED
- status: TERMINAL_SEAL_GRANTED | NEXT_ROUND_AUTHORIZED | BLOCKED | OPERATOR_ACTION_REQUIRED
- ticket_id: copy exactly from request
- chain_root_id: copy exactly from request
- stage_id: copy exactly from request

## Rule 3: Correlation Fields (when following a provider round)
- round_id: copy exactly from request
- nonce: copy exactly from request

## Rule 4: Terminal Seal (CLOSEOUT response)
Required fields:
- terminal_seal: "GRANTED" (or "SEALED" or "TRUE")
- authority_effect: "SEALED_TERMINAL"
Optional but recommended:
- authority_verdict: "ACCEPT" (or "ACCEPTED", "PASS", "SEALED_TERMINAL")

## Rule 5: Next Round Authorization (CONTINUATION response)
Required additional fields:
- next_expected_stage: the next stage_id to execute
- next_ticket_envelope: { complete RCD-ENVELOPE-v3 JSON for next round }
REQUIRED: `next_ticket_envelope.stage_id` MUST equal `next_expected_stage` (the
NEXT round's stage), NOT the current round's stage. The next envelope describes
the round to be executed after this one; its stage_id must be the stage that
round will run. Do not echo the current round's stage_id into the next envelope.

## Rule 6: Hard Halt
classification: "HARD_HALT" or status: "BLOCKED"

## Example: Terminal Seal
{
  "schema_version": "RCD-ENVELOPE-v3",
  "classification": "SEALED_TERMINAL",
  "status": "TERMINAL_SEAL_GRANTED",
  "ticket_id": "OPS-20260729-EXAMPLE-001-R01",
  "chain_root_id": "OPS-20260729-EXAMPLE-001",
  "stage_id": "R01_DO_THING",
  "authority_effect": "SEALED_TERMINAL",
  "terminal_seal": "GRANTED",
  "authority_verdict": "ACCEPT"
}

## Example: Next Round
{
  "schema_version": "RCD-ENVELOPE-v3",
  "classification": "NEXT_ROUND_AUTHORIZED",
  "status": "NEXT_ROUND_AUTHORIZED",
  "ticket_id": "OPS-20260729-EXAMPLE-001-R01",
  "chain_root_id": "OPS-20260729-EXAMPLE-001",
  "stage_id": "R01_DO_THING",
  "next_expected_stage": "R02_DO_NEXT_THING",
  "next_ticket_envelope": { "schema_version": "RCD-ENVELOPE-v3", "ticket_id": "OPS-20260729-EXAMPLE-001-R02", ... }
}
