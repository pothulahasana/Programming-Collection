# File System Management
import os
from pathlib import Path

class SimpleFileSystem:
    def __init__(self):
        self.files = {}
        self.directories = set(['/'])
    
    def create_file(self, path, content):
        self.files[path] = content
    
    def read_file(self, path):
        return self.files.get(path)
    
    def delete_file(self, path):
        if path in self.files:
            del self.files[path]

fs = SimpleFileSystem()
fs.create_file('/home/user/file.txt', 'Hello')
print(f'File content: {fs.read_file("/home/user/file.txt")}')
