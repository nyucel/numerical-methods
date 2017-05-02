from math import e
def f(x):
    return(e**x)

h = float(input("adim uzunlugu: "))
a,b = 0,1
integral = 0

for i in range(int((b-a)/h)):
    integral += f(a+h/2)
    a = a+h

print(integral*h)
