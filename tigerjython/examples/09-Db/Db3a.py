from gamegrid import *

def toLoc(seat):
    i = ((seat - 1) % 6) + 1
    k = ((seat - 1) // 6) + 2
    return Location(i, k)

def toSeatNb(loc):
    if loc.x < 1 or loc.x > 6 or loc.y < 2 or loc.y > 6:
       return None
    i = loc.x - 1
    k = loc.y - 2
    seatNb = k * 6 + i + 1
    return seatNb

class MyButton(GGButton, GGButtonListener):
    def __init__(self, imagePath):
        GGButton.__init__(self, imagePath)
        self.addButtonListener(self)
        
    def buttonClicked(self, button):
        if button == confirmBtn:
            confirm()
        if button == renewBtn:
            renew()

def renew():
    setStatusText("View refreshed")

def confirm():
    for seatNb in range(1, 31):
       if seats[seatNb - 1].getIdVisible() ==  1:
           seats[seatNb - 1].show(2)
           refresh()
    setStatusText("Reservation successful")

def pressCallback(e):
    loc = toLocation(e.getX(), e.getY())
    seatNb = toSeatNb(loc)
    if seatNb == None:
        return
    seatActor = seats[seatNb - 1]
    if seatActor.getIdVisible() == 0:  # free
        seatActor.show(1) # option
        refresh()
    elif seatActor.getIdVisible() == 1:  # option
       seatActor.show(0) # free
       refresh()


makeGameGrid(8, 8, 40, None, "sprites/stage.gif", False, 
             mousePressed = pressCallback)
addStatusBar(30)
setTitle("Seat Reservation")
setStatusText("Please select free seats and press 'Confirm'")
confirmBtn = MyButton("sprites/btn_confirm.gif")
renewBtn = MyButton("sprites/btn_renew.gif")
addActor(confirmBtn, Location(1, 7))
addActor(renewBtn, Location(6, 7))
seats = []
for seatNb in range(1, 31):
    seatLoc = toLoc(seatNb)
    seatActor = Actor("sprites/seat.gif", 3)
    seats.append(seatActor)
    addActor(seatActor, seatLoc)
    addActor(TextActor(str(seatNb)), seatLoc)
show()
