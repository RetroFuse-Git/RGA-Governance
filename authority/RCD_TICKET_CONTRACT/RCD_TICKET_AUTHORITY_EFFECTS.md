# RCD Ticket Authority Effects v1.0

| Effect | Meaning | Allows |
|--------|---------|--------|
| NONE | No authority granted | Read-only discovery, design, analysis |
| READ_ONLY_ANALYSIS_AUTHORIZED | May read and analyze | File reads, hashing, evidence creation |
| BOUNDED_IMPLEMENTATION_AUTHORIZED | May create bounded code | New files in authorized paths |
| BOUNDED_DELIVERY_AUTHORIZED | May perform governed delivery | Exactly-one provider dispatch |
| AUTHORITY_DOCUMENT_MUTATION_AUTHORIZED | May modify authority docs | RGA authority file installation |
| SEALED_TERMINAL | Chain closed | No further work on this chain |

## Mutation Consequences
authority_effect maps to allowed operations in mutation_rules.allowed.
authority_effect=NONE prohibits all mutation regardless of mutation_rules content.
