import socket
import json

HOST = "127.0.0.1"  # "156.17.181.78" # "127.0.0.1"  # The server's hostname or IP address
PORT = 9090  # The port used by the server

connect = True
#while connect:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clnt_socket:
    clnt_socket.connect((HOST, PORT))
    while connect:
        request = input("> ")
        #clnt_socket.send("Hello, world!! It's ME!!!".encode("utf-8"))
        clnt_socket.send(request.encode("utf-8"))
        data = ""
##        while True:
##            rec = clnt_socket.recv(1024)
##            if len(rec)<=0:
##                break
##            data += rec.decode("utf-8")
        data = clnt_socket.recv(1024)
        if request =="stop": connect = False
        #print("Received data: ")
        print(data.decode('utf-8'))
            

