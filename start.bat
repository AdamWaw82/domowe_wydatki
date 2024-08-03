@echo off
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python nie jest zainstalowany.
    pause
    exit /b
)

IF NOT EXIST "venv" (
    python -m venv venv
)

call venv\Scripts\activate

pip install --upgrade pip
IF EXIST requirements.txt (
    pip install -r requirements.txt
)

python app.py

deactivate