def sshClient():
    import os
    import sys
    import hashlib
    import serverProc

    loginAddress = input("connection_address$ ") #Input for connection address

    try:
        rep = serverProc.TCPClient(loginAddress, 37, "PING") #Send ping request
        if rep != "PONG": #Check to make sure the server sent the correct responce
            print("Failed to connect to: " + str(loginAddress))
            sys.exit()
    except: #Check if a connection to the server cant be esablished
        print("Failed to connect to: " + str(loginAddress))
        sys.exit()

    print(f"Connected to {loginAddress}") #Connection successfull!

    sessionToken = None #Set sessionToken to nothing
    while not sessionToken: #Keep asking for creds untill a sessionToken is successfully sent
        loginUsername = input("username$ ")
        loginPassword = input("password$ ")

        validationHash = hashlib.sha512(f"{loginUsername}{loginPassword}".encode("utf-8")).hexdigest() #Hash creds

        rep = serverProc.TCPClient(loginAddress, 37, f"GET_SESSION:{validationHash}") #Post creds hash to server for session token
        if rep != "LOGIN_FAILED":
            sessionToken = rep
        else:
            print("Login failed, try again")

    while True: #Start client interface, now the session token must be sent with the message for it to be executed
        try:
            command = input("$ ")
        except KeyboardInterrupt:
            break

        if command == "close":
            break

        try:
            responce = serverProc.TCPClient(loginAddress, 37, f"EXECUTE_SHELL:{sessionToken}:{command}")
            print(responce)
        except ConnectionRefusedError:
            print("Lost connection with SSH server")
        except:
            print("Lost connection with SSH server")
