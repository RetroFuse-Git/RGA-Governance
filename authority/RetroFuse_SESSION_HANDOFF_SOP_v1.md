# RetroFuse Session Handoff SOP v1

**Authority:** Mandatory
**Scope:** All projects, all lanes, all sessions
**Canonical Path:** D:\RETROFUSE_OPS\RGA\authority\RetroFuse_SESSION_HANDOFF_SOP_v1.md
**Date:** 2026-07-14

## 1. Purpose

Defines the governed session lifecycle: how an AI session must hydrate from the
project handoff plan, execute without restarting completed work, and preserve
unresolved state for the successor. This SOP applies to every project root,
every lane, and every session regardless of model or tool.

## 2. Binding Rules

### 2.1 Every project root MUST contain a plan.md

The file `plan.md` at the active project root is the authoritative session
handoff artifact. It carries:

- Current project and authority context
- Completed work (tickets, commits, artifacts, receipts)
- Active unresolved questions and contradictory findings
- Exact next speaker and next question
- Missing round-table legs
- Known risks and deferred items
- Key artifact paths and hashes
- No-restart-from-scratch warning
- Successor rehydration instructions

If `plan.md` does not exist, the session MUST create it before retirement.

### 2.2 READ FIRST, ACT SECOND

On every new session startup, the AI MUST:

1. Read `plan.md` from the active project root before taking any action.
2. Load the authority stack declared in the plan or canonical index.
3. Hydrate from the latest Daily Bundle.
4. Identify the exact unresolved state, next speaker, and next question.
5. Report what was found in the plan before proposing any action.

### 2.3 NEVER RESTART COMPLETED WORK

Work marked COMPLETE in the plan must not be restarted, re-audited,
re-implemented, or re-proven. If evidence conflicts with the plan, surface
the contradiction as a finding — do not silently redo the work.

### 2.4 RESUME FROM EXACT UNRESOLVED STATE

The successor inherits:
- The exact unresolved question(s)
- The next speaker assignment
- All captured advisory responses
- All proposed but unfinished stages
- The current round status

Do not re-frame, broaden, narrow, or skip unresolved items.

### 2.5 NEVER EMIT WITHOUT EXPLICIT AUTHORITY

No Daily Bundle delivery, backend provider call, CDP injection, DOM
submission, or transport dispatch may occur without an explicit separate
execution ticket. Transport selection is governed by RCD-CLI-ROUTING-CONTRACT.

### 2.6 REPORT EVIDENCE, NOT ASSUMPTIONS

Every claim must cite a source artifact, receipt, hash, path, or explicit
operator statement. Mark inferences, assumptions, and gaps explicitly.

### 2.7 UPDATE PLAN BEFORE RETIREMENT

On session end, the AI MUST update `plan.md` with:
- Current round-table state
- Newly completed work
- Updated unresolved questions
- Next speaker assignment
- Any new risks, findings, or deferred items
- Updated artifact paths and hashes
- Successor rehydration instructions

## 3. Plan Template (Minimum)

```markdown
# <Project> — Session Handoff Plan

**Date:** YYYY-MM-DD
**Session:** <Lane> with <Model>
**Status:** ACTIVE|ROUND_INCOMPLETE|RETIRING

## Authority Context
## Completed Work
## Active Round Table State
## Unresolved Questions
## Next Speaker and Next Question
## Key Artifact Paths
## Known Risks
## Successor Instructions
## DO NOT RESTART FROM SCRATCH
```

## 4. Verification

Before retirement, the AI MUST:
- Read back the exact canonical path of the written plan
- Report file size, modification time, and SHA-256 hash
- Confirm the plan contains unresolved state and successor instructions
- Confirm no temp-only or sandbox copy was treated as authoritative

## 5. Compatibility

This SOP is subordinate to:
- Governance_RetroFuse_v3.3.1
- RetroFuse_SAFEPOINT_SOP_v3.2
- AI_Contract_Safepoint_v3.2
- OPS_CANONICAL_INDEX.md

It does not override transport selection, feedback obligation, or round
lifecycle rules. It governs session hydration, resumption, and retirement
only.
