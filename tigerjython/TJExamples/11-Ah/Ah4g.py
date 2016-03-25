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
    thread1 = WorkerThread(0, 500000)
    thread2 = WorkerThread(500000, 1000000)
    thread1.start()
    thread2.start()
    thread1.join() 
    thread2.join()  
    result = thread1.total + thread2.total
    print result 
print "Time elapsed:", time.clock() - startTime, "s"
