#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
row=len(degerler)
col=len(degerler[0])
afark=[]
bfark=[]
sonuc=degerler[1][0]
for i in range(row):
    for j in range(column)
    degerler[i][j]=float(degerler[i][j])
    sayac=1
for i in range (col-1):
    for j in range(column-1):
         if(i==0):
                bfark.append(float((degerler[1][j+1])-(degerler[1][j])/(degerler[0][j+1])-(degerler[0][j])))
                afark[0]=bfark[0]
                if(i!=0):
                    bfark[j]=((bfark[j+1])-(bfark[j]))/((degerler[0][j+sayac])-(degerler[0][j]))
                    afark[i]=bfark[0]
                    sayac=sayac+1
                    column=column-1
                    for i in range(column-1):
                        carpim=1
                        for j in range(i+1):
                            carpim=1
                            for j in range(i+1):
                                carpim=carpim*afark[i]
                                sonuc=sonuc+carpim
                                print(sonuc)
