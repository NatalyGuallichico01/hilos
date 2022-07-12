import multiprocessing
import time
  
  
class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id
                 
    def run(self):
        time.sleep(0)
        print("I'm the process with id: {}".format(self.id))
  
if __name__ == '__main__':
    p = Process(0)
    p.start()
    p.join()
    p = Process(1)
    p.start()
    p.join()
    p = Process(2)
    p.start()
    p.join()
    p = Process(3)
    p.start()
    p.join()
    p = Process(4)
    p.start()
    p.join()
    p = Process(5)
    p.start()
    p.join()
    p = Process(6)
    p.start()
    p.join()
    p = Process(7)
    p.start()
    p.join()
