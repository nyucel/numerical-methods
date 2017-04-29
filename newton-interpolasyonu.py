#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

for i in range(len(degerler)):
    for j in range(len(degerler[0])):
        degerler[i][j] = float(degerler[i][j])

n, carpim, toplam, sonlufark, nsonlu, fark = len(degerler[0]), 1, 0, [], len(degerler[0]), 1
sonlufark.append(degerler[1])
for i in range(n-1):
    temp = []
    for j in range(nsonlu-1):
        temp.append((sonlufark[i][j+1]-sonlufark[i][j])/(degerler[0][j+fark]-degerler[0][j]))
    sonlufark.append(temp)
    nsonlu = nsonlu-1
    fark = fark+1
    carpim = carpim * (x-degerler[0][i])
    toplam = toplam + carpim*sonlufark[i+1][0]
toplam = toplam + degerler[1][0]
print("Sonuc:",toplam)
