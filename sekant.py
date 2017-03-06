#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(x**2-2*x-3)

def hata(x1,x2):
    return((x1-x2)/x1)

x1 = int(input("bir başlangıç değeri girin: "))
x3 = int(input("ikinci başlangıç değerini girin: "))

for i in range(5):
    x2 = x1 - (f(x1)*(x3-x1))/(f(x3)-f(x1))
    print(x3, x1, x2, hata(x2,x1))
    x1,x3 = x3,x2
