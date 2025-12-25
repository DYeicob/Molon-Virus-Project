# 🚀 Execution Instructions for VM (Academic Virus Simulator)

**WARNING:** This project must be executed **exclusively within an isolated Virtual Machine (VM)**. Never run this code on your host operating system.

---

## 1. Environment Requirements

- **Virtual Machine:** Windows (recommended for full feature support) or Linux.
- **Python:** Version 3.8 or higher.
- **Package Manager:** `pip` installed.
- **Network:** Internet access (only if communicating with a remote C2) or Local Host access.

---

## 2. Environment Setup

From the project root directory, create a virtual environment to isolate dependencies:

```bash
python -m venv venv

```

### Activate the Environment:

**Windows:**

```powershell
venv\Scripts\activate

```

**Linux/macOS:**

```bash
source venv/bin/activate

```

### Install Dependencies:

```bash
pip install -r requirements.txt
pip install -r server_c2/requirements.txt

```

---

## 3. Launching the C2 Server

In a dedicated terminal window:

```bash
python server_c2/server.py

```

The control panel will be accessible at: `http://localhost:5050/`
From this web interface, you can stage **benign commands** for the connected agents.

---

## 4. Running the Agent (Academic Virus)

In a separate terminal, ensuring the virtual environment is still active:

```bash
python src/agent.py

```

### Expected Behavior:

* The agent will perform a "beacon" to the C2 server within the first 60 seconds.
* The C2 will respond with any staged benign commands.
* If no command is received, a default safe payload (e.g., Rickroll) will trigger.

---

## 5. Testing the Killswitch

The system is designed to **automatically disable itself** if a specific trigger is detected.

### Windows (Primary Trigger):

Create the trigger file:

```powershell
echo "off" > C:\killswitch_mvs.txt

```

### Linux/macOS:

```bash
touch /tmp/killswitch_mvs

```

**Verification:** Upon detecting the file, the agent will log the detection, cease execution, and ignore all C2 commands or payloads.

---

## 6. Environment Cleanup

Once testing is complete, remove all project traces from the VM.

**Windows:**

```powershell
rmdir /S /Q venv
del mvs_sim.log
# Note: Manually delete the scheduled task using 'schtasks /delete /TN "MVS_Simulation"'

```

**Linux/macOS:**

```bash
rm -rf venv mvs_sim.log

```

---

## 7. Critical Safety Notes

* **Educational Only:** This project is for academic demonstration and must not be used on production systems.
* **Non-Malicious:** No modules implement destructive techniques.
* **Simulated Persistence:** Persistence methods are visible and easily reversible.
* **No Obfuscation:** There is no encryption, exploit code, or rootkit functionality included.
* **Mock Vectors:** The infection vectors (phishing/web) are purely for flow demonstration.
