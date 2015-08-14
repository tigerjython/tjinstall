import time

playTone(440, 5000)
time.sleep(2)
playTone(441, 5000)
time.sleep(2)
playTone(440, 20000, block = False)
playTone(441, 20000)

