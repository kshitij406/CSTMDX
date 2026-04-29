import pickle
import socket
HOST = '127.0.0.1'
PORT = 65432
# step 1 Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2  Bind host and a port with a specific socket
server_socket.bind((HOST, PORT))

# step 3 Listen for a connection from the client
server_socket.listen(1)
print('Waiting for connection')

# step 4 Accept requests from a client socket, keeps waiting for incoming connections
socket_client, (host, port) = server_socket.accept()
print(f'Received connection from {host} ({port})\n')
print(f'Connection Established from: {host}')

# step 5 Unpicking
received_data = socket_client.recv(1024)
received_object = pickle.loads(received_data)
print(f': We received from Client:: {received_object} ')

# step 6 Close the connection
socket_client.close()




