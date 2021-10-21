#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path

hooks = (
    "commit-msg",
    "pre-commit",
)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("action", choices=("install", "uninstall"))
    parser.add_argument("--hooks", choices=hooks, nargs="*", default=hooks)
    args = parser.parse_args()

    git_hooks = Path(".git") / "hooks"
    tools = Path("tools")
    for hook in args.hooks:
        git_hook = git_hooks / hook
        if args.action == "uninstall":
            script = tools / f"{hook}.py"
            if git_hook.exists():
                print(f"A hook already exists at {git_hook}, skipping")
                continue
            with open(git_hook, "w") as f:
                f.write(
                    f"""#!/bin/sh
python {script} "$@"
"""
                )
            git_hook.chmod(0o755)
            print(f"Installed hook at {git_hook}")
        else:
            if not git_hook.exists():
                continue
            git_hook.unlink()
            print(f"Uninstalled hook at {git_hook}")


# vim: set et ts=4 sw=4:
