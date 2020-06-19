#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

def fonksiyon(dizi,xi):
    toplam=0
    isaret=0
    for i in range((len(dizi))-1,-1,-1):
        toplam=toplam+(dizi[isaret])*pow(x,i)
        isaret=isaret+1
        return(toplam)
xi=float(input("Bir baslangıc degeri : "))    
def turevFonksiyon(dizi,xi):
    toplam=0
    isaret=0
    for i in range(len(dizi)-1,-1,-1):
        if(i==0):
            break
        toplam=toplam+(dizi[isaret]*i*pow(x,i-1)
        isaret=isaret+1
        return(toplam)
def KokBul(dizi,x):
     x1=xi
     for i in range(1000):
         x2=x1-(fonksiyon(dizi,x1)/turevFonksiyon(dizi,x1))
         x1=x2
         return(x1)
 denklem = []  
 a=int(input("Denklemin derecesini giriniz: "))
        for i in range(a+1):
          if(i==a):
              d=float(input("Sabit terimin katsayısı : "))
              denklem.append(d)
              continue
              d=float(input("x üssü %d değeri:"%(a-i)))
              denklem.append(d)
 xi = float(input("Bir baslangic degeri giriniz : "))       

Kokler=[]
         while(len(denklem)!=2):
               kok=KokBul(denklem,xi)
               xi=kok
               Kokler.append(kok)
               for i in range(len(denklem)):
                       if(i==0):
                            continue
                    denklem[i]=kok*(denklem[i-1]) + denklem[i]
                    denklem = denklem[:len(denklem)-1]
                    if(len(denklem) == 2):
                    ek = -denklem[1]/denklem[0]
                    Kokler.append(ek)

                 for i in range(a):
             print("%d.kök ="%(i+1),Kokler[i])       
                       
