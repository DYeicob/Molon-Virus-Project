# 🛡️ PROJECT REPORT — Academic "Molon" Virus Simulator

## 1. Project Objectives
The primary purpose of this project is to demonstrate the lifecycle of a cyber threat within a strictly educational and controlled environment. The key goals include:
* **Understanding Infection Vectors:** Emulating delivery methods without executing malicious code.
* **Analyzing Non-Malicious Persistence:** Studying how software remains active after reboots.
* **Simulating Benign C2:** Implementing command-and-control communication protocols.
* **Safe Payload Execution:** Demonstrating "Actions on Objectives" using harmless triggers.
* **Mandatory Killswitch:** Ensuring immediate deactivation via a documented trigger.

---

## 2. General System Architecture
The project is modularized to represent the different stages of the **Cyber Kill Chain**:

* `src/agent.py`: The main orchestrator that manages the execution flow.
* `src/persistence.py`: Handles simulated persistence (e.g., Scheduled Tasks).
* `src/killswitch.py`: The safety module that checks for deactivation triggers.
* `src/c2_client.py`: Manages beaconing and benign communication with the server.
* `server_c2/`: A Flask-based dashboard for remote management.
* `phishing_demo/`: Mock infection vectors used for social engineering emulation.



---

## 3. Infection Vector (Mockup)
The simulation utilizes two creative social engineering lures:
* **Mock Phishing Email:** (`phishing_demo/email.html`)
* **"Cringe" Website:** (`phishing_demo/web_cringe/`)

**Safety Note:** The downloaded file contains no malicious code. It is a standard Python script/executable that simulates the process of "Initial Access" without exploiting system vulnerabilities or causing harm.

---

## 4. Persistence
This module ensures the agent survives system restarts to demonstrate how real malware maintains a foothold:
* **Simulated Scheduled Task:** Uses `schtasks` on Windows to trigger the agent upon user logon.
* **Educational Registry Use:** References how registry keys can be used for persistence.
* **Focus:** The goal is to study detection, not to hide from the user; therefore, the tasks are clearly named and easily reversible.

---

## 5. Benign Command & Control (C2)
The communication infrastructure is built on:
* **Flask Server:** A centralized hub to stage commands.
* **Agent Client:** Located in `src/c2_client.py`, it performs periodic "beacons" to check for new instructions.
* **Functional Constraints:** To comply with lab rules, no proxies, Tor, or encrypted tunnels are used. All traffic is direct and transparent.

---

## 6. Safe Payloads
Upon receiving a command or reaching a 60-second timeout, the agent triggers a benign payload:
* **Desktop Interaction:** Opening a YouTube video (The "Rickroll").
* **UI Alerts:** Displaying a harmless system popup message.
* **System Feedback:** Writing events to a local log file for forensic analysis.

---

## 7. Killswitch (Emergency Stop)
A hardcoded safety mechanism is integrated into the core logic:
* **Trigger Path:** `C:\killswitch_mvs.txt`
* **Functionality:** If the agent detects this file at any point, it will **immediately self-terminate** and cease all background activities. This is a critical guardrail for ethical security simulations.

---

## 8. Ethical Limitations
Detailed technical exclusions (such as the absence of rootkits, memory injection, or real propagation) are documented in the `ethical_limitations.md` file. This project strictly follows "Red Team" rules of engagement.

---

## 9. Execution Instructions
Step-by-step setup for isolated Virtual Machine environments is provided in the `run_instructions.md` file.

---

## 10. Conclusion
This project provided a comprehensive look at adversarial behavior. By building a "virus" from scratch, I gained a deeper understanding of how to defend against one. The most significant takeaway was the importance of balancing technical complexity with ethical responsibility and safety guardrails.
