import socket
import sys
import threading

HOST = '' # all availabe interfaces
PORT = 9999 # arbitrary non privileged port
colors_names = ["red", "green", "blue"]
data = ""
# list of all connections (socket)
connections = []
# create server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Socket Created")

s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))

s.listen(5)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    conn.send(str(len(connections)).encode())
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break

        for i in range(len(connections)):
            reply = (colors_names[connections.index(conn)] + " " + data.decode()).encode()
            connections[i].sendall(reply)
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    connections.append(conn)
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    thread = threading.Thread(target=client_thread, args = (conn,))
    thread.start()

s.close()