# OS Threading and Concurrency
import threading
import time

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        temp = counter
        time.sleep(0.001)
        counter = temp + 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Final counter: {counter}')
