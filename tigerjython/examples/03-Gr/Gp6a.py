from gpanel import *
makeGPanel(0, 10, 0, 10)

move(1, 5)
text("Dr�cke irgendeine Taste!")
while True:
   key = getKeyCodeWait()
   print key,

