#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("katsayilar.txt")
matris = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    matris.append(line)
dosya.close()
boyut = len(matris)

for n in range(boyut):
    kat = int(matris[n][n])
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for n in range(boyut-1,-1,-1):
     for m in range(1,n+1):
         kat = float(matris[n-m][n])
         for p in range(boyut+1):
             matris[n-m][p] = float(matris[n-m][p])-float(matris[n][p])*(kat/float(matris[n][n]))
 

print(matris[0])
print(matris[1])
print(matris[2])