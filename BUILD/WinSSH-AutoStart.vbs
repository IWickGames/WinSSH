Set WshShell = WScript.CreateObject ("WScript.Shell")
WshShell.Run """C:\Program Files\WinSSH\WinSSH.exe"" -startup", 0
Set WshShell = Nothing