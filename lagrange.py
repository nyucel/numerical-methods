#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

boyut=len(degerler[0])  
for a in range(len(degerler)):
     for b in range(boyut):
        degerler[a][b]=float(degerler[a][b])

for i in range(boyut):
      pay=1
    payda=1
      for j in range(boyut):
        if(j!=i):
                 pay *=(x-degerler[0][j])
                 payda *=(degerler[0][i]-degerler[0][j])
    sonuc +=((pay/payda)*degerler[1][i])

print sonuc 
