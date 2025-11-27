import os
from pathlib import Path
import importlib
import sys
import pytest

# Aseguramos que la carpeta src esté en sys.path para poder importar
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT))

# Importamos el módulo killswitch del paquete src
from src import killswitch as ks
from src.utils import log

def test_killswitch_absent(tmp_path, monkeypatch):
    """
    Si no existe el fichero killswitch, is_killswitched() debe devolver False.
    """
    fake_file = tmp_path / "killswitch_fake.txt"
    # nos aseguramos de que no exista
    if fake_file.exists():
        fake_file.unlink()

    # Sobrescribimos la constante de ruta en el módulo para test
    monkeypatch.setattr(ks, "KILLSWITCH_PATH", fake_file)

    assert not ks.is_killswitched()

def test_killswitch_present(tmp_path, monkeypatch):
    """
    Si existe el fichero killswitch, is_killswitched() debe devolver True.
    """
    fake_file = tmp_path / "killswitch_fake.txt"
    fake_file.write_text("stop", encoding="utf-8")

    monkeypatch.setattr(ks, "KILLSWITCH_PATH", fake_file)

    assert ks.is_killswitched()
