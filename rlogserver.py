# created by Tonyk7
import logging
import socket

# change these to match your source (client) IP address and the port in RemoteLog.h
rlog_ip_address = 'replace with ip'
rlog_port = 11909

# code is from: https://gist.github.com/majek/1763628
def udp_server(host=rlog_ip_address, port=rlog_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print("Initiated server on " + host + ":" + str(port))

    while True:
        (data, addr) = s.recvfrom(128*1024)
        yield data

for data in udp_server():
    print(data.decode())
