def tri(func):
    # inner function
    def _tri(x):
        if x == 0:
            return 0
        return round(func(x), 2)
    return _tri
 
@tri
def trisect(x):
    return 3 / x
 
for x in range(0, 11):  
   value = trisect(x)
   print value


