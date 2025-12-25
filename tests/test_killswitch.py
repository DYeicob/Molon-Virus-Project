import os
from pathlib import Path
import importlib
import sys
import pytest

# Ensure the 'src' directory is in sys.path for proper imports
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import the killswitch module from the src package
from src import killswitch as ks
from src.utils import log

def test_killswitch_absent(tmp_path, monkeypatch):
    """
    If the killswitch file does not exist, is_killswitched() must return False.
    """
    fake_file = tmp_path / "killswitch_fake.txt"
    
    # Ensure the file does not exist before starting the test
    if fake_file.exists():
        fake_file.unlink()

    # Override the path constant in the module for testing purposes
    monkeypatch.setattr(ks, "KILLSWITCH_PATH", fake_file)

    assert not ks.is_killswitched()

def test_killswitch_present(tmp_path, monkeypatch):
    """
    If the killswitch file exists, is_killswitched() must return True.
    """
    fake_file = tmp_path / "killswitch_fake.txt"
    fake_file.write_text("stop", encoding="utf-8")

    # Override the path constant in the module for testing purposes
    monkeypatch.setattr(ks, "KILLSWITCH_PATH", fake_file)

    assert ks.is_killswitched()
