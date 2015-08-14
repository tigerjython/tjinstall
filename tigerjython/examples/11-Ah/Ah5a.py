import serial
from gconsole import *

makeConsole()
setTitle("Terminal")
ser = serial.Serial(port = "COM1", baudrate = 2400, timeout = 0)
while not isDisposed():
    delay(1)
    ch = getKey()
    if ch != KeyEvent.CHAR_UNDEFINED:  # a key is typed
        ser.write(ch)
    nbChars = ser.inWaiting()    
    if nbChars > 0:
        text = ser.read(nbChars)
        for ch in text:
            if ch == '\n':
                gprintln()
            else:    
                gprint(ch)
 
