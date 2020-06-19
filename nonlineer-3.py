#!/usr/bin/python3
# -*- coding: utf-8 -*-

def f(x,y):
    return(x**2+x*y-10)
+ def f_x(x,y):
    return (2*x+y)
+ def f_y(x,y):
    return (x)

def g(x,y):
    return(y+3*x*y**2-57)
+ def g_x(x,y):
    return (3*y**2)
+def g_y(x,y):
    return (1+6*x*y)

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))

+ for i in range(72)
+ xi=xi-((f(xi,yi)*g_y(xi,yi))-g(xi,yi)*f_y(xi,yi))/((f_x(xi,yi)*g_y(xi,yi))-(f_y(xi,yi)*g_x(xi,yi)))
+ yi=yi-((g(xi,yi)*f_x(xi,yi))-(f(xi,yi)*g_x(xi,yi)))/((f_x(xi,yi)*g_y(xi,yi))-(f_y(xi,yi)*g_x(xi,yi)))



print(xi,yi)
