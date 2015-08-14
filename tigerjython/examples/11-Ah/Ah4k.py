from threading import Thread, Lock
from time import sleep

def run1():
    global a, b
    print "----------- lock_a requested by thread1"
    lock_a.acquire()
    print "----------- lock_a acquired by thread1"
    a += 5
#    sleep(1)
    print "----------- lock_b requested by thread1"
    lock_b.acquire()
    print "----------- lock_b acquired by thread1"
    b += 7
    print "----------- lock_a releasing by thread1"
    lock_a.release()
    print "----------- lock_b releasing by thread1"
    lock_b.release()

def run2():
    global a, b
    print "lock_b requested by thread2"
    lock_b.acquire()
    print "lock_b acquired by thread2"
    b *= 3
#    sleep(1)
    print "lock_a requested by thread2"
    lock_a.acquire()
    print "lock_a acquired by thread2"
    a *= 2
    print "lock_b releasing by thread2"
    lock_b.release()
    print "lock_a releasing by thread2"
    lock_a.release()

a = 100
b = 200
lock_a = Lock()
lock_b = Lock()

thread1 = Thread(target = run1)
thread1.start()
thread2 = Thread(target = run2)
thread2.start()
thread1.join()
thread2.join()
print "Result: a =", a, ", b =", b
