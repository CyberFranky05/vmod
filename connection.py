"""
This file handels the connection of 2 devices at present
in future we will make it auto scan the network and establish connection with all selected ip by user with its configurations 
"""

import socket
import fcntl
import struct

# Linux code to get ip adress by formating python string to 16 byte data for linux kernal
def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except OSError:
        return "Interface not found or disconnected"

def primary_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "0.0.0.0"
    port = 5600

    server_socket(host,port)
    server_socket.listen(1)
    print(f"Listing on port {port}")
    client_socket , client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    data = client_socket.recv(1024).decode('utf-8')
    print(f"Client says: {data}")

    client_socket.send("Hello world")

    client_socket.close()
    server_socket.close()




def client_server(server_ip:str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5600
    pritn(f"Connecting to {server_ip}")
    client_socket.connect(server_ip,port)
    message = "Message from Elbaph"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).encode('utf-8')
    print(f"Message from server {response}")

    client_socket.close()









