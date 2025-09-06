#!/usr/bin/env python3
"""
VCS - Simple Version Control System
Minimal command interpreter for basic VCS operations with colored output.

Usage:
    python vcs.py <command> [args]
"""

import sys
import os
from init.init import cmd_init
from commit.commit import cmd_commit
from status.status import cmd_status, status
from log.log import cmd_log
from branch.branch import cmd_branch
from checkout.checkout import cmd_checkout
from merge.merge import cmd_merge
from diff.diff import cmd_diff
from Colors import Colors
from help_text import help_text


def colorize(text, color):
    """Apply color to text"""
    return f"{color}{text}{Colors.RESET}"


def show_help(command):
    """Show help for a specific command"""

    if command in help_text:
        print(help_text[command])
    else:
        print(
            f"{colorize('Error:', Colors.RED)} No help available for command: {colorize(command, Colors.YELLOW)}"
        )


def print_main_help():
    """Print the main help menu with colors"""
    title = f"""
{colorize('━' * 50, Colors.BLUE)}
{colorize('  VCS - Version Control System', Colors.BOLD + Colors.CYAN)}
{colorize('━' * 50, Colors.BLUE)}
"""

    print(title)
    print(
        f"{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py', Colors.CYAN)} {colorize('<command>', Colors.GREEN)} {colorize('[args]', Colors.GRAY)}"
    )
    print()
    print(f"{colorize('Available commands:', Colors.YELLOW)}")

    commands = [
        ("init", "Initialize repository"),
        ("commit", "Create a commit", '[-m "message"]'),
        ("status", "Show status"),
        ("log", "Show commit history"),
        ("branch", "List or create branch", "[name]"),
        ("checkout", "Switch branches", "<branch>"),
        ("merge", "Merge branch", "<branch>"),
        ("diff", "Show differences"),
    ]

    for cmd_info in commands:
        cmd = cmd_info[0]
        desc = cmd_info[1]
        args = cmd_info[2] if len(cmd_info) > 2 else ""

        # Format command with padding
        cmd_str = f"  {colorize(cmd, Colors.GREEN)}"
        if args:
            cmd_str += f" {colorize(args, Colors.MAGENTA)}"

        # Calculate padding for alignment
        padding = (
            35
            - len(cmd_str)
            + len(colorize("", Colors.GREEN))
            + len(colorize("", Colors.MAGENTA))
        )

        print(f"{cmd_str}{' ' * max(1, padding)}{desc}")

    print()
    print(f"{colorize('For help on a specific command, use:', Colors.YELLOW)}")
    print(
        f"  {colorize('python vcs.py', Colors.CYAN)} {colorize('<command>', Colors.GREEN)} {colorize('--help', Colors.MAGENTA)}"
    )
    print(
        f"  {colorize('python vcs.py', Colors.CYAN)} {colorize('<command>', Colors.GREEN)} {colorize('-h', Colors.MAGENTA)}"
    )
    print()


def print_error(message):
    """Print an error message with color"""
    print(f"{colorize('Error:', Colors.RED)} {message}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print_main_help()
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
    
    elif not status.repository_exists():
        print("Error: No VCS repository found. Please run 'init' first.")
        return

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
                print_error("checkout requires a branch name")
                print(
                    f"{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py checkout', Colors.CYAN)} {colorize('<branch>', Colors.GREEN)}"
                )
                print(
                    f"{colorize('For more help:', Colors.GRAY)} python vcs.py checkout --help"
                )
                sys.exit(1)
            cmd_checkout(sys.argv[2])

    elif command == "merge":
        # Check if asking for help
        if len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]:
            show_help("merge")
        else:
            # Requires branch name
            if len(sys.argv) < 3:
                print_error("merge requires a branch name")
                print(
                    f"{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py merge', Colors.CYAN)} {colorize('<branch>', Colors.GREEN)}"
                )
                print(
                    f"{colorize('For more help:', Colors.GRAY)} python vcs.py merge --help"
                )
                sys.exit(1)
            cmd_merge(sys.argv[2])

    elif command == "diff":
        cmd_diff()

    else:
        print_error(f"Unknown command '{colorize(command, Colors.YELLOW)}'")
        print(
            f"Use '{colorize('python vcs.py', Colors.CYAN)}' to see available commands"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
