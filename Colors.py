from sys import stdout
from os import environ


class Colors:
    """ANSI color codes for terminal output"""

    # Check if colors should be disabled (for non-terminal output)
    NO_COLOR = not stdout.isatty() or environ.get("NO_COLOR")

    # Color codes
    RESET = "" if NO_COLOR else "\033[0m"
    BOLD = "" if NO_COLOR else "\033[1m"
    DIM = "" if NO_COLOR else "\033[2m"

    # Foreground colors
    RED = "" if NO_COLOR else "\033[91m"
    GREEN = "" if NO_COLOR else "\033[92m"
    YELLOW = "" if NO_COLOR else "\033[93m"
    BLUE = "" if NO_COLOR else "\033[94m"
    MAGENTA = "" if NO_COLOR else "\033[95m"
    CYAN = "" if NO_COLOR else "\033[96m"
    WHITE = "" if NO_COLOR else "\033[97m"
    GRAY = "" if NO_COLOR else "\033[90m"

    # Background colors
    BG_BLUE = "" if NO_COLOR else "\033[44m"
    BG_GREEN = "" if NO_COLOR else "\033[42m"
