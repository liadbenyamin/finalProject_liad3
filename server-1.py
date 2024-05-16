import socket
import sys
import threading
import json

HOST = ''  # all available interfaces
PORT = 9999  # arbitrary non privileged port
colors_names = ["red", "green", "blue"]
# data = ""
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

def client_thread(conn, port):
    global connections
    # conn.send(str(len(connections)).encode())
    while True:
        data = conn.recv(1024)
        obj = json.loads(data.decode())
        if obj['type'] == 'kill':
            for c in connections:
                if c != conn:
                    c.send(json.dumps({"type": "killed"}).encode())
                    c.close()
                    connections = [conn]
                else:
                    c.send(json.dumps({"type": "win"}).encode())
                    c.close()
        print(f"received from {port}: {data}")
        if not data:
            break
        for c in connections:
            if c != conn:
                c.send(data)
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
            con.send(obj.encode())


s.close()
