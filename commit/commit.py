import os
from status.status import status


def cmd_commit(message=""):
    """Create a commit with optional message"""

    if not status.repository_exists():
        print("Error: No VCS repository found. Please run 'init' first.")
        return

    print("commit command called")
    print(f"  message: '{message}'")


current_dir = os.getcwd()
