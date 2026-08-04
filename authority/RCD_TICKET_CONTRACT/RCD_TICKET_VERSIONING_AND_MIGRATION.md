# RCD Ticket Versioning and Migration v1.0

## Active Versions
- RCD-ENVELOPE-v3: Current operational (installed, active)
- RCD-ENVELOPE-v4: Future (designed, not yet activated)

## Compatibility
v4 schemas accept v3 tickets with normalization. v3 consumers are unchanged during shadow mode.

## Migration Path
1. Install v4 authority family (Ticket 3 -- this ticket)
2. Implement shadow validator (Ticket 4)
3. Run shadow comparison for 30 days
4. Activate v4 admission when shadow shows <5% legacy tickets

## Rollback
Restore from pre-install Safepoint. Remove RCD_TICKET_CONTRACT directory. Restore original manifest, index, and README_FIRST.
