@echo off
chcp 65001 >nul
cd /d "%~dp0"
call .venv\Scripts\activate.bat
echo Обновляю yt-dlp (YouTube часто что-то меняет)...
pip install -U "yt-dlp[default]"
pause
