#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Bazı fonksiyonlarda Newton-Raphson metodunun çok yavaş yakınsamasına bir örnek.
def f(x):
    return(x**10-1)

def fi(x):
    return(10*x**9)

def hata(x1,x2):
    return(abs((x1-x2)/x1))

x1 = float(input("bir başlangıç değeri girin: "))
h = 1

while(h>(10**(-10))):
    x2 = x1 - f(x1)/fi(x1)
    h = hata(x1,x2)
    print(x1,hata(x1,x2))
    x1 = x2
