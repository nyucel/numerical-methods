#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
    return(x**2+x*y-10)
def g(x,y):
    return(y+3*x*y**2-57)

def fx(x,y):
    return 2*x+y
def fy(x,y):
    return x
def gx(x,y):
    return 3*y**2
def gy(x,y):
    return 1+6*x*y

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))

for n in range(100)
    xi = xi - ( f(x,y)*gy(x,y) - g(x,y)*fy(x,y) ) / ( fx(x,y)*gy(x,y) - fy(x,y)*gx(x,y) )
    yi = yi - ( g(x,y)*fx(x,y) - f(x,y)*gx(x,y) ) / ( fx(x,y)*gy(x,y) - fy(x,y)*gx(x,y) )


print(xi,yi)
