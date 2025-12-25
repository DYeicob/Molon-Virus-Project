"""
Simulates fileless techniques using harmless commands.
Does not download or execute remote code.
"""
import subprocess, os
from .utils import log

def simulate_fileless():
    """
    Simulated fileless execution: runs a benign command directly via a system shell.
    In a real attack, this would involve memory-only execution or LOLBAS.
    """
    log("Fileless simulation: executing benign command.")
    try:
        if os.name == "nt":
            # Emulating a LOLBAS technique by calling PowerShell with specific flags
            # -NoProfile prevents loading user profiles, a common evasion tactic.
            subprocess.run(["powershell", "-NoProfile", "-Command", "Write-Output 'Simulated Fileless'"], shell=True, check=False)
        else:
            # Emulating a fileless approach on Unix-like systems
            subprocess.run(["echo", "Simulated Fileless"], check=False)
            
        log("Fileless simulation completed successfully.")
    except Exception as e:
        log(f"Fileless simulation failed: {e}")
