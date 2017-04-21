#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))
limit = len(degerler[0])
toplam = 0.0
for i in range(limit):
    k = 1.0
    l = 1.0
    for j in range(limit):
        if(i != j):
            k = k*(x-float(degerler[0][j]))
            l = l*(float(degerler[0][i])-float(degerler[0][j]))
    toplam = float(toplam+(k/l)*float(degerler[1][i]))
print(toplam)





