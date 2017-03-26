#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
    return(x**2+x*y-10)
+ def fix(x,y):
    + return(2*x+y)
+ def fiy(x,y):
    + return(x)
def g(x,y):
    return(y+3*x*y**2-57)
+ def gix(x,y):
    + return(3*y**2)
+ def giy(x,y):
    + return(1+6*x*y)

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))

+for i in range (42):
    + xi=xi-((f(xi,yi)*giy(xi,yi))-g(xi,yi)*fiy(xi,yi))/((fix(xi,yi)*giy(xi,yi))-(fiy(xi,yi)*gix(xi,yi)))
    + yi=yi-((g(xi,yi)*fix(xi,yi))-f(xi,yi)*gix(xi,yi))/((fix(xi,yi)*giy(xi,yi))-(fiy(xi,yi)*gix(xi,yi)))    


print(xi,yi)
+ print(xi,yi,i)
