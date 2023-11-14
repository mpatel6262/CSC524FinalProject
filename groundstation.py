import socket
import time

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 23456  # Port to bind to

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Send a welcome message to the client
    message = "Welcome to the ground station! Enter Authentication Step:"
    client_socket.send(message.encode())
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        try:
            globals()["CTF_" + message](client_socket)
        except:
            message = "Invalid Authentication Step, Reenter authentication step:"
            client_socket.send(message.encode())

def CTF_1(client_socket):
    message = "Enter Ground Station Location ID:"
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
            response = "\nGround Station: Valid Password!\nWelcome Stephen Beard!\n\nEnter Authentication Step:"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Password: Try Again."
        client_socket.send(response.encode())


if __name__ == "__main__":
    start_server()
