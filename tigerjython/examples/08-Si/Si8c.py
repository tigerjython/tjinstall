from soundsystem import *
from gpanel import *

def toColor(z):
    w = int(450 +  300 * z)
    c = X11Color.wavelengthToColor(w)
    return c

def drawSonogram():
    makeGPanel(0, 190, 0, 1000)
    title("Sonogramm of 'Harris'")
    lineWidth(4)
    # Analyse blocks every 50 samples
    for k in range(191):
        a = fft(samples[k * 50:], n)
        for i in range(n // 2):
            setColor(toColor(a[i]))
            point(k, i)

fs = 20000 # Sampling freq->spectrum 0..10 kHz
n = 2000 #  Size of block for analyser

samples = getWavMono("wav/harris.wav")
openMonoPlayer(samples, fs)
play()
drawSonogram()

