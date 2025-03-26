import socket
import threading
HEADER =64 
PORT = 5050
SERVER = "192.168.0.101"
FORMAT = "UTF-8"
DISCONNECT="disconnect"
ADDR = (SERVER,PORT)




client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

def send():
    while True:
        message = input("you:")
        if message =="exit":
            client.close()
            break
        client.send(message.encode(FORMAT))

        

def recive_mess():
   while True:

      message = client.recv(HEADER).decode(FORMAT)

      print(f"received:{message}")

thread = threading.Thread(target=recive_mess)
thread.start() 




send()
client.close()


    