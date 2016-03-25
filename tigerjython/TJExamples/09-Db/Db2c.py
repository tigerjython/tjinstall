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
    for seatNb in range(1, 31):
        SQL = "INSERT INTO " + table + " VALUES (" + str(seatNb) + ",'N',0)"
        cursor.execute(SQL)
except Exception, e:
    print "SQL executing failed. ", e 
else:
    print "Table initialized"
con.commit()
cursor.close()
con.close()
