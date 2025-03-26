
import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER,PORT)
FORMAT="utf-8"
DISCONNECT = "disconnect"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clients=[]

server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[new connection]{addr}connected")

    clients.append(conn)
    print(f"connected client:{clients}")

    while True:

         message = conn.recv(HEADER).decode()
         print(f"{addr} {message}")

         if message == DISCONNECT:
             clients.remove(conn)
             conn.close()
             break
         

         broadcast(message,conn)
    conn.close()    


             
    
    


       


def broadcast(message,send_conn):

    print(f"broadcasting {message}")


    for client in clients:
        if client!=send_conn:
            print(f"sending to:{client}")
            client.send(message.encode(FORMAT))






                    
def start():
    server.listen()
    while True:
       conn,addr =  server.accept()
       thread = threading.Thread(target=handle_client,args=(conn,addr))
       thread.start()
       print(f"[active connections]{threading.activeCount()-1}")
       


print("server is starting")
start()

   