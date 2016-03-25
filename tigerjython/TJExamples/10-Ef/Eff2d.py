from gpanel import *

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print n,
    print "Result 1"
while True:
    n = inputInt("Enter a start number:") 
    collatz(n)
