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
        
    def longest_common_subsequence(self, file1_lines, file2_lines):
        m = len(file1_lines)
        n = len(file2_lines)

        lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (file1_lines[i] == file2_lines[j]):
                    lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
                else:
                    lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
        return lcs_matrix