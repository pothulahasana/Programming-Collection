# Inter-Process Communication (IPC)
import queue
import threading
import time

# Message Queue for IPC
message_queue = queue.Queue()

def producer():
    for i in range(5):
        message = f'Message {i}'
        message_queue.put(message)
        print(f'Produced: {message}')
        time.sleep(0.5)

def consumer():
    while not message_queue.empty():
        message = message_queue.get()
        print(f'Consumed: {message}')
        time.sleep(1)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
p.join()
c.start()
c.join()
print('IPC completed')
