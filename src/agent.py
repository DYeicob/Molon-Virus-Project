"""
Agente principal que orquesta la simulación.
Cumple: infección simulada, fileless simulado, persistencia (inofensiva),
propagación simulada, C2 beaconing, payload en <60s, killswitch.
"""
from .utils import log
from .killswitch import is_killswitched
from .migration_sim import simulate_migration
from .fileless_sim import simulate_fileless
from .persistence import simulate_persistence_windows, simulate_persistence_unix
from .propagation import simulate_propagation_usb
from .c2_client import beacon_loop
from .payloads import rickroll

import time, os

def main():
    log("=== MolonVirusSim (agente simulado) arrancando ===")
    if is_killswitched():
        return

    # 1. Vector / click simulado
    log("Vector de entrada: phishing/web 'cringe' simulado. Descarga un ejecutable inocuo.")
    # 1a. 'Migración' simulada
    simulate_migration()
    # 1b. fileless simulado
    simulate_fileless()

    # 2. Persistencia (inofensiva)
    if os.name == "nt":
        simulate_persistence_windows()
    else:
        simulate_persistence_unix()

    # 3. Propagación simulada (USB)
    simulate_propagation_usb()

    # 4. C2: beacon durante máximo 60s; si viene comando se ejecuta
    beacon_loop(max_duration_sec=60)

    # 5. Payload por defecto si no llegó comando en 60s
    if not is_killswitched():
        rickroll()

    log("=== MolonVirusSim (agente simulado) finalizado ===")

if __name__ == "__main__":
    main()
