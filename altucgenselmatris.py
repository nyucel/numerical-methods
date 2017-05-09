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
    if (kat == 0): ##Bir satir digerinin katiysa out of range hatası veriyor
        matris[n], matris[n + 1] = matris[n + 1], matris[n]
        kat=1 
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for a in range(boyut-1, -1, -1):
    for b in range(1,a+1):
        kat = float(matris[a - b][a])
        for c in range(boyut+1):
            matris[a - b][c] = float(matris[a - b][c]) - float(matris[a][c]) * (kat / float(matris[a][a]))

print(matris)
