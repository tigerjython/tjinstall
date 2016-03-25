from threading import Thread
import time

class WorkerThread(Thread):
     def __init__(self, begin, end):
         Thread.__init__(self)
         self.begin = begin
         self.end = end
         self.total = 0

     def run(self):
         for i in range(self.begin, self.end):
             self.total += i

startTime = time.clock()
repeat 10:
    thread = WorkerThread(0, 1000000)
    thread.start()
    thread.join() 
    print thread.total
print "Time elapsed:", time.clock() - startTime, "s"
