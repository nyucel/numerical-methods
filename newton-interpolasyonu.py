#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y,n):
    sonuc = 0
    for i in range(n):
        payda = 1
        for j in range(0,n):
            if i == j:
                continue:
            payda *= x[i] - x[j]
        sonuc += y[i] / payda
    return sonuc

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

xi, yi = [], []
n = len(degerler[0])
for i in range(n):
    xi.append(float(degerler[0][i]))
    yi.append(float(degerler[0][i]))

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))
if x<xi[n-1] AND x>xi[0]:
    sonuc = 0
    for i in range(0,n):
        carp = 1
        for j in range(0,i):
            carp *= x - xi[j]
        sonuc += carp * f(xi,yi,j+1)
    sonuc += yi[0]
    print(sonuc)
else:
    print('belirlediğiniz x değeri için interpolasyon uygulanamaz.')
