# from threading import Thread 
import threading
import time 


def display():
    print("t1 thread details: ", threading.current_thread().ident)
    for i in range(4):
        time.sleep(0.2)
        print("Hello world!", i)

t1 = threading.Thread(target = display)

t1.start()