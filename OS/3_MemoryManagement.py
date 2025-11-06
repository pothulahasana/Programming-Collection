# Memory Management
import sys

# Virtual memory simulation
class MemoryManager:
    def __init__(self, size):
        self.memory = [None] * size
        self.page_table = {}
    
    def allocate(self, address, size, data):
        self.memory[address:address+size] = [data]*size
        self.page_table[address] = size
    
    def deallocate(self, address):
        if address in self.page_table:
            size = self.page_table[address]
            self.memory[address:address+size] = [None]*size
            del self.page_table[address]

mm = MemoryManager(1024)
mm.allocate(0, 10, 'data')
print(f'Memory usage: {len([x for x in mm.memory if x is not None])} bytes')
