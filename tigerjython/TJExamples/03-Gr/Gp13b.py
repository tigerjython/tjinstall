from gpanel import *
from javax.swing import JMenu, JMenuBar, JMenuItem

def actionCallback(e):
   if e.getSource() == goItem:
      wakeUp()
   if e.getSource() == exitItem:
      dispose()
   if e.getSource() == aboutItem:
      msgDlg("Pyramides Version 1.0")

def doIt():
   clear()
   for i in range(1, 30):
      setColor(getRandomX11Color())
      fillRectangle(i/2, i - 0.35, 30 - i/2, i + 0.35)

fileMenu = JMenu("File")
goItem = JMenuItem("Go", actionPerformed = actionCallback)
exitItem = JMenuItem("Exit", actionPerformed = actionCallback)
fileMenu.add(goItem)
fileMenu.add(exitItem)

aboutItem = JMenuItem("About", actionPerformed = actionCallback)

menuBar = JMenuBar()
menuBar.add(fileMenu)
menuBar.add(aboutItem)

makeGPanel(menuBar, 0, 30, 0, 30)

while not isDisposed():
   putSleep()
   if not isDisposed():
      doIt()

