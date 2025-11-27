import sys
from pathlib import Path

# Aseguramos que server_c2 esté en import path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import json
import pytest

# Importamos el módulo del servidor (server_c2/server.py)
from server_c2 import server as c2mod

@pytest.fixture
def client():
    """Client de testing de Flask"""
    app = c2mod.app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_set_and_get_command(client):
    """
    Testeamos que:
     - podemos establecer un comando vía /set (form POST)
     - el endpoint /c2 devuelve ese comando y lo limpia si así lo hemos diseñado
    """
    # Establecer comando
    rv = client.post("/set", data={"cmd": "rickroll"}, follow_redirects=True)
    assert rv.status_code == 200

    # Beacon desde 'agente' al C2
    resp = client.post("/c2", json={"agent": "test_agent"})
    assert resp.status_code == 200
    data = resp.get_json()
    # Debe contener el comando que acabamos de establecer
    assert "cmd" in data
    assert data["cmd"] == "rickroll"

    # Tras la entrega, el comando se limpia (comportamiento del server)
    resp2 = client.post("/c2", json={"agent": "test_agent"})
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    assert data2.get("cmd", "") == ""
