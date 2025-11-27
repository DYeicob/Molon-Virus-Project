from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Última orden enviada a los clientes
command_buffer = {"cmd": ""}

@app.route("/")
def home():
    return """
    <h2>C2 de demostración académica</h2>
    <p>Este panel NO controla nada real. Solo es un panel educativo.</p>
    <form action="/set" method="post">
        <input name="cmd" placeholder="Comando benigno">
        <button type="submit">Enviar</button>
    </form>
    """

@app.route("/set", methods=["POST"])
def set_cmd():
    """
    Establece un comando benigno para que el cliente lo recoja.
    """
    cmd = request.form.get("cmd", "")
    command_buffer["cmd"] = cmd
    return f"Comando establecido: {cmd}"

@app.route("/c2", methods=["POST"])
def beacon():
    """
    Endpoint que consultarían los clientes.
    Devuelve el comando y lo limpia.
    """
    agent = request.json.get("agent", "unknown")
    cmd = command_buffer["cmd"]

    # limpiamos para simular "one-time commands"
    command_buffer["cmd"] = ""

    return jsonify({"agent": agent, "cmd": cmd})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
