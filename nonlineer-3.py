#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
    return(x**2+x*y-10)
def g(x,y):
    return(y+3*x*y**2-57)

def gx(x,y):  #g fonksiyonunun x e gore türevi
    return(3*y**2)
def gy(x,y):  #g fonksiyonunun y ye gore turevi
    return( 1+6*x*y)
def fx(x,y):  #f fonksiyonun x e gore turevi
    return(2*x+y)
def fy(x,y):  # f fonsiyonunun y ye gore turevi
    return(y)

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))

for i in range (21):
    xi=xi-(f(xi,yi)*gy(xi,yi)-g(xi,yi)*fy(xi,yi))/(fx(xi,yi)*gy(xi,yi)-fy(xi,yi)*gx(xi,yi))
    yi=yi-(g(xi,yi)*fx(xi,yi)-f(xi,yi)*gx(xi,yi))/(gy(xi,yi)*fx(xi,yi)-gx(xi,yi)*fy(xi,yi))
    print(xi,yi)

print(xi,yi)
