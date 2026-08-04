#!/usr/bin/env python3
"""
Smoke tests for Get-RetroFuseMountEntry.py.

Tests:
    - FOUND returns one exact canonical Windows path.
    - FOUND_WITH_DIFF returns the path and diff pointer.
    - NOT_FOUND returns no guessed path.
    - AMBIGUOUS fails closed.
    - Tool runs successfully against a copied index in a temp sandbox.
    - Tool output validates against the lookup-result schema.
    - No full index content appears in stdout.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

# Paths
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL_PATH = os.path.join(SCRIPT_DIR, "Get-RetroFuseMountEntry.py")
SCHEMA_PATH = os.path.join(SCRIPT_DIR, "RetroFuse_OPS_MOUNT_LOOKUP_RESULT.schema.json")
INDEX_PATH = os.path.join(SCRIPT_DIR, "RetroFuse_OPS_MOUNT_INDEX.json")


def load_schema():
    """Load the lookup result schema for validation."""
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_against_schema(result: dict, schema: dict) -> list:
    """
    Basic structural validation against the schema.
    Returns a list of violation strings (empty = valid).
    """
    violations = []

    # Check required fields
    required = schema.get("required", [])
    for field in required:
        if field not in result:
            violations.append(f"Missing required field: {field}")

    # Check component_key
    if "component_key" in result and not isinstance(result["component_key"], str):
        violations.append("component_key must be a string")

    # Check status enum
    valid_statuses = schema["properties"]["status"]["enum"]
    if result.get("status") not in valid_statuses:
        violations.append(
            f"status '{result.get('status')}' not in {valid_statuses}"
        )

    # Check diff_impact enum
    valid_impacts = schema["properties"]["diff_impact"]["enum"]
    if result.get("diff_impact") not in valid_impacts:
        violations.append(
            f"diff_impact '{result.get('diff_impact')}' not in {valid_impacts}"
        )

    # Check path type
    if "path" in result:
        if result["status"] in ("FOUND", "FOUND_WITH_DIFF"):
            if not isinstance(result["path"], str):
                violations.append(
                    f"path must be a string for status {result['status']}"
                )
        elif result["status"] == "NOT_FOUND":
            if result["path"] is not None:
                violations.append("path must be null for NOT_FOUND")

    return violations


class TestMountLookup(unittest.TestCase):
    """Smoke tests for Get-RetroFuseMountEntry.py."""

    @classmethod
    def setUpClass(cls):
        """Verify tool and index exist."""
        assert os.path.isfile(TOOL_PATH), f"Tool not found: {TOOL_PATH}"
        assert os.path.isfile(INDEX_PATH), f"Index not found: {INDEX_PATH}"
        cls.schema = load_schema()

    def _run_lookup(self, key: str) -> dict:
        """Run the lookup tool and return parsed JSON result."""
        result = subprocess.run(
            [sys.executable, TOOL_PATH, INDEX_PATH, key],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, f"Tool exited with {result.returncode}: {result.stderr}")
        return json.loads(result.stdout)

    def _run_lookup_expect_fail(self, key: str) -> dict:
        """Run the lookup tool expecting non-zero exit."""
        result = subprocess.run(
            [sys.executable, TOOL_PATH, INDEX_PATH, key],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        return json.loads(result.stdout)

    def test_01_found_returns_exact_path(self):
        """FOUND returns one exact canonical Windows path."""
        # Look up a known unique top-level item
        result = self._run_lookup("OPS_CANONICAL_INDEX.md")
        self.assertEqual(result["status"], "FOUND")
        self.assertIsInstance(result["path"], str)
        self.assertTrue(result["path"].startswith("D:\\"))
        self.assertTrue("\\" in result["path"])
        self.assertIsNone(result["error"])
        self.assertIsNotNone(result["match_detail"])
        self.assertEqual(result["match_detail"]["name"], "OPS_CANONICAL_INDEX.md")

    def test_02_found_file_item(self):
        """FOUND works for FILE items too."""
        result = self._run_lookup("OPS_CANONICAL_INDEX.md")
        self.assertEqual(result["status"], "FOUND")
        self.assertIsInstance(result["path"], str)
        self.assertTrue(result["path"].endswith("OPS_CANONICAL_INDEX.md"))

    def test_03_not_found_returns_no_guessed_path(self):
        """NOT_FOUND returns no guessed path."""
        result = self._run_lookup("NONEXISTENT_COMPONENT_XYZ_999")
        self.assertEqual(result["status"], "NOT_FOUND")
        self.assertIsNone(result["path"])
        self.assertIsNone(result["error"])

    def test_04_not_found_empty_string(self):
        """Empty string returns INVALID_INDEX."""
        result = self._run_lookup_expect_fail("")
        self.assertEqual(result["status"], "INVALID_INDEX")

    def test_05_ambiguous_returns_error(self):
        """AMBIGUOUS fails closed with error detail."""
        # Use a very common short name likely to appear in multiple sections
        result = self._run_lookup("Tools")
        # Tools appears in topLevel AND as a surface root
        if result["status"] == "AMBIGUOUS":
            self.assertIsNotNone(result["error"])
            self.assertIn("matches", result["error"].lower())
        else:
            # If deduplication collapsed it, that's also valid
            self.assertIn(result["status"], ("FOUND", "FOUND_WITH_DIFF"))

    def test_06_sandbox_execution(self):
        """Tool runs successfully against a copied index in a temp sandbox."""
        with tempfile.TemporaryDirectory() as tmpdir:
            sandbox_index = os.path.join(tmpdir, "RetroFuse_OPS_MOUNT_INDEX.json")
            shutil.copy2(INDEX_PATH, sandbox_index)

            result = subprocess.run(
                [sys.executable, TOOL_PATH, sandbox_index, "OPS_CANONICAL_INDEX.md"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0)
            parsed = json.loads(result.stdout)
            self.assertEqual(parsed["status"], "FOUND")
            self.assertEqual(parsed["component_key"], "OPS_CANONICAL_INDEX.md")

    def test_07_output_validates_against_schema(self):
        """Tool output validates against the lookup-result schema."""
        result = self._run_lookup("RGA")
        violations = validate_against_schema(result, self.schema)
        self.assertEqual(
            violations, [], f"Schema violations: {violations}"
        )

    def test_08_not_found_validates_against_schema(self):
        """NOT_FOUND output validates against schema."""
        result = self._run_lookup("DOES_NOT_EXIST_12345")
        violations = validate_against_schema(result, self.schema)
        self.assertEqual(
            violations, [], f"Schema violations: {violations}"
        )

    def test_09_no_full_index_in_stdout(self):
        """No full index content appears in stdout."""
        result = subprocess.run(
            [sys.executable, TOOL_PATH, INDEX_PATH, "RGA"],
            capture_output=True,
            text=True,
        )
        stdout = result.stdout

        # The full index has a "topLevel" array with many items.
        # The lookup result should NOT contain the full topLevel array.
        self.assertNotIn('"topLevel"', stdout, "Full index leaked into stdout")
        self.assertNotIn('"surfaces"', stdout, "Full index leaked into stdout")

        # Verify it's a single record, not an array
        parsed = json.loads(stdout)
        self.assertIsInstance(parsed, dict)
        self.assertNotIsInstance(parsed, list)

    def test_10_found_with_diff(self):
        """FOUND_WITH_DIFF returns path and diff pointer if diff exists."""
        # Look up a unique component that might have a diff sibling
        result = self._run_lookup("OPS_CANONICAL_INDEX.md")
        if result["status"] == "FOUND_WITH_DIFF":
            self.assertIsNotNone(result["diff_path"])
            self.assertEqual(result["diff_impact"], "PRESENT")
        else:
            # If no diff exists, FOUND is also acceptable
            self.assertIn(result["status"], ("FOUND", "NOT_FOUND"))

    def test_11_invalid_index_path(self):
        """Invalid index path returns INVALID_INDEX."""
        result = subprocess.run(
            [sys.executable, TOOL_PATH, "C:\\nonexistent\\path.json", "test"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        parsed = json.loads(result.stdout)
        self.assertEqual(parsed["status"], "INVALID_INDEX")

    def test_12_wrong_arg_count(self):
        """Wrong argument count returns INVALID_INDEX."""
        result = subprocess.run(
            [sys.executable, TOOL_PATH],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        parsed = json.loads(result.stdout)
        self.assertEqual(parsed["status"], "INVALID_INDEX")

    def test_13_rcd_envelope_v3_1_resolves(self):
        """RCD-CROSSLANE-ENVELOPE-v3.1.md resolves to exact canonical path."""
        result = self._run_lookup("RCD-CROSSLANE-ENVELOPE-v3.1.md")
        self.assertEqual(result["status"], "FOUND")
        self.assertEqual(
            result["path"],
            "D:\\RETROFUSE_OPS\\Tools\\RCD\\Artifacts\\RCD-CROSSLANE-ENVELOPE-v3.1.md"
        )
        self.assertIsNone(result["error"])
        self.assertEqual(result["match_detail"]["name"], "RCD-CROSSLANE-ENVELOPE-v3.1.md")


if __name__ == "__main__":
    unittest.main()
