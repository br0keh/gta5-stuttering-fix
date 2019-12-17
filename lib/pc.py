
import multiprocessing 
from psutil import virtual_memory
import GPUtil
import math

class PC:
    def __init__(self):
        mem = virtual_memory()
        gpu = GPUtil.getGPUs()[0]
        self.vram = float(gpu.memoryTotal / 1024)
        self.ram =  float(self.convert_size(mem.total))
        self.cores = multiprocessing.cpu_count()

    def convert_size(self, size_bytes): 
        if size_bytes == 0: 
            return "0" 
        i = int(math.floor(math.log(size_bytes, 1024)))
        power = math.pow(1024, i) 
        size = round(size_bytes / power, 2) 
        return size

    def get_vram(self):
        return self.vram
    def get_ram(self):
        return self.ram
    def get_cores(self):
        return self.cores
    
    def get_score(self):
        score = 0

        # cpu  max: 40
        if self.get_cores() > 8: # octacore or better
            score = score + 45
        elif self.get_cores() > 4: # quad core
            score = score + 30
        elif self.get_cores() == 2: # dual core
            score = score + 20
        else:                       # crappy pcs
            score = score + 5
        

        # ram  max:  30
        if self.get_ram() > 8: 
            score = score + 30
        elif self.get_ram() >= 4: 
            score = score + 25
        elif self.get_ram() < 4 and self.get_ram() > 2: 
            score = score + 20
        elif self.get_ram() <= 2: 
            score = score + 5
            
        
        # vram  max 30
        if self.get_vram() > 8.0:
            score = score + 30
        elif self.get_vram() >= 2.0:
            score = score + 20
        elif self.get_vram() == 1.0:
            score = score + 10
        elif self.get_vram() < 1.0 and self.get_vram() > 0.512:
            score = score + 5
        else:
            score = score 

        return score
    
    def can_it_run(self):
        score = self.get_score()
        # 0 - 40
        if score < 40:
            return 'Apparently your computer is too slow to run GTA V stably.'
        # 40 - 60
        elif score < 60:
            return 'Apparently your computer can run GTA V with NORMAL graphics.'
        # 60 - 80
        elif score <= 80:
            return 'Apparently your computer can run GTA V with HIGH graphics.'
        # 80 - 100
        elif score > 80:
            return 'Apparently your computer can run GTA V with VERY HIGH graphics.'
