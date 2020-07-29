def sshServer():
    import socket #Import sockets
    import random #Import random library
    import serverProc #Import serverProc library
    import subprocess #Import subprocess

    global activeSessions
    activeSessions = []

    hostname = socket.gethostname() #Get client hostname
    localIpAddr = socket.gethostbyname(hostname) #Get client local address

    def commandHandler(command): #Create command handler
        def genSessionToken():
            token = ""
            for _ in range(0, 50):
                token += random.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"))
            return token

        if command == "PING":
            return "PONG"

        if command.startswith("GET_SESSION"): #Check if the user is generating a token
            with open("creds.winssh") as f: #Grab login hash from the file
                validSSHTOKEN = f.read()
            
            if command.split(":", 1)[1] == validSSHTOKEN: #Validate the hash
                genSessionToken = genSessionToken() #Login was successfull, generate valid session token and store it
                activeSessions.append(genSessionToken) #Save session token to list
                return genSessionToken #Return generated token to connecting client
            else:
                return "LOGIN_FAILED"

        if command.startswith("GET_DEVICE_NAME"): #Get Device info return
            return f"{hostname}" #Return device name
        
        if command.startswith("EXECUTE_SHELL"): #Execute command as shell
            if len(command.split(":", 2)) != 3: #Make sure arguments are valid
                return "ERROR" #If invalid return error

            session = command.split(":", 2)[1] #Extract session token
            rawCommand = command.split(":", 2)[2] #Extract command

            if not session in activeSessions:
                return "ERROR"
            
            try:
                commandOutput = subprocess.check_output(rawCommand, shell=True).decode("utf-8")
            except:
                commandOutput = "Command failed to execute"
            
            return commandOutput
        
        if command.startswith("CLOSE_SESSION"):
            token = command.split(":", 1)[1]

            if not token in activeSessions:
                return "ERROR"
            
            try:
                activeSessions.remove(token)
            except:
                pass
            return "TRUE"
            

            


        
    while True: #Start connection loop
        try:
            connectionSave, connectionAddress, command = serverProc.TCPServerRecieve(localIpAddr, 37) #Wait for a WinSSH client to connect

            try:
                with open("winssh.log", 'a') as f: #Write connection to log
                    f.write(f"{connectionAddress} | POST_RAW_CMD: {command}" + "\n")
            except:
                pass
            
            try:
                commandOutput = commandHandler(command)
            except:
                commandOutput = "COMMAND_ERROR"

            serverProc.TCPServerRespond(connectionSave, commandOutput) #Return command output to WinSSH client
        except:
            pass