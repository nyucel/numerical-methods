#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
dosya=open("lagrange.txt")
degerler = []
 
for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()
  
x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

for m in range(len(degerler)):
    for n in range(len(degerler[0])):
        degerler[m][n]=float(degerler[m][n])

sonuc=0
for i in range(len(degerler[0])):
    pay_carpimi=1
    payda_carpimi=1
    for j in range(len(degerler[0])):
        if(i==j):
            continue
        else:
            pay_carpimi=pay_carpimi*(x-degerler[0][j])
            payda_carpimi=payda_carpimi*(degerler[0][i]-degerler[0][j])
    sonuc=sonuc+((pay_carpimi/payda_carpimi)*degerler[1][i])
print(sonuc)
