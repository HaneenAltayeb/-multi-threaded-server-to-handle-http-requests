import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
MESSAGE = raw_input("type http:// 10.50.89.240/index.html to continue/ Enter exit:")

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((host, port))

while MESSAGE != 'exit':
    Client.send(MESSAGE)
    data = Client.recv(BUFFER_SIZE)
    print " Client received data...", data
    MESSAGE = raw_input(" Thanks")

Client.close()