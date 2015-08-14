from soundsystem import *
from entrydialog import *

speaker1 = RadioEntry("Frau (Deutsch)")
speaker1.setValue(True)
speaker2 = RadioEntry("Mann (Deutsch)")
speaker3 = RadioEntry("Man (English)")
pane1 = EntryPane("Speaker Selection", speaker1, speaker2, speaker3)
textEntry = StringEntry("Message:", "Viel Spass am Programmieren!")
textEntry2 = StringEntry("Message:", "Enjoy programming!")
pane2 = EntryPane(textEntry2)
okButton = ButtonEntry("Speak")
pane3 = EntryPane(okButton)
dlg = EntryDialog(pane1, pane2, pane3)
dlg.setTitle("Synthetic Voice")

initTTS()

while not dlg.isDisposed():
    if okButton.isTouched():
        if speaker1.getValue():
            selectVoice("german-woman")
            text = textEntry.getValue()
        elif speaker2.getValue():
            selectVoice("german-man")
            text = textEntry.getValue()
        elif speaker3.getValue():
            selectVoice("english-man")
            text = textEntry2.getValue()
        if text != "":
            voice = generateVoice(text)
            openSoundPlayer(voice)
            play()  

