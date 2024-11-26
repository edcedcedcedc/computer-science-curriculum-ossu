import socket
import select
import signal
import time 
import threading
from i_am_common import SERVER_HOST,SERVER_PORT

shutdown_flag = False

clients = {}
blocked = {}
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}.")
  
    username = ""

    try:
        
        while not username:
            try:
                readable, _, _ = select.select([client_socket], [], [], 3)  # Timeout 3 seconds
                username = client_socket.recv(1024).decode().strip()
                if client_socket in readable:
                    clients[username] = client_socket  # Store username and socket
                    print(f"{client_address} registered as {username}.")
    
            except BlockingIOError:
                time.sleep(0.1) 
                continue    
    
        while not shutdown_flag:

            try:
                message = client_socket.recv(1024)

                if not message:
                    raise ConnectionResetError

                message = message.decode().strip()

                if message.startswith("BLOCK "):
                    recipients = message[6:]
                    recipients = eval(recipients)
                    for recipient in recipients:
                        if recipient in clients:
                            if username not in blocked:
                                blocked[username] = []
                            blocked[username].append(recipient)
                            recipient_socket = clients[recipient]
                            recipient_socket.sendall(f"You have been restricted by username {username}".encode())
                        

                elif message.startswith("SEND "):
                    parts = message[5:].split(":", 1)
                    recipients, msg_body = parts
                    recipients = eval(recipients)
                    msg_body = msg_body.strip()
        
                    for recipient in recipients:
                        if recipient in clients:
                            for k, v in blocked.items():
                                if k == username:
                                    if recipient not in v:
                                        recipient_socket = clients[recipient]
                                        recipient_socket.sendall(f"Message from {username}: {msg_body}".encode())
         
                        else:
                            client_socket.sendall(f"Error: Recipient {recipient} not found.".encode())

                elif message.startswith("BROADCAST"):
                    parts = message[9:].split(":", 1)
                    _, msg_body = parts
                    for recipient, recipient_socket in clients.items():
                        if username != recipient:
                            recipient_socket.sendall(f"Broadcast from {username}:{msg_body}".encode())

                else:
                    client_socket.sendall("Error: Invalid message format. Use 'SEND recipient:message' or 'BROADCAST: message.".encode())
            
            except BlockingIOError:
                time.sleep(0.1) 
                continue

            except ConnectionResetError:
                break
            

    finally:
        if username in clients:
            del clients[username]
        client_socket.close()
        print(f"Connection with client address: {client_address} username: {username} closed.")
        if username in blocked:
            del blocked[username]
            print(f"Blocked list for username {username} has been erased due to disconnect.")

# Function to handle the shutdown signal
def shutdown_server(signal, frame):
    global shutdown_flag
    print("Keyboard interrupt detected! Shutting down server...")
    shutdown_flag = True

def start_server():
    global shutdown_flag
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow socket reuse
    server_socket.bind((SERVER_HOST, SERVER_PORT))  # Listen on all available interfaces
    server_socket.listen(5)
    server_socket.setblocking(0)  # Make the server socket non-blocking
    print(f"Server is running on port {SERVER_PORT}... Press Ctrl+C to stop.")

    try:
        while not shutdown_flag:
            # Use select to check if the server socket is ready to accept a new connection
            readable, _, _ = select.select([server_socket], [], [], 3)  # Timeout 3 seconds
            if server_socket in readable:
                client_socket, client_address = server_socket.accept()
                # Create a new thread to handle each client independently
                # Pass the handle_client as a callback
                """ client_socket.sendall(f"Succesifly connected to {SERVER_HOST}".encode()) """
                #client_socket.sendall(f"Succesifly connected to {SERVER_HOST}".encode())
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()

            if shutdown_flag:
                break

    except KeyboardInterrupt:
        pass 

    finally:
        server_socket.close()
        print("Server socket closed.")

# Setup signal handler for Ctrl+C
signal.signal(signal.SIGINT, shutdown_server)

if __name__ == "__main__":
    start_server()




