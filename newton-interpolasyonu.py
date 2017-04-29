#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

for i in range(len(degerler)):
    for j in range(len(degerler[0])):
        degerler[i][j] = float(degerler[i][j])

n = len(degerler[0])
carpim = 1
toplam = 0
sonluFark = []
nSonlu = len(degerler[0])
fark = 1
sonluFark.append(degerler[1])
for i in range(n-1):
    temp = []
    for j in range(nSonlu-1):
        temp.append((sonluFark[i][j+1]-sonluFark[i][j])/(degerler[0][j+fark]-degerler[0][j]))
    sonluFark.append(temp)
    nSonlu -= 1
    fark += 1
    carpim *= (x-degerler[0][i])
    toplam += carpim*sonluFark[i+1][0]
toplam += degerler[1][0]
print("Sonuc:",toplam)
