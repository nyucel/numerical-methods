#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

xi = float(input("bir başlangıç değeri girin: "))
def f(dizi,x):
    toplam=0
    a=0
    for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+(dizi[a])*pow(x,i)
        a+=1
    return(toplam)

def fi(dizi,x):
    toplam=0
    a=0
    for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+(dizi[a])*pow(x,i-1)*i
        a+=1
    return(toplam)
def fonk(dizi,xi):
    x1=xi
    for i in range(1000):
        x2=x1-(f(dizi,x1)/fi(dizi,x1))
        x1=x2
    return(x1)

dizi1=[]

cozumler=[]

derece=int(input("kaçıncı dereceden denklem girilecek:"))

for i in range(derece+1):
    if(i==derece):
        d=float(input("sabit terimin katsayısını giriniz:"))
        dizi1.append(d)
        continue
    d=float(input("x üzeri %d nin katsayısını giriniz:"%(derece-i)))
    dizi1.append(d)
    
xi = float(input("bir başlangıç değeri girin: "))

while(len(dizi1)!=2):
    kok=fonk(dizi1,xi)
    xi=kok
    cozumler.append(kok)
    for i in range(len(dizi1)):
        dizi1[i]=kok*(dizi1[i-1])+dizi1[i]
    dizi1=dizi1[:len(dizi1)-1]
    if(len(dizi1)==2):
        ek=-dizi1[1]/dizi1[0]
        cozumler.append(ek)

for i in range(derece):
    print("%d. kok="%(i+1),cozumler[i])


print(x1,x2,x3,x4,x5)
