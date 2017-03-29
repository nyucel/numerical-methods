#!/usr/bin/python3
# -*- coding: utf-8 -*-
dosya=open("katsayilar.txt")
for dizi in dosya.readlines():
    dizi = dizi.rstrip('\n').split(' ')
dosya.close()
boyut = len(dizi)
print(dizi)

for i in range(boyut):
	dizi[i]=int(dizi[i])
#def f(x):
#    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

def f(x,dizi):
    toplam=0
    index=0
    for i in range(boyut-1,-1,-1):
        toplam=toplam+(dizi[index])*pow(x,i)
        index=index+1
    return(toplam)

def fi(x,dizi):
    toplam=0
    index=0
    for i in range(boyut-1,-1,-1):
        if(i==0):
            break
        toplam=toplam+(dizi[index])*pow(x,i-1)*i
        index=index+1
    return(toplam)

    
def kokbul(xi,dizi):    
    for i in range(25):
       x2 = xi - f(xi,dizi)/fi(xi,dizi)
       xi = x2
    return(xi)
    
def polinombol(xi,dizi):
    for i in range(boyut):
        if(i==0):
            continue
        dizi[i]=dizi[i-1]*xi+dizi[i]
    return xi
        
xi = float(input("bir başlangıç değeri girin: ")) #başlangıç değerini -1 girdiğimizde division by zero hatası karşımıza geliyor
i=1
while(boyut>1):
    print("%d. kok"%(i),polinombol(kokbul(xi,dizi),dizi))
    i=i+1
    print(dizi)
    boyut=boyut-1
