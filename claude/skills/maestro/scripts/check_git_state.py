#!/usr/bin/env python3
"""Read Maestro's branch/index preconditions and resolve Git's exclude file.

Exit 0: these checks pass; 1: blocked state; 2: unable to inspect.
Owned-path overlap and worktree-root ignore rules are checked by the caller.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess


def git(repo, *args, allowed=(0,)):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True,
        env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"},
    )
    if result.returncode not in allowed:
        raise RuntimeError(result.stderr.strip() or "Git inspection failed")
    return result


def check_git_state(repo, working_branch):
    head = git(repo, "rev-parse", "--verify", "HEAD").stdout.strip()
    branch_result = git(repo, "symbolic-ref", "--quiet", "--short", "HEAD", allowed=(0, 1))
    branch = branch_result.stdout.strip() if branch_result.returncode == 0 else None
    index = git(repo, "diff", "--cached", "--quiet", "--ita-visible-in-index",
                "--no-ext-diff", "--no-textconv", "--ignore-submodules=none", "--",
                allowed=(0, 1))
    exclude = git(repo, "rev-parse", "--path-format=absolute", "--git-path",
                  "info/exclude").stdout.strip()
    blockers = []
    if branch is None:
        blockers.append("detached-head")
    elif branch != working_branch:
        blockers.append("wrong-branch")
    if index.returncode != 0:
        blockers.append("dirty-index")
    return {"head": head, "branch": branch, "index_clean": index.returncode == 0,
            "exclude_file": exclude, "blockers": blockers}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--working-branch", required=True,
                        help="Expected local branch name, as shown by git branch.")
    args = parser.parse_args()
    try:
        result = check_git_state(args.repo.resolve(), args.working_branch)
    except (OSError, RuntimeError) as error:
        print(json.dumps({"error": str(error)}))
        return 2
    print(json.dumps(result))
    return 1 if result["blockers"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
