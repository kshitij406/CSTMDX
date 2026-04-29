from socket import *
from codecs import decode

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024

ADDRESS = (HOST, PORT)
# 1 socket
s = socket(AF_INET, SOCK_STREAM)
# 2 connect
s.connect(ADDRESS)
# 3. receive
print(s.recv(BUFSIZE).decode())
while True:
    message = input(' > ')
    if not message:
        break
    s.send(message.encode())
    reply = s.recv(BUFSIZE).decode()
    if not reply:
        print('Server disconnected')
        break
    print(reply)
s.close()



