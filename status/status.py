import os


def cmd_status():
    """Show the status of the repository"""
    status.status()


class Status:

    def __init__(self):
        self

    def repository_exists(self):
        """
        Check if .vcs repository exists with required structure

        Returns:
            bool: True if repository exists, False otherwise"""
        folder_exists = os.path.isdir(".vcs")

        json_exists = (
            any(fname.endswith(".json") for fname in os.listdir(".vcs"))
            if folder_exists
            else False
        )

        data_exists = os.path.isdir(".vcs/data") if folder_exists else False

        return folder_exists and json_exists and data_exists

    def status(self):
        """Display the status of the repository"""
        current_branch = None  # Should be branch name
        unmodified_changes = None  # Should be T or F

        if self.repository_exists():
            print(f"On branch: {current_branch if current_branch else 'NO BRANCH'}")

            if unmodified_changes:
                print("No changes to commit, working tree clean")
            else:
                print("You have uncommitted changes.")

        else:
            print("No VCS repository found. Please run 'init' to create one.")


status = Status()
