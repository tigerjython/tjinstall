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
    SQL = "SELECT * FROM " + table
    cursor.execute(SQL)
except Exception, e:
    print "SQL execution failed.", e 
else:
    nbRecord = cursor.rowcount
    print "Number of records:", nbRecord
    result = cursor.fetchall() # list of tuples
    for record in result:
        print "seatNb:", record[0], " booked:", record[1]," cust:", record[2]
con.commit()
cursor.close()
con.close()
