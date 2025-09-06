import os, json
from Colors import Colors
import shutil

def cmd_branch(name=None):
    """List branches or create a new one"""
    if name:
        branch.create_branch(name)
    else:
        branch.print_branches()

class Branch:
    def get_current(self):
        with open(os.getcwd() + "/.vcs/data/status.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["branch"]
   
    def print_branches(self):
        current_dir = os.getcwd()
        current_branch = branch.get_current()
        for file in os.listdir(current_dir + "/.vcs/"):
            if file[-5:] == ".json":
                if current_branch == file[:-5]:
                    print(Colors.GREEN + file[:-5] + Colors.RESET)
                else:
                    print(file[:-5])
    
    def create_branch(self, name):
        current_dir = os.getcwd()
        current_branch = branch.get_current()
        if os.path.exists(current_dir + f"/.vcs/{name}.json"):
            print(Colors.RED + "Branch already exists" + Colors.RESET)
        else:
            shutil.copy2(current_dir + "/.vcs/" + current_branch + ".json", current_dir + "/.vcs/"  + name + ".json")
            print(f"{Colors.GREEN}{name} branch created{Colors.RESET}")




branch = Branch()