#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import *
#def f(x,y):
#    return(x**2+x*y-10)
#def g(x,y):
#    return(y+3*x*y**2-57)

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))

for n in range(100):
    xi = sqrt(10-xi*yi)
    yi = sqrt((57-yi)/(3*xi))
    print(xi,yi)
