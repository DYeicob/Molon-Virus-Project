import time
from pathlib import Path

LOGFILE = Path("mvs_sim.log")

def log(msg):
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] {msg}"
    print(line)
    with LOGFILE.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
