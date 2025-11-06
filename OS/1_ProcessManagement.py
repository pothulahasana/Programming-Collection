# OS Process Management
# Demonstrates basic process scheduling concepts
from multiprocessing import Process
import time

def worker(name, delay):
    print(f'Process {name} started')
    time.sleep(delay)
    print(f'Process {name} completed')

if __name__ == '__main__':
    p1 = Process(target=worker, args=('P1', 2))
    p2 = Process(target=worker, args=('P2', 1))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('All processes completed')
