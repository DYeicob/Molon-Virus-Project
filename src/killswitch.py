from pathlib import Path
from .utils import log

# This path is documented in the technical report as the emergency stop trigger.
KILLSWITCH_PATH = Path(r"C:\killswitch_mvs.txt")

def is_killswitched():
    """
    Checks for the presence of the killswitch file.
    If found, the agent will immediately cease all activities.
    """
    if KILLSWITCH_PATH.exists():
        log(f"KILLSWITCH DETECTED: {KILLSWITCH_PATH}")
        return True
    return False
