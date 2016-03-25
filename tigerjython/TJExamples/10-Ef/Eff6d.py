# Eff6d.py

from javax.swing import JButton
from gturtle import *

def buttonCallback(evt):
    global state
    source = evt.getSource()
    if source == runBtn:
        state = State.RUNNING
        setTitle("State: RUNNING")
    if source == stopBtn:
        state = State.STOPPED
        setTitle("State: STOPPED")
    if source == quitBtn:
        state = State.QUITTING
        setTitle("State: QUITTING")

State = enum("STOPPED", "RUNNING", "QUITTING")
state = State.STOPPED

runBtn = JButton("Run", actionPerformed = buttonCallback)
stopBtn = JButton("Stop", actionPerformed = buttonCallback)
quitBtn = JButton("Quit", actionPerformed = buttonCallback)
makeTurtle()
setTitle("State: STOPPED")
back(100)

pg = getPlayground()
pg.add(runBtn)
pg.add(stopBtn)
pg.add(quitBtn)
pg.validate()

while state != State.QUITTING and not isDisposed():
    if state == State.RUNNING:
          forward(200).left(127)
dispose()         
