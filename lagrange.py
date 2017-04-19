#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
cozum=0
satir=len(degerler)
sutun=len(degerler[0])
for i in range(sutun):
    pay=1
    payda=1
    for j in range(sutun):
        if(i==j):
            continue
            else:
                pay=pay*(x-degerler[0][j])
                payda=payda*(degerler[0][i]-degerler[0][k])
                cozum=cozum((pay/payda)*degerler[1][i])
                
        
print(cozum)

