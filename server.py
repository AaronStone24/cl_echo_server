import socket

# socket.AF_INET - the type of address our socket will be able to interact with (hostname and a port number here)
# socket.SOCK_STREAM - using TCP protocol for our communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# setting socket.SO_REUSEADDR flag to 1 which will allow us to resuse the port number after we stop and restart
# the application
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)

server_socket.listen()  # listen for connections from clients

try:    
    connection, client_address = server_socket.accept() # wait for an incoming connection and return the socket representing
    # the connection and the client address 
    print(f"The server got a connection from {client_address}!")

    buffer = b''

    while buffer[-2:] != b'\r\n': # Keep receiving the message from client until we encounter '\r\n'
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"I got data: {data}")
            buffer = buffer + data
    
    print(f"All the data is: {buffer}")
    connection.sendall(buffer)
finally:
    server_socket.close()
