@echo off
title 🚀 HoloVoice Builder
color 0B

echo 🔁 Удаление предыдущих сборок...
rd /s /q build >nul 2>&1
rd /s /q dist >nul 2>&1
del holovoice.spec >nul 2>&1
echo ✔ Готово

echo.
echo 🔨 Сборка EXE с иконкой...
if exist icon.ico (
    pyinstaller --noconfirm --onefile --windowed --icon=icon.ico holovoice.py
) else (
    pyinstaller --noconfirm --onefile --windowed holovoice.py
)

echo.
echo 🧪 Запуск собранного EXE...
start dist\holovoice.exe

echo.
echo 📦 Архивация в HoloVoice.zip...
powershell Compress-Archive -Path dist\holovoice.exe -DestinationPath HoloVoice.zip -Force

echo.
echo ✅ Готово! holovoice.exe и HoloVoice.zip созданы
pause
3 