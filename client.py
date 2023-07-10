import socket
import json

HOST = "127.0.0.1"  # "156.17.181.78" # "127.0.0.1"  # The server's hostname or IP address
PORT = 9090  # The port used by the server
size = 8
connected = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clnt_socket:
    clnt_socket.connect((HOST, PORT))
    while connected: #True: #
        
        request = input("> ")
        clnt_socket.send(request.encode("utf-8"))
        
        data = ""
        while True:
            rec = clnt_socket.recv(size)
            
            data += rec.decode("utf-8")
##            print(data)
##            print(len(rec))
            if len(rec) < size: break 
                

                
        if request == "stop": connected = False #break #


        #data = clnt_socket.recv(1024).decode('utf-8')
        #print(data)
        #if request =="stop": connect = False
        print("Received data: ")
        print(data) #.decode('utf-8'))
            

