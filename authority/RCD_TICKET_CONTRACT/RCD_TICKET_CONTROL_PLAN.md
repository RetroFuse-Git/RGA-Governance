# RCD Ticket Control Plan v1.0

## Primary Metric
First-Pass Executable Yield: Target >=95% (baseline ~65-70%)

## Control Gates
- Pre-admission: Schema validation, envelope-class check, lookup resolution
- Post-admission: Authority-effect validation, mutation boundary check
- Pre-closeout: Persistence evidence, re-entry proof
- Pre-seal: All acceptance criteria met, no hard stops violated

## Audit Frequency
Every ticket admission. Every closeout. Every seal.

## Failure Response
- BLOCKED: Return to author with specific defect list
- NEEDS_MORE: Return with missing field inventory
- ACCEPT_WITH_WARNINGS: Admit with logged compatibility warnings
