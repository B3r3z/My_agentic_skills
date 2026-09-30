#!/usr/bin/env python3
"""Link one agent's configuration without replacing existing local files."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agent", choices=("codex", "claude"))
    parser.add_argument(
        "--target", type=Path,
        help="Agent configuration directory; defaults to ~/.codex or ~/.claude.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Check and show links without writing.")
    args = parser.parse_args()

    repository = Path(__file__).resolve().parent.parent
    source_root = repository / args.agent
    default_target = Path.home() / f".{args.agent}"
    target_root = (args.target or default_target).expanduser().absolute()
    entries = [
        (source, target_root / "skills" / source.name)
        for source in sorted((source_root / "skills").iterdir())
        if source.is_dir() and (source / "SKILL.md").is_file()
    ]
    entries.extend(
        (source, target_root / "agents" / source.name)
        for source in sorted((source_root / "agents").glob("*.md"))
    )
    if not entries:
        parser.error(f"No configuration found in {source_root}")

    conflicts = []
    pending = []
    for source, target in entries:
        if target.is_symlink() and target.resolve() == source.resolve():
            continue
        if target.exists() or target.is_symlink():
            conflicts.append(target)
        else:
            pending.append((source, target))
        for parent in target.parents:
            if parent.exists():
                if not parent.is_dir():
                    conflicts.append(parent)
                break
            if parent.is_symlink():
                conflicts.append(parent)
                break

    if conflicts:
        parser.exit(1, "No changes made; existing configuration conflicts:\n" + "".join(
            f"  {path}\n" for path in sorted(set(conflicts))
        ))

    for source, target in pending:
        print(f"{'Would link' if args.dry_run else 'Link'} {target} -> {source}")
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(source, target_is_directory=source.is_dir())

    print(f"{args.agent}: {len(pending)} {'planned' if args.dry_run else 'created'}, "
          f"{len(entries) - len(pending)} already linked.")


if __name__ == "__main__":
    main()
