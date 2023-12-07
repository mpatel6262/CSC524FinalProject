import socket
import sys

def start_client(server_host, server_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Receive and print the welcome message from the server
    while True:
        message = client_socket.recv(1024).decode()
        print(message)
        client_socket.send(input().encode())

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_host> <server_port>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    start_client(server_host, server_port)
