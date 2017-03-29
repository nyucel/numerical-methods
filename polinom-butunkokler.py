#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

xi = float(input("bir başlangıç değeri girin: "))


print(x1,x2,x3,x4,x5)
def f(x):
      return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)
 
xi = float(input("bir başlangıç değeri girin: "))
 
 def fonk(dizi,xi):
     toplam=0
     j=0
     for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+(dizi[j]*(xi**i))
         j=j+1
     return toplam
 def kokler(dizi,xi):
     for i in range(99999):
         xi=xi-fonk(dizi,xi)/fok(dizi,xi)
     return xi
 def fok(dizi,xi):
     toplam=0
     j=0
     for i in range(len(dizi)-1,0,-1):
         toplam=toplam+(dizi[j]*i*(xi**(i-1)))
         j=j+1
     return toplam
 xi = float(input("bir başlangıç değeri girin "))
 der=int(input("Kaçıncı dereceden polinom girmek istiyorsunuz?"))
 dizi=[]
 cikti=[]
 for i in range(der+1):
     print("katsayıları gir ")
     katsayi=int(input())
     dizi.append(katsayi)
 xi = float(input("bir başlangıç değeri gir?"))
   
 while(len(dizi)>2):
     sonuc.append(xi)
     for i in range(1,len(dizi)-1):
         dizi[i]=dizi[i]+(dizi[i-1]*xi)
     dizi.pop()
     xi=kokler(dizi,xi)
 xi=-dizi[1]*dizi[0]
 cikti.append(xi)
 print(cikti)
  
  print(x1,x2,x3,x4,x5)
