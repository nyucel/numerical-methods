#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

satir=len(degerler)
sutun=len(degerler[0])
gerekenfark=[]
bfark=[]
sonuc=degerler[1][0]

for i in range(satir):
    for j in range(sutun):
        degerler[i][j]=float(degerler[i][j])
        
sayac=1
for i in range(sutun-1):
    for j in range(sutun-1):
        if (i==0):
            bfark.append(float((degerler[1][j+1]-degerler[1][j])/(degerler[0][j+1]-degerler[0][j])))
            gerekenfark[0]=bfark[0]
        if (i!=0):
            bfark[j]=((bfark[j+1])-(bfark[j]))/((degerler[0][j+sayac])-(degerler[0][j]))
            gerekenfark[i]=bfark[0]
        sayac=sayac+1
        sutun=sutun-1
        
for i in range(sutun-1):
    carpim=1
    for j in range(i+1):
        carpim=carpim*(x-degerler[0][j])
    carpim=carpim*gerekenfark[i]
    sonuc = sonuc+carpim    
   
print(sonuc)
