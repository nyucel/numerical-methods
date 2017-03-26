#!/usr/bin/python3
# -*- coding: utf-8 -*-

def f(x,y):
	return(x**2+x*y-10)

def fx(x,y):
	return(2*x+y)

def fy(x,y):
	return(x)

def g(x,y):
	return(y+3*x*y*y-57)

def gx(x,y):
	return(3*y*y)

def gy(x,y):
	return(1+6*x*y)

xi = float(input("x baslangic degeri: "))
yi = float(input("y baslangic degeri: "))

for i in range(10):
	xi =xi + (- (f(xi,yi)*gy(xi,yi) - g(xi,yi)*fy(xi,yi))/(fx(xi,yi)*gy(xi,yi) - fy(xi,yi)*gx(xi,yi)))
	
	yi =yi + (- (g(xi,yi)*fx(xi,yi) - f(xi,yi)*gx(xi,yi))/(fx(xi,yi)*gy(xi,yi) - fy(xi,yi)*gx(xi,yi)))
	
	print(xi,yi)

