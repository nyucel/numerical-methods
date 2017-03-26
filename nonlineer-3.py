#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
    return(x**2+x*y-10)
def g(x,y):
    return(y+3*x*y**2-57)

xi = float(input("x için başlangıç değerini girin: "))
yi = float(input("y için başlangıç değerini girin: "))



def ana_fonk():
    try:
        global xi
        global yi
       
    def fx(x,y):
            return 2*x+y
        def fy(x,y):
            return x
        def f(x,y):
            return x**2 + x*y-10
        def g(x,y):
            return y+3*x*y*2-57
        def gx(x,y):
            return 3*x
        def gy(x,y):
            return 1+6*x*y

        for n in range(100):
          xi=xi-(f(xi,yi)*gy(xi,yi)-(xi*g(xi,yi)))/(fx(xi,yi)*gy(xi,yi)-xi*gx(xi,yi))
          yi=yi-(((f(xi,yi)*gx(xi,yi))-(g(xi,yi)*fy(xi,yi)))/((fx(xi,yi)*gy(xi,yi)-xi*(gx(xi,yi)))))
        print(xi,yi)
    except ZeroDivisionError:
        print("Sıfır değerleri girilemez!")
        return
ana_fonk()



print(xi,yi)
