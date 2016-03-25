import urllib2, json

search = input("Enter a search string(AND-connect with +):")
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + search
responseStr = urllib2.urlopen(url).read()
response = json.loads(responseStr)

#print "response:\n" + str(response) + "\n"

responseData = response["responseData"]
#print "reponseData:\n" + str(responseData) + "\n"

results = responseData["results"]
#print "results:\n" + str(results) + "\n"

for result in results:
   title = result["title"]
   url = result["url"]
   print title + " ---- " + url
