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
boyut = len(degerler[0])

sonuc=0
for i in range(boyut):
    pay=1
    payda=1
    for j in range(boyut):
        if(j == i):
            continue
        else:
            pay = pay * (x-degerler[0][j])
            payda = payda * (degerler[0][i] - degerler[0][j])
    sonuc = sonuc + pay*degerler[1][i]/payda
print(sonuc)
