#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))
uzunluk = len(degerler[0])
for m in range(len(degerler)):   #degerler dizisini float'a çeviriyoruz
    for n in range(uzunluk):
        degerler[m][n]=float(degerler[m][n])

toplam= 0.0
for i in range (uzunluk):
    carpim = 1.0
    bolum = 1.0
    for k in range (uzunluk):
        if(k==i):
            continue
        else:
            carpim=carpim*(x-degerler[0][k])
            bolum=bolum*(degerler[0][i]-degerler[0][k])
            sonuc=(carpim/bolum)*degerler[1][i]
    toplam=toplam+sonuc
print (toplam)
