import socket
import sys

def start_client(server_host):
    # Create a socket object
    start_port = 1000
    end_port = 10000  # Replace this with the end of the port range you want to scan

    # Loop through the port range and attempt to connect to each port
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)  # Set a timeout value (in seconds)

        try:
            # Attempt to connect to the port
            sock.connect((server_host, port))
            print(f"Port {port} is open")
        except socket.timeout:
            print(f"Port {port} timed out")
        except ConnectionRefusedError:
            print(f"Port {port} is closed")
        finally:
            sock.close()  # Close the socket
        # Close the connection with the server

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_host>")
        sys.exit(1)

    server_host = sys.argv[1]
    # server_port = int(sys.argv[2])

    start_client(server_host)
