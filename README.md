# RGA _boot — Canonical Boot Authority Surface

This directory is the canonical source-authority surface for the RetroFuse
GEN7 boot system.  Artifacts here are the authoritative copies; the deployed
copies under `D:\RETROFUSE_OPS\_BOOT\GEN7\` are runtime shims/pointers.

## Structure

```
_boot/
├── authority/     — Governance, SAFEPOINT, Startup Contract, CR schemas
├── manifests/     — GEN7_BOOT_MANIFEST.json (integrity reference)
├── schemas/       — Boot receipt schema, CR schemas
├── receipts/      — Historical boot receipts (reference only)
└── README.md      — This file
```

## Authority Artifacts

| File | Role |
|------|------|
| `authority/OPS_CANONICAL_INDEX.md` | Authoritative index of all OPS surfaces |
| `authority/Governance_RetroFuse_v3.3.0.md` | Governance framework |
| `authority/AI_Contract_Safepoint_v3.2.json` | Safepoint contract |
| `authority/RetroFuse_SAFEPOINT_SOP_v3.2.md` | Safepoint SOP |
| `authority/RetroFuse_OPS_StartupContract_OPSCOO_v1.md` | Startup contract |
| `authority/RetroFuse_CR_Schemas_v3.1.1.json` | CR schemas |
| `authority/GEN7_CLI_Launcher_Contract.md` | CLI launcher contract |
| `authority/MODEL_ROUTING_REGISTRY.json` | Model routing registry |
| `authority/Gen7_Operations_Kernel_v1.3.md` | GEN7 operations kernel |
| `authority/CR_Event_Classification_Doctrine_v1.md` | CR event classification |
| `authority/OPS_Handoff_Pack_v1.3.md` | OPS handoff pack |
| `authority/README_FIRST.md` | First-read orientation |

## Preservation Model

- **RGA\_boot** is tracked in the RGA git repo (canonical source).
- **OPS_COO\Tools** remains deployed runtime only (not git-tracked).
- **\_BOOT\GEN7** contains compatibility shims pointing to RGA\_boot.
- Hash validation via `GEN7_BOOT_MANIFEST.json` in `manifests/`.

## Relationship to _BOOT\GEN7

The deployed `D:\RETROFUSE_OPS\_BOOT\GEN7\` directory contains compatibility
shims/pointers that reference these canonical copies.  The GEN7 bootloader
reads from `_BOOT\GEN7` for backward compatibility; the canonical source of
truth is here in RGA\_boot.
