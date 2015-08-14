file = open("chplz.txt")
plzStr = file.read()
file.close()

pairs = plzStr.split("\n")
print str(len(pairs)) + " pairs loaded"
plz = {}

for pair in pairs:
   element = pair.split(":")
   plz[element[0]] = element[1]

while True:
   town = input("City?")
   if town in plz:
      print "The postal code of " + town + " is " + str(plz[town])
   else:
      print "The city " + town + " was not found."
