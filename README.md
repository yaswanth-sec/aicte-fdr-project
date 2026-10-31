# AICTE FDR Management Portal — Full Project

## Project structure

app/
  main.py              Flask backend and API foundation
  __init__.py
templates/
  index.html           Full working portal prototype/UI
static/
  README.txt           Static-assets folder
data/
  sample_data.json     Sample backend data
  audit.jsonl          Created automatically when audit events are posted
uploads/               Future secure document-upload storage
instance/              Runtime configuration/database location
requirements.txt       Python dependencies
run_windows.bat        One-click Windows launcher
run_mac_linux.sh       macOS/Linux launcher

## Run on Windows

Double-click `run_windows.bat`.

Then open:
http://127.0.0.1:5000

## Run on macOS/Linux

In Terminal:
./run_mac_linux.sh

Then open:
http://127.0.0.1:5000

## Demo accounts

The prototype automatically creates the initial local accounts:
- officer1 / demo123
- sunrise1 / demo123

You can also use Create new account in the login portal.

## Important security note

The browser prototype includes client-side password hashing, session timeout and failed-login protection for demonstration purposes. For a production system, authentication and authorization must be moved to the backend with secure password hashing (Argon2/bcrypt), server-side sessions/JWT with appropriate rotation, HTTPS, CSRF protection, database-backed users and roles, secure file storage, virus scanning for uploads, and immutable server-side audit logs.
