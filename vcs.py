#!/usr/bin/env python3
"""
VCS - Simple Version Control System
Minimal command interpreter for basic VCS operations.

Usage:
    python vcs.py <command> [args]
"""

import sys
from init.init import cmd_init
from commit.commit import cmd_commit
from status.status import cmd_status
from log.log import cmd_log
from branch.branch import cmd_branch
from checkout.checkout import cmd_checkout
from merge.merge import cmd_merge
from diff.diff import cmd_diff


def show_help(command):
    """Show help for a specific command"""
    help_text = {
        "init": """
Usage: python vcs.py init

Initialize a new VCS repository in the current directory.
This creates a .vcs directory with the necessary structure
to track file changes and manage version history.

Example:
    python vcs.py init
""",
        "commit": """
Usage: python vcs.py commit [-m 'message']

Record changes to the repository. Creates a snapshot of the
current state of tracked files.

Options:
    -m 'message'    Specify a commit message (optional)
                    If omitted, creates commit with empty message

Examples:
    python vcs.py commit                  # Commit with empty message
    python vcs.py commit -m "Fix bug"     # Commit with message
""",
        "status": """
Usage: python vcs.py status

Show the working tree status. Displays which files have been
modified, added, or deleted since the last commit.

Example:
    python vcs.py status
""",
        "log": """
Usage: python vcs.py log

Show commit history. Displays a list of all commits made to
the repository in reverse chronological order.

Example:
    python vcs.py log
""",
        "branch": """
Usage: python vcs.py branch [name]

List existing branches or create a new branch.

Arguments:
    name    Optional. If provided, creates a new branch with this name.
            If omitted, lists all existing branches.

Examples:
    python vcs.py branch            # List all branches
    python vcs.py branch feature    # Create branch named 'feature'
""",
        "checkout": """
Usage: python vcs.py checkout <branch>

Switch to a different branch. Updates files in the working
directory to match the specified branch.

Arguments:
    branch    Required. Name of the branch to switch to.

Example:
    python vcs.py checkout main      # Switch to 'main' branch
    python vcs.py checkout feature   # Switch to 'feature' branch
""",
        "merge": """
Usage: python vcs.py merge <branch>

Merge changes from the specified branch into the current branch.
Combines the development histories of two branches.

Arguments:
    branch    Required. Name of the branch to merge from.

Example:
    python vcs.py merge feature    # Merge 'feature' into current branch
""",
        "diff": """
Usage: python vcs.py diff

Show changes between commits or between the working directory
and the last commit. Displays line-by-line differences.

Example:
    python vcs.py diff
""",
    }

    if command in help_text:
        print(help_text[command])
    else:
        print(f"No help available for command: {command}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("VCS - Version Control System\n")
        print("Usage: python vcs.py <command> [args]")
        print("\nAvailable commands:")
        print("  init                     Initialize repository")
        print("  commit [-m 'message']    Create a commit")
        print("  status                   Show status")
        print("  log                      Show commit history")
        print("  branch [name]            List or create branch")
        print("  checkout <branch>        Switch branches")
        print("  merge <branch>           Merge branch")
        print("  diff                     Show differences")
        print("\nFor help on a specific command, use:")
        print("  python vcs.py <command> --help")
        print("  python vcs.py <command> -h")
        sys.exit(1)

    command = sys.argv[1]

    # Check for help flag as second argument
    if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
        show_help(command)
        sys.exit(0)

    if command == "init":
        # Check for help flag
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("init")
        else:
            cmd_init()

    elif command == "commit":
        # Check for help flag first
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("commit")
        else:
            # Check for -m flag
            message = ""
            if len(sys.argv) > 2:
                if sys.argv[2] == "-m" and len(sys.argv) > 3:
                    message = sys.argv[3]
            cmd_commit(message)

    elif command == "status":
        cmd_status()

    elif command == "log":
        cmd_log()

    elif command == "branch":
        # Check if asking for help
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("branch")
        else:
            # Optional branch name
            name = sys.argv[2] if len(sys.argv) > 2 else None
            cmd_branch(name)

    elif command == "checkout":
        # Check if asking for help
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("checkout")
        else:
            # Requires branch name
            if len(sys.argv) < 3:
                print("Error: checkout requires a branch name")
                print("Usage: python vcs.py checkout <branch>")
                print("For more help: python vcs.py checkout --help")
                sys.exit(1)
            cmd_checkout(sys.argv[2])

    elif command == "merge":
        # Check if asking for help
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("merge")
        else:
            # Requires branch name
            if len(sys.argv) < 3:
                print("Error: merge requires a branch name")
                print("Usage: python vcs.py merge <branch>")
                print("For more help: python vcs.py merge --help")
                sys.exit(1)
            cmd_merge(sys.argv[2])

    elif command == "diff":
        cmd_diff()

    else:
        print(f"Error: Unknown command '{command}'")
        print("Use 'python vcs.py' to see available commands")
        sys.exit(1)


if __name__ == "__main__":
    main()
