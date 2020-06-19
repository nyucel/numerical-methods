#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()
sonuc = 0.0
arasonuc = 1.0

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

for i in range(len(degerler[0])):
    for j in range(len(degerler[0])):
        if i!=j:
            arasonuc *= (x-float(degerler[0][j]))/(float(degerler[0][i])-float(degerler[0][j])) 
    sonuc += float(degerler[1][i])*arasonuc
    arasonuc = 1
print sonuc
