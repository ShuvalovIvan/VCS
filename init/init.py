import os
import json
from status.status import status

def cmd_init():
    """Initialize a new repository"""
    print("Repository Initialized")

    if status.repository_exists():
        raise ValueError("Repository already exists")
    
    current_dir = os.getcwd()
    os.makedirs(current_dir + "/.vcs/", exist_ok=True)
    os.makedirs(current_dir + "/.vcs/data", exist_ok=True)

    if not os.path.exists(current_dir + "/.vcs/main.json"):
        with open(current_dir + "/.vcs/main.json", "w", encoding='utf-8') as f:
            json.dump({}, f)
    else:
        print("Repository exists")
    if not os.path.exists(current_dir + "/.vcs/data/status.json"):
        with open(current_dir + "/.vcs/data/status.json", "w", encoding='utf-8') as f:
            json.dump({"branch": "main"}, f)
    else:
        print("Data status exists")

    

    
