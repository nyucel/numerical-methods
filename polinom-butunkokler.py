#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

xi = float(input("bir başlangıç değeri girin: "))

def f(dizi,x):
   toplam=0
   sayi=0
   for i in range(len(dizi)-1,-1,-1):
       toplam=toplam+(dizi[sayi])*pow(x,i)
       sayi=sayi+1 
   return(toplam)
def fi(dizi,x):
     toplam=0
     sayi=0
     for i in range(len(dizi)-1,-1,-1):
         if(i==0):
             break
         toplam=toplam+(dizi[sayi])*pow(x,i-1)*i
         sayi+=1
     return(toplam)
def fonk(dizi,xi):
     x1=xi
     for i in range(1000):
         x2=x1-(f(dizi,x1)/fi(dizi,x1))
         x1=x2
     return(x1)
dizi=[]

k=int(input("kaçıncı dereceden denklem:"))
 for i in range(k+1):
     if(i==k):
         l=float(input("sabit terimin katsayısını giriniz:"))
         dizi.append(l)
         continue
     l=float(input("x üzeri %d nin katsayısını giriniz:"%(k-i)))
     denklem.append(l)
xi = float(input("bir başlangıç değeri girin: "))

kokler=[]
while(len(dizi)!=2):
     kok=fonk(dizi,xi)
     xi=kok
     kokler.append(kok)
     for i in range(len(dizi)):
         dizi[i]=kok*(dizi[i-1])+dizi[i]
     dizi=dizi[:len(dizi)-1]
     if(len(dizi)==2):
         h=-dizi[1]/dizi[0]
         kokler.append(h)
  for i in range(k):
     print("%d. kok="%(i+1),kokler[i])

print(x1,x2,x3,x4,x5)
