import urllib2

def remove_html_tags(s):
   inTag = False
   out = ""

   for c in s:
      if c == '<':
         inTag = True
      elif c == '>':
        inTag = False
      elif not inTag:
         out = out + c
   return out

def remove_umlaute(s):
   s = s.replace("&auml;", "ä")
   s = s.replace("&ouml;", "ö")
   s = s.replace("&uuml;", "ü")
   s = s.replace("&Auml;", "Ä")
   s = s.replace("&Ouml;", "Ö")
   s = s.replace("&Uuml;", "Ü")
   return s

def remove_nbsp(s):
   s = s.replace("&nbsp;", " ")
   return s

def remove_blank_lines(s):
   s = s.replace("\n    \n", "\n")
   return s

html = urllib2.urlopen("http://www.meteoschweiz.admin.ch/web
/de/wetter/detailprognose.html").read()
html = remove_html_tags(html)
html = remove_umlaute(html) 
html = remove_nbsp(html) 

start = html.find("Wetterprognose für die")
end = html.find("Wetter und Temperatur")
html = html[start:end].strip()
html = remove_blank_lines(html)

print html
