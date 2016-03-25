from gpanel import *
import math

def doIt():
    clear()
    drawGrid(0, 200, -100, 100, "seagreen")
    m = mass.getValue() / 1000 # Mass (kg)
    k = spring.getValue() / 1000 # Spring const (N/kg)
    t = 0; y = 50; v = 0 # Initial conditions
    r = 0.7       # Coefficient of friction (N/m/s)
    d = 200; dt = 0.01
    status.setValue("m = %6.2f kg, k = %6.2f N/kg" % (m, k))
    move(t, y)  # Initial cursor position
    while t < d:
        draw(t, y)      # Draw segment
        F = -k*y - r*v  # Force
        a = F/m         # Acceleration
        v = v + a*dt    # New velocity
        y = y + v*dt    # New position
        t = t + dt      # New time
    T = 2 * math.pi * math.sqrt(m / k)
    status.setValue("Done")

mass = SliderEntry(0, 10000, 10000, 1000, 500)
pane1 = EntryPane("Mass (g)", mass)
spring = SliderEntry(0, 1000, 500, 100, 50)
pane2 = EntryPane("Spring constant (mN/kg)", spring)
goBtn = ButtonEntry("Go")
pane3 = EntryPane(goBtn)
status = StringEntry("")
pane4 = EntryPane("Status", status)
dlg = EntryDialog(850, 150, 
        pane1, pane2, pane3, pane4)

makeGPanel()
window(-20, 220, -110, 110)
drawGrid(0, 200, -100, 100, "seagreen")
title("Harmonic Oscillation")
status.setValue("Press Go to start")
while not dlg.isDisposed():
    if isDisposed():
        dlg.dispose()
        break
    if goBtn.isTouched():
        doIt()
dispose()

