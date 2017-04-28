#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya = open("lagrange.txt")
degerler = []
sozluk = {}
for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()
sozluk = {float(degerler[0][i]): float(degerler[1][i]) for i in range(len(degerler[0]))}


def fark(x, sozluk):
    keys = list(sozluk.keys())
    if x == 1:
        return (sozluk[keys[1]] - sozluk[keys[0]]) / (keys[1] - keys[0])
    sozluk2 = {keys[0]: (sozluk[keys[1]] - sozluk[keys[0]]) / (keys[1] - keys[0])}
    for i in range(1, len(keys) - 1):
        sozluk2[keys[i + 1]] = (sozluk[keys[i + 1]] - sozluk[keys[i]]) / (keys[i + 1] - keys[i])
    return fark(x - 1, sozluk2)


def carpim(sayi, x, sozluk):
    sonuc = 1
    keys = list(sozluk.keys())
    for i in range(sayi):
        sonuc *= x - keys[i]
    return sonuc


def Px(x, sozluk):
    key = list(sozluk.keys())
    toplam = sozluk[key[0]]
    for i in range(1, len(key)):
        toplam += carpim(i, x, sozluk) * fark(i, sozluk)
    return toplam


x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

print(Px(x, sozluk))
