#!/usr/bin/python3
# -*- coding: utf-8 -*-

degerler = []
dosya = open("lagrance.txt")

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = float(input("Fonksiyona hangi değer gönderilecek: "))

for i in range(len(degerler)):
    for j in range(len(degerler[1])):
        degerler[i][j] = float(degerler[i][j])

xi,fxi,sayac = degerler[0],degerler[1],1
sonuc, artis = fxi[0], 0
while(len(fxi) != 1):
    mul, f = 1, []
    for i in range(len(fxi)-1):
        yeni_deger = (fxi[i+1]- fxi[i])/(xi[i+1+artis] - xi[i])
        f.append(yeni_deger)
    for index in range(sayac):
        mul *= (x - xi[index])
    sonuc += (mul*f[0])
    fxi, artis, sayac = f, artis+1, sayac+1
print("f(",x,") = ", sonuc)

