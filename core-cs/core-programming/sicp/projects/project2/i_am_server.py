import socket
import select
import signal
import time 
import threading
from i_am_common import SERVER_HOST,SERVER_PORT

shutdown_flag = False

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        while not shutdown_flag:

            try:
                message = client_socket.recv(1024)
                if not message:
                    break
                message = message.decode().strip()
                print(f"Message from {client_address}: {message}")
                
                if message.startswith("SEND "):
                    parts = message[5:].split(":", 1)
                    if len(parts) == 2:
                        recipient, msg_body = parts
                        recipient = recipient.strip()
                        msg_body = msg_body.strip()
                        client_socket.sendall(f"Echoing to you: {msg_body}".encode())
                    else:
                        client_socket.sendall("Error: Invalid message format. Use 'SEND recipient:message'.".encode())
                else:
                    client_socket.sendall("Error: Invalid message format. Use 'SEND recipient:message'.".encode())
            
            except BlockingIOError:
                time.sleep(0.1) 
                continue

    except Exception as e:
        print(f"Error with {client_address}: {e}")

    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed.")

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
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()

            # Periodically check for shutdown signal
            if shutdown_flag:
                break

    except KeyboardInterrupt:
        # Let the shutdown signal handle it
        pass 

    finally:
        server_socket.close()
        print("Server stopped.")

# Setup signal handler for Ctrl+C
signal.signal(signal.SIGINT, shutdown_server)

if __name__ == "__main__":
    start_server()




