#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

def fonksiyon(dizi,xi):
    toplam=0
    j=0
    for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+(dizi[j]*(xi**i))
        j=j+1
    return toplam
def fi(dizi,xi):
    toplam=0
    j=0
    for i in range(len(dizi)-1,0,-1):
        toplam=toplam+(dizi[j]*i*(xi**(i-1)))
        j=j+1
    return toplam

def kokBul(dizi,xi):
    for i in range(10000):
        xi=xi-fonksiyon(dizi,xi)/fi(dizi,xi)
    return xi

derece=int(input("Kaçıncı dereceden polinom girmek istiyorsunuz?"))

dizi=[]
sonuc=[]
for i in range(derece+1):

    print("katsayıları giriniz")
    katsayı=int(input())
    dizi.append(katsayı)
print(dizi)

xi = float(input("bir başlangıç değeri girin: "))

while(len(dizi)>2):
    sonuc.append(xi)
    for i in range(1,len(dizi)-1):
        dizi[i]=dizi[i]+(dizi[i-1]*xi)

    dizi.pop()
    xi=kokBul(dizi,xi)
xi=-dizi[1]*dizi[0]
sonuc.append(xi)
print(sonuc)

