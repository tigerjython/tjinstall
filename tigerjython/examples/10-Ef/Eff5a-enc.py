import string
key = 4
alphabet = string.ascii_uppercase + " "

def encode(text):
    enc = ""
    for ch in text:
        if ch != "\n":
            i = alphabet.index(ch)               
            ch = alphabet[(i + key) % 27]
        enc += ch
    return enc
    
fInp = open("original.txt")
text = fInp.read()
fInp.close() 

print "Original:\n", text
krypto = encode(text)
print "Krypto:\n", krypto

fOut = open("secret.txt", "w")    
for ch in krypto:
    fOut.write(ch)
fOut.close()      

