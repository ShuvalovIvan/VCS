from diff_class import Diff
import os

diff = Diff()

testFile = os.path.abspath('test.txt')

read_file = diff.read_file(testFile)

for i in range(len(read_file)):
    print(read_file[i])