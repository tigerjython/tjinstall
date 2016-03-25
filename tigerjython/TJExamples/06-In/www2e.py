from soundsystem import *

initTTS()
selectVoice("german-man")
sound = generateVoice(html)
openSoundPlayer(sound)
play() 
