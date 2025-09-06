def cmd_branch(name=None):
    """List branches or create a new one"""
    if name:
        print("branch command called")
        print(f"  create branch: {name}")
    else:
        print("branch command called")
        print("  list branches")
