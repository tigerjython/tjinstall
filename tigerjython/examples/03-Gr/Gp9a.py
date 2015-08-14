bioGrades = []
bioGrades.append(5.5)
print bioGrades
bioGrades.append(5)
print bioGrades
bioGrades.append(5.5)
print bioGrades
bioGrades.append(6)
print bioGrades
sum = 0
for note in bioGrades:
    sum += note
print "Average: " + str(sum / len(bioGrades))

