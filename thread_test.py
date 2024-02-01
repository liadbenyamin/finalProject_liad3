import threading
import time


def loop(name):
    for i in range(10):
        print(i, name)
        time.sleep(1)


thread1 = threading.Thread(target=loop, args=("liad",))
thread2 = threading.Thread(target=loop, args=("jeremy",))
thread1.start()
thread2.start()