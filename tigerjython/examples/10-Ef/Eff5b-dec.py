import string
key = "ALICE"
alphabet = string.ascii_uppercase + " " 

def decode(text):
    keyList = []
    for ch in key:
        i = alphabet.index(ch)
        keyList.append(i)
    print "keyList:", keyList
    enc = ""
    for n in range(len(text)):
        ch = text[n]
        if ch != "\n":
            i = alphabet.index(ch)  
            k = n % len(key)                
            ch = alphabet[(i - keyList[k]) % 27]      
        enc += ch
    return enc

fInp = open("secret.txt")
krypto = fInp.read()
fInp.close() 

print "Krypto:\n", krypto
msg = decode(krypto)
print "Message:\n", msg

fOut = open("message.txt", "w")    
for ch in msg:
    fOut.write(ch)
fOut.close()      

