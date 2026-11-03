# flask_labo

A Flask application that displays part of the server computer's screen in a browser. The capture rectangle is fixed at `(0, 0, 1050, 600)`, and frames are returned as **1050 × 600 PNG images** through `/screen.png`.

## Requirements

- An existing Python 3.14 installation.
- An accessible desktop session on the server computer.
- Flask 3.1.3 and Pillow 13.0.0, as specified in `requirements.txt`.

## Installation on macOS and Linux

From the project directory, create the environment once and install the dependencies:

```bash
python3.14 -m venv .venv314-compat
.venv314-compat/bin/python -m pip install -r requirements.txt
.venv314-compat/bin/python -m pip check
```

If the environment already exists and is ready, proceed directly to running the application. Do not recreate an existing environment.

## Running on macOS and Linux

From the project directory:

```bash
bash scripts/run
```

The script uses `.venv314-compat` directly. Manual environment activation is not required.

On the server computer, open [http://localhost:5000](http://localhost:5000).

To view the screen from another device on the local network, open `http://SERVER_IP:5000`, replacing `SERVER_IP` with the server computer's IP address. The application captures the screen of the computer running Flask.

## Running on Windows

From the project directory, using PowerShell or Command Prompt:

```powershell
py -3.14 -m venv .venv314-compat
.venv314-compat\Scripts\python.exe -m pip install -r requirements.txt
.venv314-compat\Scripts\python.exe -m pip check
.venv314-compat\Scripts\python.exe src\screen.py
```

Create the environment and install dependencies only once. For subsequent runs, use the final command.

## Compatibility Notes

- **macOS:** If prompted, allow the application running Python to capture the screen under System Settings → Privacy & Security → Screen Recording. Actual capture was tested on macOS 15.7.5 Intel with Python 3.14.10.
- **Linux:** Capture depends on the display session and available X11/XCB support or screenshot tools. Wayland support depends on the desktop environment.
- **Windows and Linux:** Actual screen capture was not tested on these platforms during this upgrade.
- The current startup configuration uses `0.0.0.0:5000` with `debug=True`. Use it on a trusted network and do not expose it directly to the internet.

## Troubleshooting `No module named 'PIL'`

Use `bash scripts/run` on macOS and Linux, or the environment-specific Python command above on Windows. If the error persists, install `requirements.txt` using Python inside `.venv314-compat` rather than the system-wide Python interpreter.
