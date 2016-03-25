def isPalindrom(a):
    return a == a[::-1]

fInp = open("worte-1$.txt")
fOut = open("palindrom.txt", "w")

print "Searching for palindroms..." 
while True:
    word = fInp.readline()
    if word == "":
        break
    word = word[:-1] # remove trailing \n
    word = word.lower() # make lowercase
    if isPalindrom(word):
        print word
        fOut.write(word + "\n")
fInp.close()        
fOut.close()
print "All done" 
