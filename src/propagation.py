"""
Simulates propagation by creating harmless text files on detected removable drives.
Does NOT copy executables or send data across the network.
"""
import os
from .utils import log

def simulate_propagation_usb():
    """
    Simulated propagation: identifies potential removable drives and leaves 
    a non-malicious text file to demonstrate lateral movement potential.
    """
    if os.name != "nt":
        log("Simulated propagation: demo implemented for Windows environments only.")
        return
        
    # Standard enumeration of drive letters associated with removable media
    for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
        path = f"{letter}:\\"
        try:
            if os.path.exists(path):
                # Creating a benign marker file instead of a malicious executable
                target = os.path.join(path, "MVS_SIMULATED_README.txt")
                with open(target, "w", encoding="utf-8") as f:
                    f.write("Simulation: harmless propagation file. Safe to delete.\n")
                log(f"Simulated propagation: file successfully created at {path}")
        except Exception as e:
            # Common failure point: access denied or drive is not ready/writable
            log(f"Simulated propagation: failed at {path}: {e}")
