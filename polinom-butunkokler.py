#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(dizi,x):
    toplam=0;
    a=0
    for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+dizi[a]*x**i
        a+=1
    return toplam
def fi(dizi,x):
    toplam=0
    a=0
    for i in range(len(dizi)-1,0,-1): 
        toplam=toplam+a*i*x**i-1
        a+=1
    return toplam
def kokbul(dizi,xi):
    for i in range(1000):
        if(fi(dizi,xi)==0):
            print("hatali deger girdiniz:")
            xi=float(input("yeni degeri giriniz:"))
        x2=xi-f(dizi,xi)/fi(dizi,xi)
        xi=x2
    return (xi)
        
dizi=[]
cevapdizi=[]
derece=int(input("kaçıncı dereceden denklem olacak:"))
for i in range(derece+1):
    sayi2=float(input("%d dereenin sayisini giriniz:"%(i)))
    dizi.append(sayi2)
xi = float(input("bir başlangıç değeri girin: "))
while(len(dizi)-2):
    xi=kokbul(dizi,xi)
    cevapdizi.append(xi)
    for i in range(1,len(dizi)-1):
           dizi[i]=xi*dizi[i-1]+dizi[i]
    dizi.pop()
x=-1*dizi[1]/dizi[0]
cevapdizi.append(x)
print (cevapdizi)

