#!/usr/bin/python3
# -*- coding: utf-8 -*-
# verilen denkelem katsayıları ile köklerini bulan program

# Buradaki listede değişkenler x^0, x, x^1, x^2 şeklinde tanımlı
degiskenler = [-120, -46, 79, -3, -7, 1]

# değişkenlerin dereceleri terseten sıralı yani 0. elemanın üzeri x^0

def f1(x, girilen_liste):
    sonuc = 0
    for i in range(0, len(girilen_liste)):
        sonuc += pow(x, i) * girilen_liste[i]
    return sonuc


def turev(girilen_liste):
    yeni_liste = []
    for i in range(0, len(girilen_liste)):
        yeni_liste.append(girilen_liste[i] * i)
    del yeni_liste[0]
    return yeni_liste


def derece_dusur(kok, bolunen_liste):
    for i in range(len(bolunen_liste)-1, -1, -1):
        bolunen_liste[i-1] += kok * bolunen_liste[i]
    del bolunen_liste[0]
    return bolunen_liste


def kok_bul(xi, girilen_liste):
    while True:
        f2 = f1(xi, turev(girilen_liste))
        xn = xi - (f1(xi, girilen_liste) / f2)

        if (xn > xi):
            if ((xn - xi) < 0.0000001):
                return xn
        else:
            if ((xi - xn) < 0.0000001):
                return xn
        xi = xn

xi = float(input("Bir Başlangıç Değeri giriniz: "))

kokler = []
for i in range(0, len(degiskenler)-1):
    kokler.append(kok_bul(xi,degiskenler))
    derece_dusur(kokler[i], degiskenler)


for i in kokler:
    print(i, end=",")

