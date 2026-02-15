This project is a multi-client chat server built using Python socket programming and threading.
It allows multiple clients to connect simultaneously and communicate in real-time with username-password authentication.

The project demonstrates understanding of:
TCP/IP communication
Client-server architecture
Concurrent connections using threading
Basic authentication mechanisms

Features:
Multi-client support
TCP socket-based communication
Concurrent handling using threading

Tech Stack:
Python 3
Socket Programming
Threading
TCP/IP Networking

How It Works:
Server creates a TCP socket and binds to a specific port.
Server listens for incoming client connections.
For each new client, a separate thread is created.
Client must authenticate using predefined username-password.
After successful authentication:
Client can send messages.
Server broadcasts messages to other connected clients.
If client disconnects, server removes it from active connections list.
Server broadcasts messages to other connected clients.

How to Run:
1:Start the Server
(python server.py)
Server will start listening on configured IP and port.

2:Run Client (in separate terminal)
(python client.py)


Enter:
Server IP
Port
Username
Password







If client disconnects, server removes it from active connections list.
