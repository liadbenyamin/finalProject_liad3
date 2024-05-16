import socket
import threading


class Network:
    ip = '127.0.0.1'
    port = 5555

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('127.0.0.1', 9999))
        self.server.listen()
        conn1, addr = self.server.accept()
        thread1 = threading.Thread(target=handle_connection, args=(conn1,))
        thread1.start()

        print(f"Connected by {addr}")
        print("waiting for player 2")
        conn2, addr = self.server.accept()
        print(f"Connected by {addr}")

        thread2 = threading.Thread(target=handle_connection, args=(conn2,))
        thread2.start()

    def handle_connection(conn):
        while True:
            data = conn.recv(1024)
            print(data)
                # if not data:
                #     break
                # conn.sendall(data)

net = Network()