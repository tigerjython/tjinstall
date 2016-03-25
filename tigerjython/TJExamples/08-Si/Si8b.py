from soundsystem import *
from gpanel import *

def showSpectrum(text):
    makeGPanel(-2000, 22000, -0.2, 1.2)
    drawGrid(0, 20000, 0, 1.0, 10, 5, "blue")
    title(text)
    lineWidth(2)
    r = fs / n # Resolution
    f = 0
    for i in range(n // 2): 
        line(f, 0, f, a[i])
        f += r  

n = 10000
fs = 40000 # Sampling frequency
f = 1000 # Signal frequency

samples = [0] * 120000  # sampled data for 3 s
t = 0
dt = 1 / fs # sampling period
for i in range(120000):
   samples[i] = square(1000, f, t)
   t += dt

openMonoPlayer(samples, 40000)
play()
a = fft(samples, n)
showSpectrum("Spectrum Square Wave")

