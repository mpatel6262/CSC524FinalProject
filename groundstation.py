import socket
import time
from CTFScripts.ctf_1 import CTF_1
from CTFScripts.ctf_2 import CTF_2
from CTFScripts.ctf_3 import CTF_3
from CTFScripts.ctf_4 import CTF_4

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 23456  # Port to bind to

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(1000)

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
            globals()["CTF_" + message](server_socket, client_socket)
        except:
            message = "Invalid Authentication Step, Reenter authentication step:"
            client_socket.send(message.encode())


if __name__ == "__main__":
    start_server()
