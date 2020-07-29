@echo off
cd "%~dp0"
echo Uninstalling WinSSH...
taskkill /im WinSSH.exe /f >nul

rd /s /q "C:\Program Files\WinSSH" >nul
del /f /q "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\WinSSH-AutoStart.vbs" >nul

echo Uninstalled WinSSH
pause >nul
exit