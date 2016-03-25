import random

n = 1000 # number experiment

def pair():
    # Select two distinct inhabitants
    a = random.randint(0, 99)
    b = a
    while b == a:
        b = random.randint(0, 99)
    z[a] = z[a] or z[b]
    z[b] = z[a]

def nbInfected():
    sum = 0
    for i in range(100):
        if z[i]:
            sum += 1
    return sum

def sim():
    global z
    z = [False] * 100
    t = 0
    a = random.randint(0, 99) 
    z[a] = True # random infected inhabitant
    while True:
        pair()
        t += 1
        if nbInfected() == 100:
            return t

sum = 0
for i in range(n):
    u = sim()
    print "Experiment #", i + 1, "Waiting time:", u
    sum += u
    
print "Mean waiting time:", sum / n

