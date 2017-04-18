#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()


x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

xi = degerler[0]
yi = degerler[1]
n = len(xi)

sonuc = 0
for i in range(n):
    ekle, pay, payda = 0, 1, 1
    for j in range(0,n,1):
        if i==j:
            continue
        else:
            pay *= (x - float(xi[j]))
            payda *= (float(xi[i]) - float(xi[j]))
        ekle += float(yi[i]) * pay / payda
    sonuc += ekle

print ("X = ", x, " sonuc = ", sonuc)
    
