import os


def cmd_status():
    """Show the status of the repository"""
    if status.repository_exists():
        print("Repository is initialized and has the correct structure.")
    else:
        print("No VCS repository found. Please run 'init' to create one.")


class Status:

    def __init__(self):
        self

    def repository_exists():
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


status = Status()
