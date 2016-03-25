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

fs = 40000 # Sampling frequency
n = 10000 # Number of samples
samples = getWavMono("wav/doublesine.wav")
openMonoPlayer(samples, fs)
play()
a = fft(samples, n)
showSpectrum("Audio Spectrum")

