import time

key = "스티븐 비어드"

def CTF_4(server_socket, client_socket):
    message = "Enter Authentication Key:"
    client_socket.send(message.encode())
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        if message == key:
            response = "Ground Station: Valid Authentication Key Provided!\nWelcome to our Regular Denial of Service test (not to be confused wiuth ReDoS)\nWe want to see if you can make a sufficient number of connections to this socket within ten seconds.\nType 'go' "
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Authentication Key: Try again."
        client_socket.send(response.encode())
    
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        if message == "go":
            break
        
        response = "Type 'go' when you are ready"
        client_socket.send(response.encode())

    while True:
        t1 = time.time()
        sockets_list = []
        response = "Start!\n"
        client_socket.send(response.encode())
        while time.time() - t1 < 10:
            sockets_list.append(server_socket.accept())
        print(sockets_list)