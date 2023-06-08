from math import sqrt
from sys import stdout

a = -2
b = 4

x = 0
for i in range (10**7):
    y = sqrt(x**3 + a*x + b)
    if y.is_integer():
        print ('', end=30*' '+'\r')
        print (x, y)
    else:
        print (x, y, end ='\r')
    x+=1
