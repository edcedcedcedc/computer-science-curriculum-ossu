import socket
import threading
import select
from i_am_common import SERVER_HOST, SERVER_PORT, MESSAGE_END


def listen_for_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print("Server closed the connection.")
                break

            print(f"{message.decode()}")

        except ConnectionAbortedError:
            break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def start_client():

    try:
        print(f"Initiating a connection to {SERVER_HOST}, {SERVER_PORT}...")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        readable, _, _ = select.select([client_socket], [], [], 3)

        if readable:
            message = client_socket.recv(1024)
            if message:
                print(f"{message.decode()}")
        else:
            raise TimeoutError

        try:
            username = input("Enter your username: ")
            client_socket.sendall(username.encode())

            listener_thread = threading.Thread(
                target=listen_for_messages, args=(client_socket,), daemon=True
            )
            listener_thread.start()

            while True:
                message = input("")

                if message.lower() == "exit":
                    raise KeyboardInterrupt

                if message.startswith("SEND "):
                    if ":" in message[5:]:
                        recipients, rest = message[5:].split(":", 1)
                        recipients = recipients.split()
                        formatted_message = f"SEND {recipients}: {rest}"

                        client_socket.sendall(formatted_message.encode())

                elif message.startswith("BLOCK "):
                    recipients = message[6:].split(" ")
                    if recipients:
                        formatted_message = f"BLOCK {recipients}"
                        client_socket.sendall(formatted_message.encode())

                elif message.startswith("BROADCAST"):
                    if ":" in message[9:]:
                        _, rest = message[9:].split(":", 1)
                        formatted_message = f"BROADCAST: {rest}"

                        client_socket.sendall(formatted_message.encode())

                else:
                    print(
                        "Error: Invalid message format. Use 'SEND recipient:message'."
                    )

        except KeyboardInterrupt:
            print("\nDisconnected.")

        finally:
            client_socket.close()

    except ConnectionRefusedError:
        print(f"Connection refused, cannot connected to {SERVER_HOST}:{SERVER_PORT}.")


if __name__ == "__main__":
    start_client()
