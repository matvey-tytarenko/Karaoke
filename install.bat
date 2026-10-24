@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === Установка караоке ===

where python >nul 2>nul
if errorlevel 1 goto nopython

where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo [*] Устанавливаю ffmpeg...
    winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
)
where deno >nul 2>nul
if errorlevel 1 (
    echo [*] Устанавливаю Deno - он нужен yt-dlp для YouTube...
    winget install -e --id DenoLand.Deno --accept-source-agreements --accept-package-agreements
)

if not exist .venv (
    echo [*] Создаю виртуальное окружение...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip

where nvidia-smi >nul 2>nul
if errorlevel 1 goto cpu
echo [*] Найдена видеокарта NVIDIA - ставлю PyTorch с CUDA...
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu128
goto rest
:cpu
echo [*] Видеокарта NVIDIA не найдена - ставлю PyTorch для процессора...
pip install torch torchaudio
:rest
pip install -r requirements.txt
echo.
echo === Готово! Закрой это окно и запусти run.bat ===
echo (если ffmpeg или Deno только что установились - открой новое окно, чтобы они стали видны)
pause
exit /b 0

:nopython
echo Python не найден. Установи Python 3.11 или 3.12 с python.org
echo и при установке поставь галочку "Add Python to PATH".
pause
exit /b 1
