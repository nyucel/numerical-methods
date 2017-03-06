#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import e

def f(x):
    return(e**(-x)-x)

def fi(x):
    return(-e**(-x)-1)

def hata(x1,x2):
    return((x1-x2)/x1)

x1 = int(input("bir başlangıç değeri girin: "))

for i in range(5):
    x2 = x1 - f(x1)/fi(x1)
    print(x1, x2, hata(x2,x1))
    x1 = x2
