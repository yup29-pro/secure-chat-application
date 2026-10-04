import socket
import threading
import struct

# ==============================
# SERVER SETTINGS
# ==============================

HOST = "127.0.0.1"
PORT = 5000

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(2)

print("=" * 50)
print("          SECURE CHAT SERVER")
print("=" * 50)
print(f"Server started on {HOST}:{PORT}")
print("Waiting for two clients...\n")


# Store connected clients
clients = []


# ==============================
# RECEIVE EXACT NUMBER OF BYTES
# ==============================

def receive_all(sock, size):

    data = b""

    while len(data) < size:

        packet = sock.recv(size - len(data))

        if not packet:
            return None

        data += packet

    return data


# ==============================
# FORWARD MESSAGE
# ==============================

def handle_client(client_socket, client_number):

    try:

        while True:

            # Receive message size
            header = receive_all(client_socket, 4)

            if not header:
                break

            message_size = struct.unpack("!I", header)[0]

            # Receive encrypted message
            encrypted_message = receive_all(
                client_socket,
                message_size
            )

            if not encrypted_message:
                break

            print(
                f"Client {client_number} sent encrypted data:"
            )

            print(encrypted_message.hex())
            print()

            # Send encrypted message to other client
            for client in clients:

                if client != client_socket:

                    client.send(
                        struct.pack(
                            "!I",
                            len(encrypted_message)
                        )
                    )

                    client.send(encrypted_message)

    except Exception as e:

        print("Connection error:", e)

    finally:

        if client_socket in clients:
            clients.remove(client_socket)

        client_socket.close()

        print(f"Client {client_number} disconnected.")


# ==============================
# ACCEPT CLIENTS
# ==============================

client_number = 1

while len(clients) < 2:

    client_socket, address = server.accept()

    clients.append(client_socket)

    print(
        f"Client {client_number} connected:"
        f" {address}"
    )

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_number),
        daemon=True
    )

    thread.start()

    client_number += 1


print("\nBoth clients connected!")
print("Secure chat is ready.\n")

# Keep server running
while True:

    pass