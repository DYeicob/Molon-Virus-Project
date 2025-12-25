"""
Simulation of process 'migration' to another process.
This module DOES NOT inject code or alter memory — it only enumerates processes and logs targets.
"""
import psutil
from .utils import log

def simulate_migration():
    """
    Simulated migration: enumerates running processes to identify suitable targets.
    In a professional Red Team operation, this mimics the 'Discovery' and 'Evasion' phases.
    """
    log("Simulation: searching for target processes to 'migrate' (simulated).")
    targets = []
    
    # Iterate through all running processes
    for p in psutil.process_iter(attrs=['pid','name']):
        name = (p.info['name'] or "").lower()
        
        # Look for common targets that provide stability or stealth
        # explorer.exe is a classic target for persistence
        if any(k in name for k in ["notepad", "explorer", "code", "python"]):
            targets.append((p.info['pid'], p.info['name']))
            
    if targets:
        # Select the first viable candidate for the simulation log
        pid, name = targets[0]
        log(f"Simulation: would select PID {pid} ({name}) as the migration target.")
    else:
        log("Simulation: no 'interesting' target processes found.")
