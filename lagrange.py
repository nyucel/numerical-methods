#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

boyut = len(line)
boyut2 = len(degerler)

sonuc,sonuc1, genelsonuc= 1,1,0

for m in range(boyut2):
    for i in range(boyut):
        degerler[m][i] = int(degerler[m][i])

for xi in range(boyut):
    for n in range(boyut):
        if n==xi:
            continue
        else:
            sonuc1 = (x - degerler[0][n]) / (degerler[0][xi]-degerler[0][n])
        sonuc = sonuc * sonuc1
    sonuc = sonuc * degerler[1][xi]
    genelsonuc = genelsonuc + sonuc
    sonuc=1

print(genelsonuc)
