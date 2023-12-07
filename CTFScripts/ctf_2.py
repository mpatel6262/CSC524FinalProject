import re, time, multiprocessing

title = "TRUSTGUARD: A MODEL FOR PRACTICAL TRUST IN REAL SYSTEMS"
solution = "^(a+)+$"
#message = "TRUSTGUARD: A MODEL fOR PRACTICAL tRUST IN REAL SYSTEMs"
# if message.casefold() == title.casefold():
#     print("Pass")

def execute_with_timeout(target_function, arguments, timeout_seconds):
    # Create a process to run the target function
    process = multiprocessing.Process(target=target_function, args=arguments)

    # Start the process
    process.start()

    # Wait for the process to finish or timeout
    process.join(timeout=timeout_seconds)

    # If the process is still alive (didn't finish within the timeout), terminate it
    if process.is_alive():
        process.terminate()
        return -1
        # You can execute additional code here when the function times out
    else:
        return 0
    
def CTF_2(server_socket, client_socket):
    message = "Enter Authentication Key:"
    client_socket.send(message.encode())
    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        if message.casefold() == title.casefold():
            response = "Ground Station: Valid Authentication Key Provided!\nWelcome to our ReDoS test.\nWe know all of our users are experts of ReDoS.\n\nWhy did the coder's ReDoS algorithm tell bad jokes?\n\nBecause it got stuck in an infinite loop trying to match the perfect punchline, only to realize it was chasing a joke that was more elusive than debugging on a Monday morning!\n\nPretend that someone is attempting to login with password 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaab'\nProvide a Regex. pattern which would be vulnerable to this password and timeout:"
            client_socket.send(response.encode())
            break
        
        response = "Ground Station: Incorrect Authentication Key: Try again."
        client_socket.send(response.encode())


    while True:
        # Establish a connection
        message = client_socket.recv(1024).decode()
        
        print(f"Received message: {message}")
        t1 = time.time()
        
        ret = execute_with_timeout(re.match, (message, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaab'), 10)
        if ret == -1:
            response = "Nice Job! That took longer than ten seconds so clearly you know something!\nYour next authentication key is your research advisor's name [FIRST LAST]. You must really like this guy!\n\nEnter Authentication Step:"
            client_socket.send(response.encode())
            return
        else:
            response = "Not quite, that only took " + str(time.time() - t1) + " seconds, try again:"
            client_socket.send(response.encode())
