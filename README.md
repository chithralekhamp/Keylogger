# Keylogger

This project is a functional demonstration of a keystroke logging system, designed for educational purposes and security research.The tool runs silently in the background, captures keystrokes, and automatically emails the logs at set intervals. It uses pynput for keyboard input capture,

## ⚠️ Legal & Ethical Warning
**This software is for educational and authorized security research purposes only.**
Unauthorized use of keylogging software against systems or users without their explicit consent is illegal and unethical. By using this code, you agree to use it only in a lawful, controlled environment (such as a local VM or a dedicated research lab).

## Project Structure
The project consists of three main components:
* `logger.py`: The backend monitoring script that captures keystrokes.
* `app.py`: A Flask web server that serves the analysis dashboard.
* `index.html`: The frontend template that displays the logs and defensive research information.


KeyLogger
    
    │── app.py           (The Website)
    
    │── logger.py        (The Keylogger script)

    │── research_logs.txt (This will be created automatically)

    └── 📁 templates
         └── index.html   (The Dashboard)

---

## Component Details

### 1. The Logger (`logger.py`)
This script uses the `pynput` library to monitor keyboard events.
* **Functionality**: It listens for every keypress and records the character or special key (e.g., Space, Enter) into a local file named `research_logs.txt`.
* **Mechanism**: It utilizes system-level "hooks" to intercept input before it reaches the intended application.

### 2. The Dashboard Server (`app.py`)
A lightweight web application built with the Flask framework.
* **Functionality**: It reads the contents of `research_logs.txt` and renders them into a user-friendly web interface.
* **Configuration**: Runs locally on a debug server for real-time updates during research.

### 3. The Research Interface (`index.html`)
A dark-themed dashboard designed for security analysts.
* **Captured Input Log**: Displays a live-style feed of the data recorded by the logger.
* **Defensive Research Section**: Provides critical information on how to defend against keylogging attacks, including:
    * Multi-Factor Authentication (MFA)
    * Endpoint Detection and Response (EDR) Anti-Hooking
    * Keystroke Encryption
    * Virtual Keyboards

---

## Installation & Usage

### Prerequisites
* Python 3.x
* Flask: `pip install flask`
* Pynput: `pip install pynput`

### Running the Project
1.  **Start the Logger**:
    ```bash
    python logger.py
    ```
    The console will indicate "Security Research Monitor Active...". Type in any application to begin capturing data.

2.  **Launch the Dashboard**:
    Open a second terminal and run:
    ```bash
    python app.py
    ```

3.  **View Results**:
    Navigate to `http://127.0.0.1:5000` in your web browser to view the captured keystroke patterns and defensive tips.

## Defensive Strategies (Summary)
This project highlights that while logging is a powerful research tool, it is also a threat. 
Modern security posture relies on **MFA** to invalidate stolen credentials, **EDR** to detect the "Hooking" behavior seen in `logger.py`, and **Keystroke Encryption** to ensure that even if data is captured, it remains unreadable.
