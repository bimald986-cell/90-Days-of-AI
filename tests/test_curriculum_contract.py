"""Offline contract checks for the ongoing AI Learning Journey."""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CURRICULUM = json.loads((ROOT / "CURRICULUM.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))


class CurriculumContractTests(unittest.TestCase):
    def test_readme_uses_ongoing_curriculum_language(self):
        lowered = README.lower()
        self.assertIn("ai learning journey", lowered)
        self.assertIn("continues", lowered)
        self.assertNotIn("90 days", lowered)
        self.assertNotIn("90-day", lowered)

    def test_curriculum_has_a_foundation_and_ongoing_tracks(self):
        self.assertEqual(CURRICULUM["program"], "AI Learning Journey")
        self.assertIn("beginning, not the end", CURRICULUM["philosophy"])
        self.assertTrue(CURRICULUM["foundation"])
        self.assertTrue(CURRICULUM["ongoing_tracks"])

    def test_state_preserves_completed_days_without_marking_current_day_done(self):
        completed = STATE["completed_days"]
        self.assertEqual(completed, sorted(set(completed)))
        self.assertGreater(STATE["current_day"], max(completed))
        self.assertNotIn(STATE["current_day"], completed)
        self.assertEqual(STATE["status"], "ACTIVE")
        self.assertGreaterEqual(STATE["metrics"]["sessions_completed"], len(completed))
        self.assertIsNone(STATE["metrics"]["current_streak"])


if __name__ == "__main__":
    unittest.main()
