from gpanel import *

# K5 glass
B = 1.5220
C = 4590  # nanometer^2
# Cauchy equation for refracting index
def n(wavelength):
    return B + C / (wavelength * wavelength)

makeGPanel(-1, 1, -1, 1)
title("Refracting at the K5 glass")
bgColor("black")
setColor("white")
line(-1, 0, 1, 0)


lineWidth(4)
line(-1, 1, 0, 0)
lineWidth(1)

sineAlpha = 0.707

for i in range(51):
     wavelength = 380 + 8 * i
     setColor(X11Color.wavelengthToColor(wavelength))
     sineBeta = sineAlpha / n(wavelength)
     x = (sineBeta - 0.45) * 100 - 0.5  # magnification
     line(0, 0, x, -1)

