from socket import *

HOST = 'localhost' # or  '127.0. 0.1'
PORT = 5000
BUFSIZE = 1024

ADDRESS = (HOST, PORT)
# 1 socket
s = socket(AF_INET, SOCK_STREAM)
# 2 bind
s.bind(ADDRESS)
# 3 listen
s.listen(5)

while True:
    print('Waiting for connection ...')
    # 4. accept
    (client, address) = s.accept()
    print(f'... connection from : {address}')
    client.send(f'Hello {client} Im  server'.encode())

    while True:
        message = client.recv(BUFSIZE)
        message = message.decode()
        if not message:
            print('Client disconnected')
            client.close()
            break
        else:
            print(message)
            new_message = input('> ').encode()
            client.send(new_message)

