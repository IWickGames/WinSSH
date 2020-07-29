# WinSSH
 SSH type client for Windows computers

# Easy setup
 - Download or clone the repo
 - Look in the BUILD folder
 - Run install.bat as admin
 - Setup the Username and Password
 - Done! The SSH server is now running on port 37

# Uninstall
 - Run the unintall.bat as admin and it will automaticly uninstall the WinSSH server

# Client usage
 The WinSSH client is built into the server. To use it just execute the WinSSH.exe via command line
 It will ask you for the IP address to connect to then ask for the login details for the client if the connection was successfull
 
 If your login was successfull you will be connected to the WinSSH server and be allowed to execute commands

# Warning
 WinSSH runs on port 37, for security do not open this port unless you know what you are doing.
 This can open large security issues on your network if your password is week as it will allow
 attackers if they guess your week password to execute commands on your computer without your
 knowledge.