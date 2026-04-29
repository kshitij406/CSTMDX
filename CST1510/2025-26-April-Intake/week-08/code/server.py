from socket import *
from time import ctime

HOST = 'localhost' # or  '127.0. 0.1'
PORT = 5000
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
    current_time = ctime().encode('ascii')
    client.send(current_time)
    client.close()

