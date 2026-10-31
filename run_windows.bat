@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  py -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo AICTE FDR Portal is starting at http://127.0.0.1:5000
echo Press Ctrl+C to stop.
python app\main.py
