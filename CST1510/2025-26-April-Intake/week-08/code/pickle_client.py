import pickle
import socket
from Animal import *



HOST = '127.0.0.1'
PORT = 65432
# step 1 Create a server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2 Listen for a connection from a server and accepted
client_socket.connect((HOST, PORT))
# creating an object
pink = Cat('Pink')
# step 3 Pickle the data
pickle_object = pickle.dumps(pink)
client_socket.send(pickle_object)

# step 5 Close the connection
client_socket.close()

