def cmd_diff():
    """Show differences"""
    print("diff command called")

class Diff:

    def init(self):
        pass

    def diff_defualt(self, current_file_path, prev_file_as_string: str):
        lines1 = self.read_file(current_file_path)
        lines2 = prev_file_as_string.splitlines()
        self.diff(lines1, lines2)
        

    def diff(self, lines1, lines2):
        operations = self.gen_diff_operations(lines1, lines2)
        formatted = self.format_operations_for_console(operations)
        self.print_console_format(formatted)


    # assumes full working filepath is passed in
    def read_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.rstrip("\n\r") for line in f.readlines()]
        except FileNotFoundError:
            return []
    
    def string_file_to_lines(self, file):
        return [line.rstrip("\n\r") for line in file.readlines()]
        
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
                operations.append(('keep', i, j, file1_lines[i-1]))
                i -= 1
                j -= 1
            elif i > 0 and (j == 0 or lcs_matrix[i-1][j] >= lcs_matrix[i][j-1]):
                operations.append(('remove', -1, i, file1_lines[i-1]))
                i -= 1
            else:
                operations.append(('insert', j, -1, file2_lines[j-1]))
                j -= 1
        operations.reverse()
        return operations
    

    def format_operations_for_console(self, operations):
        if not operations:
            return ""
        
        max_file1 = max(op[1] for op in operations if op[1] != -1)
        max_file2 = max(op[2] for op in operations if op[2] != -1)
        width1 = len(str(max_file1))
        width2 = len(str(max_file2))
        
        formatted = []

        for op, idx1, idx2, line in operations:
            if op == 'keep':
                symbol = '='
                f1 = str(idx1).rjust(width1)
                f2 = str(idx2).rjust(width2)
            elif op == 'insert':
                symbol = '+'
                f1 = ' '.rjust(width2)
                f2 = str(idx1).rjust(width1)
            elif op == 'remove':
                symbol = '-'
                f1 = str(idx2).rjust(width2)
                f2 = ' '.rjust(width1)
            formatted.append(f"{symbol} {f1} {f2} {line}")
        
        return formatted

    def print_console_format(self, formatted):
        for i in range(len(formatted)):
            print(formatted[i])
    