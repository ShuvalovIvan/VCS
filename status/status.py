import os


def cmd_status():
    """Show working tree status"""
    print("status command called")


class Status:

    def repository_exists():
        # Check if .vcs directory exists
        folder_exists = os.path.isdir(".vcs")

        json_exists = (
            any(fname.endswith(".json") for fname in os.listdir(".vcs"))
            if folder_exists
            else False
        )

        data_exists = os.path.isdir(".vcs/data") if folder_exists else False

        return folder_exists and json_exists and data_exists


status = Status()
