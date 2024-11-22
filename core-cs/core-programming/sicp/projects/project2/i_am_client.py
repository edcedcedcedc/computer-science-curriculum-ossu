import socket
from i_am_common import SERVER_HOST, SERVER_PORT, MESSAGE_END

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT)) 
    print(f"Connected to {SERVER_HOST}:{SERVER_PORT} {MESSAGE_END}")

    try:
        while True:
            # Read the message from the user
            message = input("Enter a message (type 'exit' to quit): ")
            
            # Exit condition
            if message.lower() == "exit":
                break

            # Check if the message starts with "SEND"
            if message.startswith("SEND "):
                client_socket.sendall(message.encode())
                response = client_socket.recv(1024)
                print(f"Server response: {response.decode()}")
            else:
                print("Error: Invalid message format. Use 'SEND recipient:message'.")

    except KeyboardInterrupt:
        print("\nDisconnected.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()

