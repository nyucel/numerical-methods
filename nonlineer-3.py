#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
    return(x**2+x*y-10)
def g(x,y):
    return(y+3*x*y**2-57)
def fx(x,y):
    return(2*x+y)
def fy(x,y):
    return(x)
def gx(x,y):
    return(3*y**2)
def gy(x,y):
    return(1+6*x*y)

x = float(input("x için baslangiç degerini girin: "))
y = float(input("y için baslangiç degerini girin: "))
print("x",":",x,"---","y",":",y)
for i in range(10):
    x-=((f(x,y)*gy(x,y))-(g(x,y)*fy(x,y)))/((fx(x,y)*gy(x,y))-(x*gx(x,y)))
    y-=((g(x,y)*fx(x,y))-(f(x,y)*gx(x,y)))/((fx(x,y)*gy(x,y))-(x*gx(x,y)))
    print("x",i,":",x,"---","y",i,":",y)
