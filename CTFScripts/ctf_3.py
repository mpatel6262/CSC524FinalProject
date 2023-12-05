key = "David August"

def CTF_3(server_socket, client_socket):
    message = "Enter Authentication Key:"
    client_socket.send(message.encode())
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        if message.casefold() == key.casefold():
            response = "Ground Station: Valid Authentication Key Provided!\n\nWelcome to our port scanning test.\nWe know all of our users are experts of creating sockets.\nDo you remember that instance you used for your first test, the timing attack, now you can spin up the program titled CTF_3.exe\nThe password is the same authentication key, 'David August'\nOnce connected, follow the instructions to receive your next authentication key\n\nEnter Authentication Step:"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Authentication Key: Try again."
        client_socket.send(response.encode())

