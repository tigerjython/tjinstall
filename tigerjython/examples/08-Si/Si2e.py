# Si2d.py
# Lebenserwartung

n = 10000 # Groesse der Population

def readData(filename):
    table = []
    fData = open(filename)

    while True:
        line = fData.readline().replace(" ", "")
        if line == "":
            break
        line = line[:-1] # remove trailing \n
        try:
            q = float(line)
        except exceptions.ValueError:
           break
        table.append(q)
    fData.close()
    return table

qx = readData("qx.dat")
qy = readData("qy.dat")
x = n
y = n
xSum = 0
ySum = 0
for t in range(101):
    rx = qx[t]
    x = x - x * rx
    mx = x * rx # Todesfälle Mann
    xSum = xSum + mx * t #Beitrag Mann
    ry = qy[t]
    y = y - y * ry
    my = y * ry # Todesfälle Frau
    ySum = ySum + my * t #Beitrag Frau

print "Lebenserwartung Mann:", xSum / 10000
print "Lebenserwartung Frau:", ySum / 10000
