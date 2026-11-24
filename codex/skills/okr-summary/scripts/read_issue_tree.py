#!/usr/bin/env python3
"""Read a GitHub issue, its descendants and issue comments as JSON Lines."""

import argparse
import json
import re
import subprocess
import sys
from collections import deque
from urllib.parse import urlsplit


def issue_endpoint(url):
    parsed = urlsplit(url)
    match = re.fullmatch(r"/([\w.-]+)/([\w.-]+)/issues/([1-9][0-9]*)/?", parsed.path)
    if parsed.scheme != "https" or not parsed.hostname or not match:
        raise ValueError(f"Expected a full HTTPS GitHub issue URL, got {url!r}")
    owner, repository, number = match.groups()
    return parsed.hostname, f"repos/{owner}/{repository}/issues/{number}"


def gh_get(host, endpoint, *, paginate=False):
    command = ["gh", "api", "--method", "GET", "--hostname", host]
    if paginate:
        command.extend(["--paginate", "--slurp"])
    result = subprocess.run([*command, endpoint], check=True, stdout=subprocess.PIPE)
    return json.loads(result.stdout)


def read_list(host, endpoint, expected):
    if expected == 0:
        return []
    pages = gh_get(host, f"{endpoint}?per_page=100", paginate=True)
    items = [item for page in pages for item in page]
    if expected is not None and len(items) != expected:
        raise ValueError(f"{endpoint} reported {expected} items, returned {len(items)}")
    return items


def read_issue_tree(root_url):
    pending = deque([gh_get(*issue_endpoint(root_url))])
    seen = set()
    while pending:
        issue = pending.popleft()
        url = issue["html_url"]
        if url in seen:
            continue
        seen.add(url)
        host, endpoint = issue_endpoint(url)
        child_summary = issue.get("sub_issues_summary") or {}
        children = read_list(host, f"{endpoint}/sub_issues", child_summary.get("total"))
        comments = read_list(host, f"{endpoint}/comments", issue.get("comments"))
        yield {
            "url": url,
            "title": issue["title"],
            "body": issue["body"],
            "state": issue["state"],
            "state_reason": issue.get("state_reason"),
            "milestone": (issue.get("milestone") or {}).get("title"),
            "created_at": issue["created_at"],
            "closed_at": issue.get("closed_at"),
            "children": [child["html_url"] for child in children],
            "comments": [
                {
                    "url": comment["html_url"],
                    "created_at": comment["created_at"],
                    "updated_at": comment["updated_at"],
                    "body": comment["body"],
                }
                for comment in comments
            ],
        }
        pending.extend(children)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("issue_url", help="Full GitHub issue URL")
    args = parser.parse_args()
    try:
        for issue in read_issue_tree(args.issue_url):
            print(json.dumps(issue, ensure_ascii=False))
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        sys.exit(f"Incomplete issue tree: {error}")


if __name__ == "__main__":
    main()
