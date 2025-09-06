import os
from status.status import status

def cmd_commit(message=""):
    """Create a commit with optional message"""
    print("commit command called")
    print(f"  message: '{message}'")


current_dir = os.getcwd()
