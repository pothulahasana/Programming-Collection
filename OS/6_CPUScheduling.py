# CPU Scheduling Algorithms

class Process:
    def __init__(self, pid, burst_time, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time

def fcfs_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    for p in processes:
        current_time = max(current_time, p.arrival_time)
        completion_time = current_time + p.burst_time
        print(f'Process {p.pid}: {current_time}-{completion_time}')
        current_time = completion_time

procs = [Process(1, 5), Process(2, 3), Process(3, 8)]
fcfs_scheduling(procs)
