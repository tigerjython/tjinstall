from random import randint

n = 1000 # number of games
won = 0
repeat n:
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)
    if a == 6 or b == 6 or c == 6:
        won += 1
 
print "Won:", won, " of ", n, " games"
print "My winning percentage:", won / n

