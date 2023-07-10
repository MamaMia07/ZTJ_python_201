# echo-server.py
import socket
import time
import json

class Response():
    def __init__(self, command):
        self.command = command
        self.commands = ["stop", "help", "uptime","info"]

    def stop_resp(self, add):
        print(f"Connection terminated by {add[0]}")
        clnt_conn_socket.send(f"Unconnected".encode('utf-8'))
        
    def help_resp(self):
        pass

    def uptime_resp(self):
        pass

    def version_resp(self):
        pass

    def unknown_cmd_resp(self):
        pass

    def send_response(self):
        pass
        #if self.command not in self.commands: unknown_cmd_resp(self) 
        #if self.command == "help": help_msg()
        


version = '0.1.0'
HOST = "127.0.0.1"  #"156.17.181.78" # "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)
start_server = time.time()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Listening...")
    clnt_conn_socket, address = server.accept()
   
    with clnt_conn_socket:
        print(f"Connected with {address[0]}")
        while True:
            #data_recv = conn_socket.recv(1024)
            data = clnt_conn_socket.recv(1024).decode("utf-8")

            resp = Response(data)

##            if data.decode("utf-8") == "stop":
##                print(f"Connection terminated by {address[0]}")
##                conn_socket.send(f"Unconnected".encode('utf-8'))
            if data == "stop":
                resp.stop_resp(address)
                break

            elif data == "info": #data.decode('utf-8') == "info":
                 clnt_conn_socket.send(f"info: to jest wersja {version}".encode('utf-8'))
          
            elif data == "uptime": #data.decode('utf-8') == "uptime":
                 server_life = time.time() - start_server
                 clnt_conn_socket.send(f"czas życia servera: {server_life:0.4f}s".encode('utf-8'))

            else:   
                clnt_conn_socket.send(f"Got your message! Thank you!\nit was: {data}".encode('utf-8'))
            print(data) #(data.decode('utf-8'))
