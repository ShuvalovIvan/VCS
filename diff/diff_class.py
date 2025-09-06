from typing import List, Tuple, Optional
import os
def cmd_diff():
    """Show differences"""
    print("diff command called")

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
        
    def longest_common_subsequence(self, lines1, lines2):
        m, n = len(lines1), len(lines2)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if lines1[i-1] == lines2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        
        return lcs

    def gen_diff_operations(self, file1_lines, file2_lines):
        lcs_matrix = self.longest_common_subsequence(file1_lines, file2_lines)
        operations = []

        i = len(file1_lines)
        j = len(file2_lines)
        while (i > 0 or j > 0):
            if i > 0 and j > 0 and file1_lines[i-1] == file2_lines[j-1]:
                operations.append(('=', i, j, file1_lines[i-1]))
                i -= 1
                j -= 1
            elif i > 0 and (j == 0 or lcs_matrix[i-1][j] >= lcs_matrix[i][j-1]):
                operations.append(('+', i, " ", file1_lines[i-1]))
                i -= 1
            else:
                operations.append(('-', " ", j, file2_lines[j-1]))
                j -= 1
        operations.reverse()
        return operations
    
    def print_diff_operations(self, file1, file2):
        lines1 = self.read_file(file1)
        lines2 = self.read_file(file2)
        operations = self.gen_diff_operations(lines1, lines2)
        for i in range(len(operations)):
            
            print(f"{operations[i][0]} {operations[i][1]} {operations[i][2]} {operations[i][3]}")