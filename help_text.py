from Colors import Colors, colorize

help_text = {
    "init": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py init', Colors.CYAN)}

{colorize('Description:', Colors.YELLOW)}
Initialize a new VCS repository in the current directory.
This creates a {colorize('.vcs', Colors.GREEN)} directory with the necessary structure
to track file changes and manage version history.

{colorize('Example:', Colors.YELLOW)}
    {colorize('python vcs.py init', Colors.CYAN)}
""",
    "commit": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py commit', Colors.CYAN)} {colorize('[-m', Colors.MAGENTA)} {colorize("'message']", Colors.GREEN)}

{colorize('Description:', Colors.YELLOW)}
Record changes to the repository. Creates a snapshot of the
current state of tracked files.

{colorize('Options:', Colors.YELLOW)}
    {colorize('-m', Colors.MAGENTA)} {colorize("'message'", Colors.GREEN)}    Specify a commit message {colorize('(optional)', Colors.GRAY)}
                    If omitted, creates commit with empty message

{colorize('Examples:', Colors.YELLOW)}
    {colorize('python vcs.py commit', Colors.CYAN)}                  {colorize('# Commit with empty message', Colors.GRAY)}
    {colorize('python vcs.py commit -m "Fix bug"', Colors.CYAN)}     {colorize('# Commit with message', Colors.GRAY)}
""",
    "status": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py status', Colors.CYAN)}

{colorize('Description:', Colors.YELLOW)}
Show the working tree status. Displays which files have been
{colorize('modified', Colors.YELLOW)}, {colorize('added', Colors.GREEN)}, or {colorize('deleted', Colors.RED)} since the last commit.

{colorize('Example:', Colors.YELLOW)}
    {colorize('python vcs.py status', Colors.CYAN)}
""",
    "log": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py log', Colors.CYAN)}

{colorize('Description:', Colors.YELLOW)}
Show commit history. Displays a list of all commits made to
the repository in reverse chronological order.

{colorize('Example:', Colors.YELLOW)}
    {colorize('python vcs.py log', Colors.CYAN)}
""",
    "branch": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py branch', Colors.CYAN)} {colorize('[name]', Colors.GREEN)}

{colorize('Description:', Colors.YELLOW)}
List existing branches or create a new branch.

{colorize('Arguments:', Colors.YELLOW)}
    {colorize('name', Colors.GREEN)}    {colorize('Optional.', Colors.GRAY)} If provided, creates a new branch with this name.
            If omitted, lists all existing branches.

{colorize('Examples:', Colors.YELLOW)}
    {colorize('python vcs.py branch', Colors.CYAN)}            {colorize('# List all branches', Colors.GRAY)}
    {colorize('python vcs.py branch feature', Colors.CYAN)}    {colorize('# Create branch named "feature"', Colors.GRAY)}
""",
    "checkout": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py checkout', Colors.CYAN)} {colorize('<branch>', Colors.GREEN)}

{colorize('Description:', Colors.YELLOW)}
Switch to a different branch. Updates files in the working
directory to match the specified branch.

{colorize('Arguments:', Colors.YELLOW)}
    {colorize('branch', Colors.GREEN)}    {colorize('Required.', Colors.RED)} Name of the branch to switch to.

{colorize('Examples:', Colors.YELLOW)}
    {colorize('python vcs.py checkout main', Colors.CYAN)}      {colorize('# Switch to "main" branch', Colors.GRAY)}
    {colorize('python vcs.py checkout feature', Colors.CYAN)}   {colorize('# Switch to "feature" branch', Colors.GRAY)}
""",
    "merge": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py merge', Colors.CYAN)} {colorize('<branch>', Colors.GREEN)}

{colorize('Description:', Colors.YELLOW)}
Merge changes from the specified branch into the current branch.
Combines the development histories of two branches.

{colorize('Arguments:', Colors.YELLOW)}
    {colorize('branch', Colors.GREEN)}    {colorize('Required.', Colors.RED)} Name of the branch to merge from.

{colorize('Example:', Colors.YELLOW)}
    {colorize('python vcs.py merge feature', Colors.CYAN)}    {colorize('# Merge "feature" into current branch', Colors.GRAY)}
""",
    "diff": f"""
{colorize('Usage:', Colors.YELLOW)} {colorize('python vcs.py diff', Colors.CYAN)}

{colorize('Description:', Colors.YELLOW)}
Show changes between commits or between the working directory
and the last commit. Displays line-by-line differences.

{colorize('Example:', Colors.YELLOW)}
    {colorize('python vcs.py diff', Colors.CYAN)}
""",
}
