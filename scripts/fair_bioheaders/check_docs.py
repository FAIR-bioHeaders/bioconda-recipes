"""Check local Markdown file targets and whitespace in an explicitly owned scope."""
import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


def check_file(path, root):
    errors = []
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            errors.append(f"{path}:{number}: trailing whitespace")
        if re.match(r"^(<<<<<<< |=======$|>>>>>>> )", line):
            errors.append(f"{path}:{number}: unresolved conflict marker")
    # Inline links/images and reference definitions; this does not validate fragments.
    links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
    links += re.findall(r"(?m)^\s*\[[^\]]+\]:\s*(\S+)", text)
    for target in links:
        target = target.strip()
        if not target:
            continue
        if target.startswith("<"):
            target = target[1:].split(">", 1)[0]
        else:
            target = target.split()[0]
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        relative = unquote(parts.path)
        resolved = (root / relative.lstrip("/") if relative.startswith("/")
                    else path.parent / relative).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"{path}: local link escapes repository: {target}")
        elif not resolved.exists():
            errors.append(f"{path}: missing local target: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    root = Path.cwd()
    errors = [e for path in args.paths for e in check_file(path, root)]
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Checked {len(args.paths)} owned Markdown files (local paths; no network or fragment checks).")


if __name__ == "__main__":
    main()
