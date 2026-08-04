#!/usr/bin/env python3
"""
Get-RetroFuseMountEntry.py — Thin sandbox-usable lookup tool for the
biweekly OPS mount index.

Usage:
    python Get-RetroFuseMountEntry.py <index_path> <component_key>

Output:
    Single JSON record conforming to RetroFuse_OPS_MOUNT_LOOKUP_RESULT.schema.json.
    Never prints the full mount index.

Exit codes:
    0 — lookup completed (status may be FOUND, NOT_FOUND, etc.)
    1 — index file unreadable or malformed
"""

import json
import sys
import os


def load_index(index_path: str) -> dict | None:
    """Load and validate the mount index JSON file."""
    if not os.path.isfile(index_path):
        return None
    try:
        with open(index_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        if not isinstance(data, dict) or "schema" not in data:
            return None
        return data
    except (json.JSONDecodeError, PermissionError, OSError):
        return None


def search_section(section, key: str, case_sensitive: bool = True) -> list:
    """Search a section of the index for items matching the key."""
    matches = []
    if not isinstance(section, list):
        return matches

    for item in section:
        if not isinstance(item, dict):
            continue
        name = item.get("name", "")
        if case_sensitive:
            if name == key:
                matches.append(item)
        else:
            if name.lower() == key.lower():
                matches.append(item)
    return matches


def search_surfaces(surfaces, key: str, case_sensitive: bool = True) -> list:
    """Search all surface items for a matching name."""
    matches = []
    if not isinstance(surfaces, list):
        return matches
    for surface in surfaces:
        if not isinstance(surface, dict):
            continue
        items = surface.get("items", [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            name = item.get("name", "")
            if case_sensitive:
                if name == key:
                    item_copy = dict(item)
                    item_copy["section"] = f"surfaces/{surface.get('root', 'unknown')}"
                    matches.append(item_copy)
            else:
                if name.lower() == key.lower():
                    item_copy = dict(item)
                    item_copy["section"] = f"surfaces/{surface.get('root', 'unknown')}"
                    matches.append(item_copy)
    return matches


def search_anchors(anchors, key: str, case_sensitive: bool = True) -> list:
    """Search anchors for a matching path component."""
    matches = []
    if not isinstance(anchors, list):
        return matches
    for anchor in anchors:
        if not isinstance(anchor, dict):
            continue
        path = anchor.get("path", "")
        name = os.path.basename(path) if path else ""
        if case_sensitive:
            if name == key or path == key:
                matches.append({"name": name, "path": path, "section": "anchors"})
        else:
            if name.lower() == key.lower() or path.lower() == key.lower():
                matches.append({"name": name, "path": path, "section": "anchors"})
    return matches


def lookup(index: dict, key: str) -> dict:
    """
    Perform a lookup for component_key in the mount index.
    Returns a result dict conforming to the lookup schema.
    """
    result = {
        "component_key": key,
        "path": None,
        "diff_path": None,
        "diff_impact": "NONE",
        "status": "NOT_FOUND",
        "match_detail": None,
        "error": None,
    }

    if not isinstance(key, str) or not key.strip():
        result["status"] = "INVALID_INDEX"
        result["error"] = "component_key must be a non-empty string"
        return result

    key = key.strip()

    # Canonical-root aliases (documented, not inferred).
    # These map well-known component keys to their canonical OPS roots per
    # OPS_CANONICAL_INDEX.md even when the index's folder basename differs
    # (e.g. the OPS root folder is "RETROFUSE_OPS", not "OPS").
    CANONICAL_ROOT_ALIASES = {
        "OPS": r"D:\RETROFUSE_OPS",
        "OPS_ROOT": r"D:\RETROFUSE_OPS",
    }
    if key in CANONICAL_ROOT_ALIASES:
        canonical_path = CANONICAL_ROOT_ALIASES[key]
        # Prefer a real FOUND match from the index; fall back to the alias.
        result["path"] = canonical_path
        result["status"] = "FOUND"
        result["match_detail"] = {
            "name": key,
            "kind": "DIR",
            "path": canonical_path,
            "section": "canonical_alias",
            "note": "Resolved via canonical-root alias (OPS_CANONICAL_INDEX.md).",
        }
        return result

    all_matches = []

    # Search topLevel
    top_matches = search_section(index.get("topLevel", []), key)
    for m in top_matches:
        m["section"] = "topLevel"
    all_matches.extend(top_matches)

    # Search surfaces
    surface_matches = search_surfaces(index.get("surfaces", []), key)
    all_matches.extend(surface_matches)

    # Search anchors
    anchor_matches = search_anchors(index.get("anchors", []), key)
    all_matches.extend(anchor_matches)

    # Search recent by filename
    recent = index.get("recent", [])
    if isinstance(recent, list):
        for item in recent:
            if not isinstance(item, dict):
                continue
            path = item.get("path", "")
            name = os.path.basename(path) if path else ""
            if name == key:
                all_matches.append({
                    "name": name,
                    "path": path,
                    "lastWriteTime": item.get("lastWriteTime"),
                    "bytes": item.get("bytes"),
                    "kind": "FILE",
                    "section": "recent",
                })

    if not all_matches:
        return result

    if len(all_matches) > 1:
        # Check if all paths are the same (duplicate entries, same result)
        unique_paths = set(m.get("path") for m in all_matches if m.get("path"))
        if len(unique_paths) == 1:
            # Deduplicate — same path found in multiple sections
            single = all_matches[0]
            result["path"] = single.get("path")
            result["status"] = "FOUND"
            result["match_detail"] = {
                "name": single.get("name"),
                "kind": single.get("kind", "DIR"),
                "lastWriteTime": single.get("lastWriteTime"),
                "bytes": single.get("bytes"),
                "path": single.get("path"),
                "section": single.get("section", "unknown"),
            }
            return result

        result["status"] = "AMBIGUOUS"
        result["error"] = (
            f"Found {len(all_matches)} matches for key '{key}'. "
            f"Paths: {[m.get('path') for m in all_matches[:10]]}"
        )
        return result

    # Single match
    match = all_matches[0]
    result["path"] = match.get("path")
    result["status"] = "FOUND"
    result["match_detail"] = {
        "name": match.get("name"),
        "kind": match.get("kind", "DIR"),
        "lastWriteTime": match.get("lastWriteTime"),
        "bytes": match.get("bytes"),
        "path": match.get("path"),
        "section": match.get("section", "unknown"),
    }

    # Check for diff path (convention: look for _diff or _delta sibling)
    if match.get("path"):
        base_dir = os.path.dirname(match["path"])
        base_name = os.path.splitext(os.path.basename(match["path"]))[0]
        diff_candidates = [
            os.path.join(base_dir, f"{base_name}_diff.md"),
            os.path.join(base_dir, f"{base_name}_delta.md"),
            os.path.join(base_dir, f"_diff_{base_name}.md"),
        ]
        for dc in diff_candidates:
            if os.path.isfile(dc):
                result["diff_path"] = dc
                result["diff_impact"] = "PRESENT"
                result["status"] = "FOUND_WITH_DIFF"
                break

    return result


def main():
    if len(sys.argv) != 3:
        print(
            json.dumps(
                {
                    "component_key": "",
                    "path": None,
                    "diff_path": None,
                    "diff_impact": "NONE",
                    "status": "INVALID_INDEX",
                    "match_detail": None,
                    "error": (
                        "Usage: python Get-RetroFuseMountEntry.py "
                        "<index_path> <component_key>"
                    ),
                },
                indent=2,
            )
        )
        sys.exit(1)

    index_path = sys.argv[1]
    component_key = sys.argv[2]

    index = load_index(index_path)
    if index is None:
        print(
            json.dumps(
                {
                    "component_key": component_key,
                    "path": None,
                    "diff_path": None,
                    "diff_impact": "NONE",
                    "status": "INVALID_INDEX",
                    "match_detail": None,
                    "error": (
                        f"Cannot read or parse index at: {index_path}"
                    ),
                },
                indent=2,
            )
        )
        sys.exit(1)

    result = lookup(index, component_key)
    print(json.dumps(result, indent=2))

    if result["status"] in ("INVALID_INDEX",):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
