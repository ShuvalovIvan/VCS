import os
import json

def cmd_init():
    """Initialize a new repository"""
    print("init command called")

    current_dir = os.getcwd()
    os.makedirs(current_dir + "/.vcs/", exist_ok=True)

    if not os.path.exists(current_dir + "/.vcs/main.json"):
        with open(current_dir + "/.vcs/main.json", "w", encoding='utf-8') as f:
            json.dump({}, f)
    else:
        print("Repository exists")
    if not os.path.exists(current_dir + "/.vcs/data/status.json"):
        with open(current_dir + "/.vcs/data/status.json", "w", encoding='utf-8') as f:
            json.dump({"branch", "main"}, f)
    else:
        print("Data status exists")

    
