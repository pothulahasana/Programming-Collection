# Page Replacement Algorithms - FIFO

class PageReplacer:
    def __init__(self, frame_count):
        self.frames = []
        self.frame_count = frame_count
        self.page_faults = 0
    
    def reference_page(self, page):
        if page not in self.frames:
            self.page_faults += 1
            if len(self.frames) < self.frame_count:
                self.frames.append(page)
            else:
                self.frames.pop(0)  # FIFO
                self.frames.append(page)
    
    def display(self):
        print(f'Frames: {self.frames}, Page Faults: {self.page_faults}')

replacer = PageReplacer(3)
for page in [1, 2, 3, 4, 2, 1, 5]:
    replacer.reference_page(page)
replacer.display()
