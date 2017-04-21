#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))

cozum=0
 boyut1=len(degerler)
 boyut2=len(degerler[0])
 
 for i in range(boyut2):
     ust=1
     alt=1
     for j in range(boyut2):
         if(i==j):
             continue
         else:
             ust=ust*(x-degerler[0][j])
             alt=alt*(degerler[0][i]-degerler[0][k])
             cozum=cozum+((ust/alt)*degerler[1][i])
 print(cozum)
