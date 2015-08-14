import random

sum = 0
z = 100000
repeat z:
    n = random.randint(0, 15)
    if n != 15:
        q = n + 1 # number of questions
    else:
       q = 15
    sum += q   
print "Mean:", sum / z
