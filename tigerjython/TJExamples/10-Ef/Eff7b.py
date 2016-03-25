import math

f = open("letterfreq_de$.txt")
s = "{"
for line in f:
    line = line[:-1] # remove trailing \n
    s += line + ", "
f.close()
s = s[:-2]  # remove trailing ,
s += "}"
occurance = eval(s)

while True:
    word = inputString("Enter a word")
    I = 0
    for letter in word.upper():
        p = occurance[letter] / 100
        I -= math.log(p, 2)
    print word, "-> I =", round(I, 2), "bit"   

