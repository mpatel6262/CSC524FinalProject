import socket
import time

correct_ID = "14-214"
correct_password = "twosigma"

def check_password(message):
    for i in range(0, len(correct_password)):
        if (i >= len(message) or message[i] != correct_password[i]):
            return False
        time.sleep(0.05)
    return True

def check_ID(message):
    for i in range(0, len(correct_ID)):
        if (i >= len(message) or message[i] != correct_ID[i]):
            return False
        time.sleep(0.05)
    return True


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345  # Port to bind to

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Send a welcome message to the client
    message = "Welcome to the server! Enter your ground station location ID:"
    client_socket.send(message.encode())

    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        if check_ID(message):
            response = "Server: Valid ID Provided, Enter your Password:"
            client_socket.send(response.encode())
            break
        
        response = "Server: Incorrect ground station location ID: Try again."
        client_socket.send(response.encode())


    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        if check_password(message):
            response = "Server: Valid Password!\nWelcome Stephen Beard!"
            client_socket.send(response.encode())
            break
        
        response = "Server: Incorrect Password: Try Again."
        client_socket.send(response.encode())

    client_socket.close()

if __name__ == "__main__":
    start_server()
