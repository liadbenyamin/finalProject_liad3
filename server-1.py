import os
import random
import socket
import sys
import threading
import json
from time import sleep

HOST = ''  # all available interfaces
PORT = 9999  # arbitrary non privileged port
# data = ""
# list of all connections (socket)
connections = []
# create server socket over TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[-] Socket Created")

s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))

s.listen(5)
print("Listening...")


# The code below is what you're looking for ############

def client_thread(conn, port):
    global connections

    while len(connections) > 0:
        data = conn.recv(1024)
        obj = json.loads(data.decode())
        print(f"received from {port}: {data}")

        if obj['type'] == 'reset':
            s.close()
            os.system("python server-1.py")
            for con in connections:
                con.shutdown(socket.SHUT_RDWR)
                con.close()
            connections = []

        else:
            if not data:
                break
            for c in connections:
                if c != conn:
                    c.sendall(data)

        # for i in range(len(connections)):
        #     reply = (colors_names[connections.index(conn)] + " " + data.decode()).encode()
        #     connections[i].sendall(reply)
    conn.close()


while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    connections.append(conn)
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    thread = threading.Thread(target=client_thread, args=(conn, addr[1]))
    thread.start()

    if len(connections) >= 2:
        for con in connections:
            obj = json.dumps({"type": "spawn_sprites"})
            con.sendall(obj.encode())
            # con.sendall([])

        sleep(0.5)
        imposter_index = random.randint(0, 1)
        connections[imposter_index].sendall(json.dumps({"type": "role", "role": "imposter"}).encode())
        connections[1 - imposter_index].sendall(json.dumps({"type": "role", "role": "runner"}).encode())

s.close()
