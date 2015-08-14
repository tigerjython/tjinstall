import urllib2
from ch.aplu.util import HtmlPane

url = "http://www.meteoschweiz.admin.ch/web/de/wetter/detailprognose.html"
HtmlPane.browse(url)
html = urllib2.urlopen(url).read()
print html
