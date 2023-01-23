from socket import AF_INET, socket, SOCK_STREAM ,gethostname ,gethostbyname
from threading import Thread ,activeCount

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
SERVER = gethostbyname(gethostname())
ADDR = (SERVER,PORT) #This will strore the server ip and port
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket(AF_INET , SOCK_STREAM) #SOCK_STREAM is there to read continous data from the server
server.bind(ADDR) #we are bound this socket to this address anything that connect to this address will no hit this socket


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True 
    while connected:
        #This is also a blocker we will not go forward until we recieve the message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg Recieved".encode(FORMAT))
    conn.close()

def start():
    server.listen() #This is going to listen the server request
    print(f"[LISTENING] Server is listening to {SERVER} ")
    while True:
        conn,addr = server.accept() #conn = This is the object which will allow us to connect back to the server
        #This is a blocking code we will not go forward until we are connected to any socket
        thread = Thread(target=handle_client,args=(conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {activeCount()- 1}")
print("[STARTING] The server is starting ...")
start()