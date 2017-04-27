#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    line = [float(i) for i in line]
    degerler.append(line)
dosya.close()
arasonuc,sonuc,boyut,sf = 1,degerler[1][0],len(degerler[0]),[]

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

sf.append(degerler[1])
for i in range(boyut-1):
    a = []
    for j in range(len(sf[i])-1):
        a.append((sf[i][j]-sf[i][j+1])/(degerler[0][j]-degerler[0][j+i+1]))
    sf.append(a)
    arasonuc *= x-degerler[0][i]
    sonuc += arasonuc*sf[i+1][0]
print sonuc
