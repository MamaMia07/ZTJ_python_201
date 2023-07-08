# echo-server.py
import socket
import time

class Message():
    def __init__(self, command):
        self.command = command

    def help_msg(self):
        pass
    def
        
        
    def send_message(self):
        if self.command == "help": help_msg()
        


version = '0.1.0'
HOST = "127.0.0.1"  #"156.17.181.78" # "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)
start_server = time.time()

message = message()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn_socket, address = server.accept()
    with conn_socket:
        print(f"Connected with {address[0]}")
        while True:
            data_recv = conn_socket.recv(1024)
            data = data_recv.decode('utf-8)

            if data.decode('utf-8') == "stop":
                print(f"Connection terminated by {address[0]}")
                conn_socket.send(f"Unconnected".encode('utf-8'))
                break

            elif data.decode('utf-8') == "info":
                 conn_socket.send(f"info: to jest wersja {version}".encode('utf-8'))
          
            elif data.decode('utf-8') == "uptime":
                 server_life = time.time() - start_server
                 conn_socket.send(f"czas życia servera: {server_life:0.4f}s".encode('utf-8'))

            else:   
                conn_socket.send(f"Got your message! Thank you!\nit was: {data.decode('utf-8')}".encode('utf-8'))
            print(data.decode('utf-8'))
