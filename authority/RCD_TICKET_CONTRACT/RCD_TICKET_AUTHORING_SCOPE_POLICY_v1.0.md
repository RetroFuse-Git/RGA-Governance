# RCD Ticket Authoring Scope Policy v1.0

**Purpose:** Keep governed execution tickets bounded, executable, and token-efficient without weakening authority or evidence requirements.

## Core rule

Every ticket element must materially affect at least one of these functions:

1. authorization;
2. execution scope;
3. evidence collection;
4. acceptance or adjudication;
5. a credible halt condition.

If an element affects none of them, omit it.

The governing standard is the shortest ticket that is unambiguous, executable, and sufficient for closeout.

## Required ticket content

A ticket contains only what the task needs:

- canonical identity and routing fields required by the active schema;
- one concise authorized objective;
- exact authorized scope and paths;
- necessary starting state or dependencies;
- required outputs and evidence;
- measurable acceptance criteria;
- credible task-specific hazards and halt conditions;
- the execution-return contract.

Do not repeat the same requirement across the mission, stage contract, acceptance rules, negative controls, hard stops, and return contract. State it once in the field that governs it.

## Exclusion rules

Omit the following unless they are necessary to this specific task:

- provider, endpoint, model, transport, or tool names;
- historical narration already bound by a prior round or evidence artifact;
- generic safety prohibitions already enforced by admitted governance;
- hypothetical misconduct or failure modes without a demonstrated risk;
- tutorials, implementation speculation, explanatory essays, or defensive prose;
- repeated evidence requirements or synonymous acceptance rules;
- broad “do not” lists describing actions the executor has no reason or authority to perform.

Provider and transport details belong in runtime metadata unless the task is specifically about that provider or transport, or the selection materially affects authorization, cost, security, evidence identity, or acceptance.

## Exception test

Add an otherwise excluded constraint only when at least one condition is true:

- a prior observed failure demonstrates the need;
- a material task-specific risk is not controlled elsewhere;
- acceptance depends on the constrained behavior;
- the operator or admitted authority explicitly requires it.

When a safeguard is included because of a prior failure, bind it to the relevant finding or evidence instead of adding generalized defensive language.

## Scoping rules

- Name the ticket and chain for the governed objective, not the incidental provider, model, endpoint, or tool.
- Authorize one bounded outcome per ticket.
- Separate independent subsystems or independently rejectable changes into separate tickets.
- Treat provider fallback as a runtime change when objective, model capability, cost authority, security boundary, and evidence contract remain satisfied.
- Use a corrective continuation to change only the affected scope when a prior assumption fails; do not expand unrelated authority.
- Preserve immutable chain identity for continuity, but do not repeat obsolete assumptions in later ticket content.
- Do not turn review recommendations into implementation or validation authority.

## Ticket quality gate

Before emission, verify:

- each field passes the core-rule test;
- the objective is one sentence and has one bounded outcome;
- paths and mutation authority are exact;
- acceptance criteria are measurable;
- halt conditions are credible and task-specific;
- provider and transport details are absent unless justified;
- redundant prohibitions and repeated requirements are removed;
- the return contract requests only evidence needed for adjudication.

Failure of this quality gate requires ticket revision before emission.

## Applied example

For a Mnemosyne architecture review, the ticket identity and objective bind to the architecture review. The selected inference route is recorded as execution metadata. A provider outage or route change does not alter the review authority unless it changes the authorized model capability, cost boundary, security boundary, or evidence contract.

## Adoption note

This policy is ready for placement into the canonical RCD ticket-authoring authority set through the project's governed admission process.
