from diff_class import Diff
import os

diff = Diff()

file1 = os.path.abspath('file1.txt')
file2 = os.path.abspath('file2.txt')


filestring1 = "line 1\nline 2\nline 3\nline 4\ni dont know anymore\nyeah what is happening\nanymoreb\n\ngr\n\n\ncode and stuff\ntwin kys"
filestring2 = "line 1\nline 2\nline 3\nyeah what is happening atp\n\ncode and stuff\ntwin kys\n\nI Cleaned up some code twin <3"

diff.diff(file1, filestring2)