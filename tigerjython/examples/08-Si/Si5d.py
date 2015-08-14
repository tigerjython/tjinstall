from entrydialog import *
from decimal import *
getcontext().prec = 50

def a(k):
    return 1/16**Decimal(k) * (4 / (8 * Decimal(k) + 1) - 2 
    / (8 * Decimal(k) + 4) - 1
    / (8 * Decimal(k) + 5) - 1 / (8 * Decimal(k) + 6))

inp = IntEntry("n", 0)
out = StringEntry("Pi")
pane0 = EntryPane(inp, out)
btn = ButtonEntry("Next")
pane1 = EntryPane(btn)
dlg = EntryDialog(pane0, pane1) 
dlg.setTitle("BBP Series - Click Next")
n = 0
s = a(0)
out.setValue(str(s))
while not dlg.isDisposed():
    if btn.isTouched():
       n += 1
       s += a(n)
       inp.setValue(n)
       out.setValue(str(s))

