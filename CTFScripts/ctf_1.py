import time

def CTF_1(server_socket, client_socket):
    message = "To get started, you need to provide your ground station ID. Good luck finding that though the only place those are stored are all the way up on the satellite.\nI heard that thing is pretty ancient though and has to check IDs and passwords one character at a time?\nProbably built on one of those 8-bit calculators and was never updated...\n\nLucky for us, this ground station is state of the art, so it can process the whole ID and password at once!\n\nEnter Ground Station Location ID:"
    client_socket.send(message.encode())
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        time.sleep(5)
        if message == "14-214":
            response = "Ground Station: Valid ID Provided, Enter your Password:"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect ground station location ID: Try again."
        client_socket.send(response.encode())


    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        time.sleep(5)
        if message == "twosigma":
            response = "\nGround Station: Valid Password!\nWelcome Stephen Beard!\nReminder: You set your PhD dissertation title as Authentication Key 2.\nI'm not really sure why you did that!\n\nEnter Authentication Step:"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Password: Try Again."
        client_socket.send(response.encode())