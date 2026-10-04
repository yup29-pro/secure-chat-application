# 🔐 Secure Chat Application

A Python-based client-server chat application that uses **AES encryption** to protect messages during network communication.

## 📌 Overview

The Secure Chat Application demonstrates how cryptography can be integrated with network communication to provide confidential messaging.

Messages are encrypted using the **Advanced Encryption Standard (AES)** before transmission. The encrypted data is sent through a **TCP socket** to the server, which forwards the ciphertext to the intended client. The receiving client then decrypts the message using the shared AES key.

## ✨ Features

- 🔒 AES-128 message encryption
- 🌐 TCP socket-based communication
- 🖥️ Client-server architecture
- 🔐 Encrypted messages transmitted over the network
- 🔓 Decryption at the receiving client
- 👥 Communication between two clients
- 🐍 Implemented completely in Python

## 🏗️ System Architecture

```text
Client A
   │
   │ Plaintext Message
   ▼
AES Encryption
   │
   │ Encrypted Message
   ▼
Server
   │
   │ Encrypted Message
   ▼
Client B
   │
   ▼
AES Decryption
   │
   ▼
Original Message
```

The server only forwards encrypted data and does not decrypt the messages.

## 🛠️ Technologies Used

| Technology         | Purpose                           |
|--------------------|-----------------------------------|
| Python             | Application development           |
| Socket Programming | Client-server communication       |
| TCP                | Reliable network communication    |
| AES                | Message encryption and decryption |
| PyCryptodome       | Cryptographic implementation      |

## 📁 Project Structure

```text
secure-chat-application/
│
├── client.py
├── server.py
└── README.md
```

### `client.py`

Handles the chat interface, AES encryption of outgoing messages, and AES decryption of incoming messages.

### `server.py`

Handles client connections and forwards encrypted messages between connected clients.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yup29-pro/secure-chat-application.git
cd secure-chat-application
```

### 2. Install the Required Library

```bash
pip install pycryptodome
```

## ▶️ How to Run

The application requires **three terminals**:

- Terminal 1 → Server
- Terminal 2 → Client 1
- Terminal 3 → Client 2

### Step 1 — Start the Server

```bash
python server.py
```

The server will start on:

```text
127.0.0.1:5000
```

You should see:

```text
SECURE CHAT SERVER
Server started on 127.0.0.1:5000
Waiting for two clients...
```

### Step 2 — Start Client 1

Open a second terminal:

```bash
python client.py
```

Enter a name when prompted:

```text
Enter your name: Alice
```

### Step 3 — Start Client 2

Open a third terminal:

```bash
python client.py
```

Enter another name:

```text
Enter your name: Bob
```

### Step 4 — Send a Message

From Client 1:

```text
You: Hello Bob
```

The message is encrypted before transmission:

```text
Encrypted data being sent:
<encrypted hexadecimal data>
```

The receiving client gets the encrypted data and decrypts it:

```text
ENCRYPTED MESSAGE RECEIVED:
<encrypted hexadecimal data>

DECRYPTED MESSAGE:
Hello Bob
```

## 🔐 Security Workflow

```text
Plaintext Message
       ↓
AES Encryption
       ↓
Ciphertext
       ↓
TCP Socket Transmission
       ↓
Server
       ↓
Encrypted Ciphertext Forwarded
       ↓
Receiving Client
       ↓
AES Decryption
       ↓
Original Plaintext Message
```

The server forwards the encrypted data without decrypting the message.

## 🧪 Example

### Sender

```text
You: Hello Bob

Encrypted data being sent:
693f2f053c6269015149a477c6c4b830...
```

### Server

```text
Client 1 sent encrypted data:
693f2f053c6269015149a477c6c4b830...
```

### Receiver

```text
ENCRYPTED MESSAGE RECEIVED:
693f2f053c6269015149a477c6c4b830...

DECRYPTED MESSAGE:
Hello Bob
```

This demonstrates that the message is transmitted as encrypted ciphertext and converted back to readable text only at the receiving client.

## 🎯 Project Objective

The objective of this microproject is to demonstrate the integration of **cryptographic techniques with network socket programming** to establish secure communication between users.

## 🔑 Cryptography Used

### Advanced Encryption Standard (AES)

AES is used to encrypt and decrypt chat messages.

This project uses:

- **AES-128**
- **EAX mode**
- Shared secret key between the communicating clients
- Authentication tag for message verification

## 🌐 Network Communication

The application uses Python's built-in `socket` library to establish TCP-based communication.

```text
Client → TCP Socket → Server → TCP Socket → Client
```

The server acts as the communication layer between the two clients while encrypted messages remain unreadable during transmission.

## 🎓 Course Outcome

**CO2:** Apply mathematical concepts from number theory to design and solve problems related to cryptographic techniques.

## 📚 Project Type

**Cyber Network Security Microproject**

## 👨‍💻 Author

**Yashwanth R**

- GitHub: [@yup29_pro](https://github.com/yup29-pro)
- Repository: [Secure Chat Application](https://github.com/yup29-pro/secure-chat-application)

## ⚠️ Disclaimer

This project is developed for **educational and academic demonstration purposes**.

The AES key is included directly in the source code for simplicity. A production-level secure messaging application should use secure key management, authentication, protected key storage, and additional security mechanisms.
