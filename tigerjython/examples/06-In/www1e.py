# ComKom1e.py

from ch.aplu.util import HtmlPane

def linkCallback(url):
   pane.insertUrl(url)

html = open("welcomex.html").read()
pane = HtmlPane(linkListener = linkCallback)
pane.insertText(html)



