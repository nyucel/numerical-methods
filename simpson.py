from math import e
def f(x):
    return(e**-x**3)
x0,x1 = 0,1
n = 10
integral = f(x0)+f(x1)
h = (x1-x0)/n
for i in range(int(n/2)):
    integral += 4*f(x0+h+2*i*h)
for i in range(int(n/2)-1):
    integral += 2*f(x0+2*h+2*i*h)
print(h/3*integral)
