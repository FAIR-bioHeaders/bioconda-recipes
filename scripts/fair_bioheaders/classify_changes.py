"""Conservatively route owned documentation/CI-only diffs away from recipe builds."""
import argparse
import os
from pathlib import Path
import re
import subprocess

OWNED_FILES = {"AGENTS.md", ".github/workflows/fair-bioheaders-docs.yml", ".github/workflows/PR.yml"}
OWNED_PREFIXES = ("docs/fair-bioheaders/", "scripts/fair_bioheaders/")


def recipe_ci_required(paths):
    # Unknown paths, recipes and global build inputs retain the original CI.
    return not paths or any(p not in OWNED_FILES and not p.startswith(OWNED_PREFIXES) for p in paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()
    if not all(re.fullmatch(r"[0-9a-f]{40}", value) for value in [args.base, args.head]):
        parser.error("base and head must be full Git commit hashes")
    raw = subprocess.check_output(["git", "diff", "--name-only", "--no-renames", "-z", args.base, args.head, "--"])
    paths = [p.decode("utf-8") for p in raw.split(b"\0") if p]
    required = recipe_ci_required(paths)
    output = f"recipe_ci={str(required).lower()}\n"
    if os.environ.get("GITHUB_OUTPUT"):
        with Path(os.environ["GITHUB_OUTPUT"]).open("a") as stream:
            stream.write(output)
    print(output.strip())
    print(f"Classified {len(paths)} paths; unknown paths require recipe CI.")


if __name__ == "__main__":
    main()
