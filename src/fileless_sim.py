"""
Simula técnicas fileless usando comandos inofensivos.
No descarga ni ejecuta código remoto.
"""
import subprocess, os
from .utils import log

def simulate_fileless():
    log("Simulación fileless: ejecutando comando benigno.")
    try:
        if os.name == "nt":
            subprocess.run(["powershell", "-NoProfile", "-Command", "Write-Output 'Fileless simulado'"], shell=True, check=False)
        else:
            subprocess.run(["echo", "Fileless simulado"], check=False)
        log("Fileless simulado completado.")
    except Exception as e:
        log(f"Fileless simulado falló: {e}")
