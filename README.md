# 🦠 MolonVirusSim - Academic Simulator (Harmless)

**Purpose:** A cybersecurity lab project that simulates malware behavior (Infection, Persistence, C2, Propagation, and Payload) **without causing real damage**.

**Important:** This project does not contain rootkits, does not overwrite boot/UEFI sectors, does not perform actual code injection, and does not propagate across real networks.

---

## 🚀 How to Execute (Inside an Isolated VM)

1. **Clone the repository.**
2. **Create a virtual environment:** * **Windows:** `python -m venv venv && venv\Scripts\activate`
   * **Linux:** `source venv/bin/activate`
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch the C2 Server:**
   ```bash
   python server_c2/server.py
   ```
5. **Run the agent on the victim VM (separate terminal):**
   ```bash
   python -m src.agent
   ```
6. Emergency Stop: To halt the simulation immediately, create the file `C:\killswitch_mvs.txt` inside the VM.
