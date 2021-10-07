#!/usr/bin/env python

from pathlib import Path
from sys import argv, exit

hooks = (
    "commit-msg",
    "pre-commit",
)


def usage() -> None:
    print("Usage: tools/hooks.py (install|uninstall)")
    exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        usage()

    if argv[1] == "install":
        uninstall = False
    elif argv[1] == "uninstall":
        uninstall = True
    else:
        usage()

    git_hooks = Path(".git") / "hooks"
    tools = Path("tools")
    for hook in hooks:
        git_hook = git_hooks / hook
        if not uninstall:
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
