# Disk Scheduling Algorithms - FCFS

class DiskScheduler:
    def __init__(self, head_position):
        self.head = head_position
        self.total_seek_time = 0
    
    def fcfs(self, requests):
        seek_time = 0
        for request in requests:
            seek_time += abs(request - self.head)
            self.head = request
        self.total_seek_time = seek_time
        return seek_time

scheduler = DiskScheduler(50)
requests = [12, 25, 3, 100, 75]
seek_time = scheduler.fcfs(requests)
print(f'Total Seek Time (FCFS): {seek_time} ms')
