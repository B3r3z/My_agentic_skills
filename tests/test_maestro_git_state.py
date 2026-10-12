"""Exercise the shipped preflight against isolated, real Git repositories."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELPERS = [ROOT / agent / "skills/maestro/scripts/check_git_state.py"
           for agent in ("codex", "claude")]


class GitStateTest(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="maestro-git-test-")
        self.addCleanup(self.scratch.cleanup)
        self.base = Path(self.scratch.name).resolve()
        self.repo = self.base / "repository with spaces"
        self.repo.mkdir()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_AUTHOR_NAME="Test", GIT_AUTHOR_EMAIL="test@example.invalid",
                        GIT_COMMITTER_NAME="Test", GIT_COMMITTER_EMAIL="test@example.invalid")
        self.git("init", "-b", "main")
        (self.repo / "task.txt").write_text("original task\n")
        (self.repo / "unrelated.txt").write_text("original user file\n")
        self.git("add", ".")
        self.git("commit", "-m", "fixture baseline")

    def git(self, *args, repo=None):
        return subprocess.run(["git", "-C", str(repo or self.repo), *args],
                              env=self.env, check=True, capture_output=True).stdout

    def check_helpers(self, expected_code, repo=None, branch="main"):
        results = []
        for helper in HELPERS:
            result = subprocess.run(
                [sys.executable, "-B", str(helper), "--repo", str(repo or self.repo),
                 "--working-branch", branch], env=self.env,
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, expected_code,
                             f"{helper.relative_to(ROOT)}: {result.stderr or result.stdout}")
            results.append(json.loads(result.stdout))
        self.assertEqual(results[0], results[1])
        return results[0]

    def test_clean_checkout_reports_resolved_exclude_path(self):
        result = self.check_helpers(0)
        self.assertTrue(result["index_clean"])
        self.assertEqual(result["branch"], "main")
        self.assertEqual(result["head"], self.git("rev-parse", "HEAD").decode().strip())
        self.assertEqual(Path(result["exclude_file"]), self.repo / ".git/info/exclude")
        self.assertEqual(result["blockers"], [])

    def test_unrelated_staged_change_blocks_without_touching_user_work(self):
        (self.repo / "unrelated.txt").write_text("staged user change\n")
        self.git("add", "unrelated.txt")
        (self.repo / "unrelated.txt").write_text("later unstaged user change\n")
        before = (self.git("diff", "--cached", "--binary"), self.git("diff", "--binary"),
                  (self.repo / ".git/index").read_bytes())
        result = self.check_helpers(1)
        self.assertFalse(result["index_clean"])
        self.assertIn("dirty-index", result["blockers"])
        self.assertEqual(before, (self.git("diff", "--cached", "--binary"),
                                  self.git("diff", "--binary"),
                                  (self.repo / ".git/index").read_bytes()))

    def test_unstaged_and_untracked_files_are_left_for_scope_check(self):
        (self.repo / "unrelated.txt").write_text("unstaged user change\n")
        (self.repo / "user note.txt").write_text("untracked user note\n")
        before = self.git("status", "--porcelain=v1", "-z")
        result = self.check_helpers(0)
        self.assertTrue(result["index_clean"])
        self.assertEqual(before, self.git("status", "--porcelain=v1", "-z"))

    def test_existing_linked_worktree_resolves_common_exclude_file(self):
        worktree = self.base / "linked worktree"
        self.git("worktree", "add", "-b", "working", str(worktree))
        self.assertTrue((worktree / ".git").is_file())
        result = self.check_helpers(0, repo=worktree, branch="working")
        self.assertEqual(Path(result["exclude_file"]), self.repo / ".git/info/exclude")
        # The returned path must be usable and shared with the original checkout.
        with Path(result["exclude_file"]).open("a") as stream:
            stream.write("\n/.scratch/maestro/\n")
        self.git("check-ignore", ".scratch/maestro/run/worktrees/", repo=worktree)

    def test_recheck_catches_index_change_after_dispatch(self):
        self.check_helpers(0)
        (self.repo / "unrelated.txt").write_text("staged during agent work\n")
        self.git("add", "unrelated.txt")
        self.assertIn("dirty-index", self.check_helpers(1)["blockers"])

    def test_intent_to_add_entry_also_blocks_merging(self):
        (self.repo / "draft.txt").write_text("unfinished user work\n")
        self.git("add", "--intent-to-add", "draft.txt")
        index = (self.repo / ".git/index").read_bytes()
        self.assertIn("dirty-index", self.check_helpers(1)["blockers"])
        self.assertEqual(index, (self.repo / ".git/index").read_bytes())

    def test_wrong_branch_blocks(self):
        self.assertIn("wrong-branch", self.check_helpers(1, branch="other")["blockers"])

    def test_detached_head_blocks(self):
        self.git("checkout", "--detach")
        result = self.check_helpers(1)
        self.assertIsNone(result["branch"])
        self.assertIn("detached-head", result["blockers"])

    def test_non_repository_returns_an_error_not_a_clean_result(self):
        result = self.check_helpers(2, repo=self.base)
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
