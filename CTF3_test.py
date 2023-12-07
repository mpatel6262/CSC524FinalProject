import socket

password = "David August"
entered_pass = ""

while entered_pass.casefold() != password.casefold():
    entered_pass = input("Enter Password: ")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
host = socket.gethostname()
port = 4500  # Port to bind to

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

print(f"Correct password entered\nServer listening on {host}:XXXXX\nMake a connection to receive your next key\nTo help you out, the port is between 1000 and 10000 (inclusive!)")

client_socket, addr = server_socket.accept()

message = "Congratulations, you found the right port number!\nI hope you didn't enter them manually!\nYour next authentication key is what you get when you translate 'Stephen Beard' to Korean? Looks like you were taking Korean lessons again..."
print(message)
client_socket.close()
server_socket.close()