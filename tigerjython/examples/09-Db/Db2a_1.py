from dbapi import *

username = "admin"
password = "solar"
dbname = "casino"
serverURL = "localhost"
#serverURL = "10.1.1.123"

con = getDerbyConnection(serverURL, dbname, username, password)
cursor = con.cursor()
try:
   SQL = "CREATE TABLE res_20140115 (seat INTEGER, booked CHAR(1), cust INTEGER)"
   cursor.execute(SQL)
except Exception, e:
   print "SQL executing failed.", e 
else:
   print "Table created"
con.commit()
cursor.close()
con.close()
