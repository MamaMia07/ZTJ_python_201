import socket
import time
import json

class Response():
    def __init__(self): 
        self.helping = {"stop": " : disconnect",
                        "info": " : server software version",
                        "uptime": " : server uptime",
                        "help": " : menu help"}

    def get_command(self, cmd):
        self.command = cmd
        return self.command

    def send_response(self):
        server_life = time.time() - start_server
        responses = {"info": {"server v.:": version},
                     "uptime": {"server uptime:": f"{server_life:.4f}s"},
                     "stop" : {"connection status:": "terminated"},
                     "help": self.helping}
        if self.command in responses:
            data = responses[self.command]
            response = json.dumps(data, indent = 4)
        else:
            data = {"Unknown command.\nType 'help' for command list.":""}
            response = json.dumps(data, indent = 4)
        clnt_conn_socket.sendall(response.encode("utf-8"))




version = '0.1.0'
HOST = "127.0.0.1"  
PORT = 9090  
start_server = time.time()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Listening...")
    clnt_conn_socket, address = server.accept()
    resp = Response()
    with clnt_conn_socket:
        print(f"Connected with {address[0]}")
        while True:
            data = clnt_conn_socket.recv(1024).decode("utf-8")
            resp.get_command(data)
            resp.send_response()
            if data == "stop":
                print("Connection terminated")
                break
