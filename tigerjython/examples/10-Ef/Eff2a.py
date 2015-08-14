# Eff1a.py
# Teilsumme

from gamegrid import *
import itertools

coins = ["one", "two", "five", "ten", "twenty", "fifty"] 

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

makeGameGrid(8, 20, 40, False)
setBgColor(Color.white)
show()

n = 6 
k = 1
while k <= n:
    combinations = list(itertools.combinations(coins, k))
    print type(combinations)
    setTitle("(n, k) = (" + str(n) + ", " + str(k) + ") nb = "
    + str(len(combinations)))
    y = 0
    for moneybag in combinations:
        showMoneybag(moneybag, y)
        y += 1
    getKeyCodeWait()
    removeAllActors()
    k += 1

   
