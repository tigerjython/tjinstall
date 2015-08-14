# Eff1b.py
# Teilsumme mit 12 Münzen (ohne Wiederholung)

from gamegrid import *
import itertools

coins = ["one", "one", "one", "two", "five", "five", 
         "ten", "ten", "ten", "ten", "twenty", "twenty", 
         "fifty", "fifty", "fifty"] 

def value(coin):
    if coin == "one":
        return 1
    if coin == "two":
        return 2
    if coin == "five":
        return 5
    if coin == "ten":
        return 10
    if coin == "twenty":
        return 20
    if coin == "fifty":
        return 50
    return 0

def getSum(moneybag):
    sum = 0
    for coin in moneybag:
        sum += value(coin)
    return sum

def showMoneybag(moneybag, y):
    x = 0
    for coin in moneybag:
        loc = Location(x, y)
        removeActor(getOneActorAt(loc))
        coinActor = Actor("sprites/" + coin + "cent.png")
        addActor(coinActor, loc)
        x += 1
    addActor(TextActor(str(getSum(moneybag))), Location(x, y))

makeGameGrid(15, 20, 40, False)
setBgColor(Color.white)
show()

target = 100

k = 1
result = []
count = 0
while k <= len(coins):
    combinations = tuple(itertools.combinations(coins, k))
    nb = len(combinations)
    for moneybag in combinations:
        count += 1
        sum = getSum(moneybag)
        if sum == target:
            if not moneybag in result:
               result.append(moneybag)
    k += 1

y = 0
for moneybag in result:
    showMoneybag(moneybag, y)
    y += 1
setTitle("Schritte: " + str(count) + ". Anzahl Lösungen für Summe "
          + str(target) + ": " + str(len(result)))

    
