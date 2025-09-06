import os, json
from Colors import Colors

def cmd_branch(name=None):
    """List branches or create a new one"""
    current_dir = os.getcwd()
    if name:
        pass
    else:
        current_branch = branch.get_current()
        for file in os.listdir(current_dir + "/.vcs/"):
            if file[-5:] == ".json":
                if current_branch == file[:-5]:
                    print(Colors.GREEN + file[:-5] + Colors.RESET)
                else:
                    print(file[:-5])

class Branch:
    def get_current(self):
        with open(os.getcwd() + "/.vcs/data/status.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["branch"]
        
    




branch = Branch()