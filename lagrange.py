#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

sonuc,boyut,a,b= 0,len(degerler[0]),0,0
for i in range(boyut):
    L = 1
    for j in range(boyut):
        if(a == j) : continue
        L *= (x-float(degerler[0][j]))/(float(degerler[0][a])-float(degerler[0][j]))
    if(b != boyut): L *= float(degerler[1][b])
    sonuc += L
    b,a = b+1,a+1

print(sonuc)
