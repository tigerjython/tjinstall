def isPalindrom(a):
    return a == a[::-1]

f = open("worte-1$.txt")

print "Searching for palindroms..." 
for word in f:
    word = word[:-1] # remove trailing \n
    word = word.lower() # make lowercase
    if isPalindrom(word):
        print word
f.close()
print "All done" 
