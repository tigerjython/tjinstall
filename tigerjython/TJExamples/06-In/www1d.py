# ComKom1d.py

from ch.aplu.util import HtmlPane

html = open("welcome.html").read()
pane = HtmlPane()
pane.insertText(html)



