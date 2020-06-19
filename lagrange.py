#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

boyut=len(degerler[0])  #satırdaki elemanların adedi (sutun sayısı)
for m in range(len(degerler)):
    for n in range(boyut):
        degerler[m][n]=float(degerler[m][n])

sonuc=0
for i in range(boyut):
    carp=1
    carp2=1
    for k in range(boyut):
        if(k==i):
            continue
        else:
            carp=carp*(x-degerler[0][k])
            carp2=carp2*(degerler[0][i]-degerler[0][k])
    sonuc=sonuc+((carp/carp2)*degerler[1][i])
print(sonuc)
