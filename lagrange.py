#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

uzunluk=len(degerler[0])

for i in range(len(degerler)):
    for j in range(uzunluk):
        degerler[i][j] = float(degerler[i][j])

toplam = 0.0

for i in range(uzunluk):
    carpim = 1.0
    bolum = 1.0
    for k in range(uzunluk):
        if (k==i):
            continue
        else:
            carpim *= (x-degerler[0][k])
            bolum *= (degerler[0][i] - degerler[0][k])
            sonuc = (carpim/bolum) * degerler[1][i]

    toplam += sonuc

print(toplam)
