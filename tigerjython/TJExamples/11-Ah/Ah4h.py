# Ah4h.py

from gpanel import *
from threading import Thread, Lock
import random

class MyThread(Thread):
    def run(self):
        while not isDisposed():
            if getKeyCode() == 32:
                print "----------- Lock requested by MyThread"
                lock.acquire()
                print "----------- Lock acquired by MyThread"
                move(random.randint(2, 8), random.randint(2, 8))
                delay(500)  # for demonstration purposes
                print "----------- Lock releasing by MyThread..."
                lock.release()
            else:
                delay(1)

def square():
    print "Lock requested by main"
    lock.acquire()
    print "Lock acquired by main"
    setColor("red")
    fillRectangle(2, 2)
    delay(1000)
    setColor("white")
    fillRectangle(2, 2) 
    delay(1000)
    print "Lock releasing by main..."
    lock.release()

lock = Lock()
makeGPanel(0, 10, 0, 10)

t = MyThread()
t.start()
move(5, 5)
while not isDisposed():
    square()
    delay(1) # Give up thread for a short while
