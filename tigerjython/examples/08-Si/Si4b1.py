import random

n = 10000
s = 7  # rolled sum of the die numbers

def sim():
    i = 0
    total =  0
    while True:
        i += 1
        r = random.randint(1, 6)
        total += r
        if total >= s:
            break
    return i

sum = 0
repeat n:
    sum += sim()

print "Mean waiting time:", sum / n

