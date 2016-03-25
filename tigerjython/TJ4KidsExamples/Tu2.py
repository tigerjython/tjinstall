from gturtle import *

makeTurtle()

#Kerze
setLineWidth(60)
setPenColor("red")
forward(100) 
#Flamme
penUp()
forward(50)
penDown()
setPenColor("yellow")
dot(40)
#Docht
setLineWidth(5)
setPenColor("black")
back(15) 
hideTurtle() #Turtle verstecken
