from diff_class import Diff
import os

diff = Diff()

file1 = os.path.abspath('file1.txt')
file2 = os.path.abspath('file2.txt')
lines1 = diff.read_file(file1)
lines2 = diff.read_file(file2)

# print(diff.print_diff_operationss(read_file, read_file))
print(diff.print_diff_operations(file1, file2))