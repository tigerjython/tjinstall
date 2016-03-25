from threading import Thread
import random, time
from gturtle import *

class TurtleAnimator(Thread):
    def __init__(self, turtle):
        Thread.__init__(self)
        self.t = turtle

    def run(self):
        while True:
            if isPaused:
                Turtle.sleep(10)
            else: 
                self.t.forward(100 * random.random())
                self.t.left(-180 + 360 * random.random())

tf = TurtleFrame()
john = Turtle(tf)
laura = Turtle(tf)
laura.setColor("red")
laura.setPenColor("red")
laura.setPos(-200, 0)
laura.rightCircle(200)
laura.setPos(0, 0)
thread1 = TurtleAnimator(john)
thread2 = TurtleAnimator(laura)
isPaused = False
thread1.start() 
thread2.start()

tf.setTitle("Running")
while not isPaused and not tf.isDisposed():
    if laura.distance(0, 0) > 200 or john.distance(0, 0) > 200:
        isPaused = True
        tf.setTitle("Paused")
        Turtle.sleep(2000)
        laura.home()
        john.home()
        isPaused = False
        tf.setTitle("Running")
    time.sleep(0.001)
