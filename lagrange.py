#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

total = 0.0
length = len(degerler[0])
for i in range(length):
    temp=1.0
    for j in range(length):
        if(i != j):
            temp *= ((x-float(degerler[0][j]))/(float(degerler[0][i])-float(degerler[0][j])))

    total = (temp*float(degerler[1][i]))+total
print(total)

