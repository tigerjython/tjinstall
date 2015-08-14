from dbapi import *
from gamegrid import *

table = "res_20140115"
username = "admin"
password = "solar"
dbname = "casino"
serverURL = "localhost"
#serverURL = "10.1.1.123"

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

def pressCallback(e):
    if not isReady:
        return
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

class MyButton(GGButton, GGButtonListener):
    def __init__(self, imagePath):
        GGButton.__init__(self, imagePath)
        self.addButtonListener(self)
        
    def buttonClicked(self, button):
        if not isReady:
            return
        if button == confirmBtn:
            confirm()
        if button == renewBtn:
            renew()

def renew():
    global isReady
    try:    
        SQL = "SELECT * FROM " + table
        cursor.execute(SQL)
        con.commit()
    except:
        setStatusText("Fatal error. Restart and try again.")
        isReady = False
        return
   
    result = cursor.fetchall()
    for record in result:
        seatNb = record[0]
        isBooked = (record[1] != 'N')
        if isBooked:
            seats[seatNb - 1].show(2)
        else:
            seats[seatNb - 1].show(0)
    refresh()
    setStatusText("View refreshed")

def confirm():
    global isReady
    try:
        # check if seats is still available
        for seatNb in range(1, 31):
           if seats[seatNb - 1].getIdVisible() == 1:
               SQL = "SELECT * FROM "  + table + "  WHERE seat=" + str(seatNb)
               cursor.execute(SQL)
               result = cursor.fetchall()
               for record in result:
                   if record[1] == 'Y':
                        setStatusText("One of the seats are already taken.")
                        return
        isReserved = False                    
        for seatNb in range(1, 31):
           if seats[seatNb - 1].getIdVisible() == 1:
               SQL = "UPDATE "  + table + " SET booked='Y' WHERE seat=" + \
                     str(seatNb)
               cursor.execute(SQL)
               isReserved = True
           con.commit()
        renew()
        if isReserved:
            setStatusText("Reservation successful")
        else:
            setStatusText("Nothing to do")
    except Exception, e:
        setStatusText("Fatal error. Restart and try again.")
        isReady = False
        
isReady = False
makeGameGrid(8, 8, 40, None, "sprites/stage.gif", False, 
             mousePressed = pressCallback)
addStatusBar(30)
setTitle("Seat Reservation - Loading...")
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

con = getDerbyConnection(serverURL, dbname, username, password)
if con == None:
    setStatusText("Fatal error. Connection to database failed")
else:    
    cursor = con.cursor()
    renew()

    setTitle("Seat Reservation - Ready")
    setStatusText("Select free seats and press 'Confirm'")
    isReady = True
    while not isDisposed():
        delay(100)
    cursor.close()
    con.close()
