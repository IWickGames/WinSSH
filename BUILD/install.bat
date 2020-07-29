@echo off
cd "%~dp0"
echo Installing WinSSH...

taskkill /im WinSSH.exe /f >nul
mkdir "C:\Program Files\WinSSH" >nul
copy /-Y "WinSSH.exe" "C:\Program Files\WinSSH\WinSSH.exe" >nul
call "C:\Program Files\WinSSH\WinSSH.exe" -passwd
copy /-Y "creds.winssh" "C:\Program Files\WinSSH\creds.winssh"

echo Ready to start service

copy /-Y "WinSSH-AutoStart.vbs" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\WinSSH-AutoStart.vbs" >nul
start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\WinSSH-AutoStart.vbs" >nul

echo WinSSH server is now running!

pause >nul
exit