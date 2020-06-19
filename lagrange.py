#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("Fonksiyona hangi değer gönderilecek: "))
boyut = len(degerler[0])
for m in range(len(degerler)):
    for n in range(boyut):
        degerler[m][n] = float(degerler[m][n])

sonuc = 0
for i in range(boyut):
    pay = 1
    payda = 1
    for j in range(boyut):
        if (i == j):
            continue
        else:
            pay = pay * (x - degerler[0][j])
            payda = payda * (degerler[0][i] - degerler[0][j])
    sonuc = sonuc + ((pay/payda) * degerler[1][i])
print("f(",x,") = ",sonuc)

