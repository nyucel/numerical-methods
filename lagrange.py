#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))


Boyut=len(degerler[0])
for i in range(len(degerler)):
    for j in range(Boyut):
        degerler[i][j]=float(degerler[i][j])

Sonuc=0
for i in range(Boyut):
    carpim1=1
    carpim2=1
    for k in range(Boyut):
        if(k==i):
            continue
        else:
            carpim1=carpim1*(x-degerler[0][k])
            carpim2=carpim2*(degerler[0][i]-degerler[0][k])
    Sonuc=Sonuc+((carpim1/carpim2)*degerler[1][i])
print(Sonuc)
