dict = {"blau":"blue", "rot":"red", "grün":"green", "gelb":"yellow"}

print "All entries:"
for key in dict:
   print key + " -> " + dict[key]

while True:
   farbe = input("Color (deutsch)?")
   if farbe in dict:
      print farbe + " -> " + dict[farbe]
   else:
      print farbe + " -> " + "(not translatable)" 
   
