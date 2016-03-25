from threading import Thread
import random, time
from gturtle import *

class TurtleAnimator(Thread):
    def __init__(self, turtle):
        Thread.__init__(self)
        self.t = turtle

    def run(self):
        while isRunning:
            self.t.forward(50 * random.random())
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
isRunning = True
thread1.start() 
thread2.start()

while isRunning and not tf.isDisposed():
    if laura.distance(0, 0) > 200 or john.distance(0, 0) > 200:
        isRunning = False
    time.sleep(0.001)
tf.setTitle("Limit exceeded")
