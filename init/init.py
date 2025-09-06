import os

def cmd_init():
    """Initialize a new repository"""
    print("init command called")
    current_dir = os.getcwd()
    os.makedirs(current_dir + "/.vcs/objects", exist_ok=True)
    os.makedirs(current_dir + "/.vcs/refs/heads", exist_ok=True)

    with open(current_dir + ".vcs/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")

    open(current_dir + "/.vcs/index", "w").close()
    open(current_dir + "/.vcs/config", "w").close()
    open(current_dir + "/.vcs/description", "w").close()
    open(current_dir + "/.vcs/refs/heads/main", "w").close()

    print(f"Initialized empty VCS repository in {current_dir}/.vcs/")
