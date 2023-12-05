import socket
import sys

def create_connection(ip, port):
    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((ip, port))

        # Perform any necessary operations here
        # ...

        # Close the connection
        client_socket.close()

        print(f"Connection {ip}:{port} established")
    except Exception as e:
        print(f"Connection {ip}:{port} failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 connect.py <ip_address> <port>")
        sys.exit(1)

    ip_address = sys.argv[1]
    port = int(sys.argv[2])

    create_connection(ip_address, port)
