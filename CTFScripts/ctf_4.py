import time, socket

key = "스티븐 비어드"

def CTF_4(server_socket, client_socket):
    message = "Enter Authentication Key:"
    client_socket.send(message.encode())
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        if message == key:
            response = "Ground Station: Valid Authentication Key Provided!\nWelcome to our Regular Denial of Service test (not to be confused wiuth ReDoS)\nWe want to see if you can make a sufficient number of connections to this socket within ten seconds.\nType 'go' when you are ready\n"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Authentication Key: Try again."
        client_socket.send(response.encode())
    
        
    server_socket.settimeout(10)
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        response = ""
        if message == "go":
            t1 = time.time()
            sockets_list = []
            while time.time() - t1 < 10:
                try:
                    sockets_list.append(server_socket.accept())
                except socket.timeout:
                    pass
            print(sockets_list)
            if len(sockets_list) > 50:
                response = "Congratulations, you did it!\nThis is the current end of our CTF!\nWe hope you enjoyed and maybe will even contribute a new step or two for this project\n\nEnter Authentication Step:"
                client_socket.send(response.encode())
                break
                
            response = "Looks like you didnt make enough connections in time\n"
            for sock in sockets_list:
                try:
                    sock.close()
                except:
                    pass
        response += "Type 'go' when you are ready\n"
        client_socket.send(response.encode())

    server_socket.settimeout(None)