import random

n = 10000

def sim():
    z = []
    i = 0
    while True:
        r = random.randint(1, 6)
        i += 1
        if not r in z:
            z.append(r)
        if len(z) == 6:
            return i

sum = 0
repeat n:
    sum += sim()

print "Mean waiting time:", sum / n

