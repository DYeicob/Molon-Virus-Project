# MolonVirusSim - Simulador académico (inofensivo)

**Propósito:** proyecto para prácticas de ciberseguridad que simula comportamiento de malware
(enferma: infección, persistencia, C2, propagación, payload) **sin causar daño real**.

**Importante:** No contiene rootkits, no sobrescribe boot/UEFI, no inyecta código real ni propaga por la red.

## Cómo ejecutar (en VM aislada)
1. Clona el repo.
2. Crea un entorno virtual: `python -m venv venv && venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux).
3. `pip install -r requirements.txt`
4. Levanta el C2: `python server_c2/server.py`
5. En otra terminal corre el agente en la VM víctima: `python -m src.agent`
6. Para detenerlo inmediatamente: crea el fichero `C:\killswitch_mvs.txt` en la VM.

## Killswitch
Ruta: `C:\killswitch_mvs.txt` — si existe el agente se detiene.

## Licencia
MIT — uso educativo únicamente.
