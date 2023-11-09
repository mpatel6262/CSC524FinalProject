import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345  # Port to bind to

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Send a welcome message to the client
    message = "Welcome to the server! Enter your ground station ID:"
    client_socket.send(message.encode())

    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        # Compare the received message with a predefined string
        correct_string = "Hello, Server!"
        if message == correct_string:
            response = "Valid ID Provided, Enter your Password"
            break
        else:
            response = "Incorrect ground station ID:. Try again."

        client_socket.send(response.encode())
        # Close the connection with the client
        #client_socket.close()

    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        # Compare the received message with a predefined string
        correct_string = "Hello, Server!"
        if message == correct_string:
            response = "Valid Password Provided, Welcome!"
            break
        else:
            response = "Incorrect ground station ID:. Try again."

        client_socket.send(response.encode())

    client_socket.close()

if __name__ == "__main__":
    start_server()
