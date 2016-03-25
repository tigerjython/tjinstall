possible = 0
favorable = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            possible += 1
            if i == 6 or j == 6 or k == 6:
                favorable += 1
print "favorable:", favorable, "possible:", possible
print "My winning percentage:", favorable / possible
