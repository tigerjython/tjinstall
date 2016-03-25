def toUmlaut(c):
    if c == "A":
        return "Ä"
    if c == "O":
        return "Ö"
    if c == "U":
        return "Ü"
    if c == "a":
        return "ä"
    if c == "o":
        return "ö"
    if c == "u":
        return "ü"

def convert(infile, outfile):
    inFile = open(infile, "r")
    outFile = open(outfile, "w")
    for line in inFile:
        # Cut at trailing /
        index = line.find("/")
        if index != -1:  # found
            line = line[0:index + 1]
        # Insert umlaute
        line1 = ""
        i = 0
        while i < len(line) - 1: # don't include trailing \n
            pair = line[i : i + 2]
            if pair[1] == "\"":  # indicates Umlaut
                line1 = line1 + toUmlaut(pair[0])
                i += 1 
            elif pair == "sS":  # indicates sz
                line1 = line1 + "ss"
                i += 1
            elif  pair == "qq":
                i += 2 # skip "qq"
            else:
                line1 = line1 + pair[0]
            i += 1
        outFile.write(line1 + "\n") 
    inFile.close()
    outFile.close()

convert("dictionary/verben.txt", "dictionary/verben-1.txt")
print "All done"
