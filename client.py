import socket
import threading
import struct

from Crypto.Cipher import AES


# ==============================
# SERVER SETTINGS
# ==============================

HOST = "127.0.0.1"
PORT = 5000


# ==============================
# AES SECRET KEY
# ==============================

# AES requires a key of 16, 24, or 32 bytes.
# We are using a 16-byte key = AES-128.

KEY = b"1234567890123456"


# ==============================
# AES ENCRYPTION
# ==============================

def encrypt_message(message):

    # Create AES cipher
    cipher = AES.new(
        KEY,
        AES.MODE_EAX
    )

    # Encrypt message
    ciphertext, tag = cipher.encrypt_and_digest(
        message.encode()
    )

    # Store:
    # nonce + tag + ciphertext

    return cipher.nonce + tag + ciphertext


# ==============================
# AES DECRYPTION
# ==============================

def decrypt_message(data):

    # Extract nonce
    nonce = data[:16]

    # Extract authentication tag
    tag = data[16:32]

    # Extract encrypted message
    ciphertext = data[32:]

    # Create AES cipher
    cipher = AES.new(
        KEY,
        AES.MODE_EAX,
        nonce=nonce
    )

    # Decrypt and verify
    plaintext = cipher.decrypt_and_verify(
        ciphertext,
        tag
    )

    return plaintext.decode()


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
# RECEIVE MESSAGES
# ==============================

def receive_messages():

    while True:

        try:

            # Receive message size
            header = receive_all(
                client,
                4
            )

            if not header:
                break

            message_size = struct.unpack(
                "!I",
                header
            )[0]

            # Receive encrypted message
            encrypted_message = receive_all(
                client,
                message_size
            )

            if not encrypted_message:
                break

            print("\n")
            print("-" * 50)

            print("ENCRYPTED MESSAGE RECEIVED:")
            print(encrypted_message.hex())

            # Decrypt
            message = decrypt_message(
                encrypted_message
            )

            print("\nDECRYPTED MESSAGE:")
            print(message)

            print("-" * 50)

            print("\nYou: ", end="", flush=True)

        except Exception as e:

            print("\nError receiving message:", e)
            break


# ==============================
# CONNECT TO SERVER
# ==============================

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    (HOST, PORT)
)


# ==============================
# USER NAME
# ==============================

name = input("Enter your name: ")


print("\n")
print("=" * 50)
print("          SECURE CHAT CLIENT")
print("=" * 50)

print("Connected to server.")
print("AES encryption is active.")

print("\nType 'exit' to close the chat.\n")


# ==============================
# START RECEIVING THREAD
# ==============================

receive_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

receive_thread.start()


# ==============================
# SEND MESSAGES
# ==============================

while True:

    message = input("You: ")

    # Exit
    if message.lower() == "exit":

        break

    # AES encryption
    encrypted_message = encrypt_message(
        message
    )

    print("\nEncrypted data being sent:")

    print(
        encrypted_message.hex()
    )

    # Send message size first
    client.send(
        struct.pack(
            "!I",
            len(encrypted_message)
        )
    )

    # Send encrypted message
    client.send(
        encrypted_message
    )

    print()


# ==============================
# CLOSE CONNECTION
# ==============================

client.close()

print("Disconnected from server.")