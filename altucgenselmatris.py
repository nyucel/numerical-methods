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
    for satir in range(0,n): #üst satırları döndür
        print(satir)
        kat = matris[n-1-satir][n]
        print(kat)
        for m in range(n,boyut+1):
            matris[n-1-satir][m] -= matris[n][m]*kat
            
print(matris)
