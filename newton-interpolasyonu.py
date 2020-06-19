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

fark,farklar,boyut2,kat= [],[],boyut-1,1

for i in range(boyut-1):
    for j in range(boyut2):
        if (i==0):
            fark.append((degerler[1][j]-degerler[1][j+1])/(degerler[0][j]-degerler[0][j+kat]))
            farklar.append(float(fark[j]))
        if (i!=0):
            fark[j]=(float(fark[j])-float(fark[j+1]))/(float(degerler[0][j])-float(degerler[0][j+kat]))
            farklar[i]=float(fark[0])
    kat=kat+1
    boyut2=boyut2-1

anasonuc=degerler[1][0]
for i in range(boyut-1):
    aracarpim=1
    for j in range(i+1):
        aracarpim=aracarpim*(x-degerler[0][j])
    anasonuc = anasonuc + aracarpim*farklar[i]
print("Sonuc = ",anasonuc)
