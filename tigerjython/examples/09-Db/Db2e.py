from dbapi import *

table = "res_20140115"
username = "admin"
password = "solar"
dbname = "casino"
serverURL = "localhost"
#serverURL = "10.1.1.123"

con = getDerbyConnection(serverURL, dbname, username, password)
cursor = con.cursor()
try:
    SQL = "DROP TABLE " + table
except Exception, e:
    print "SQL executing failed. ", e 
else:
    print "Table removed"
con.commit()
cursor.close()
con.close()
