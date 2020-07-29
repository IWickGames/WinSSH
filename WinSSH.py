import os
import sys
import json
import hashlib
import threading
import serverProc

import sshClient
import sshServer

arguments = sys.argv

if len(arguments) == 1:
    sshClient.sshClient()
    sys.exit()

if arguments[1] == "-startup":
    threading.Thread(target=sshServer.sshServer).start()
    sys.exit()

if arguments[1] == "-passwd":
    print("Set your WinSSH username and password(make sure they are secure)")
    loginUsername = input("Username: ")
    loginPassword = input("Password: ")

    loginHash = hashlib.sha512(f"{loginUsername}{loginPassword}".encode("utf-8")).hexdigest()

    with open("creds.winssh", "w") as f:
        f.write(loginHash)
    
    sys.exit()