from socket import AF_INET, socket, SOCK_STREAM ,gethostname ,gethostbyname

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = gethostbyname(gethostname())
ADDR = (SERVER,PORT)


client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER -len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Helloooo World")
input()
send("Helloooo Tim")
input()
send("Helloooo Everyone")
input()
send("Helloooo bys")
input()
send("Helloooo World")
send(DISCONNECT_MESSAGE)