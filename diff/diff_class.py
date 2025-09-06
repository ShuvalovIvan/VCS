def cmd_diff():
    """Show differences"""
    print("diff command called")

import os
class Diff:

    def cmd_diff():
        """Show differences"""
        print("diff command called")

    def init(self):
        pass

    def diff(file_path1, file_path2):
        return 0

    # assumes full working filepath is passed in
    def read_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.rstrip("\n\r") for line in f.readlines()]
        except FileNotFoundError:
            return []