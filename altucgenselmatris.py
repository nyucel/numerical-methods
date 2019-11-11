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
    if(kat == 0):
        matris[n], matris[n+1] = matris[n+1], matris[n]
        kat = int(matris[n][n])
    for m in range(boyut+1):
        if (kat == 0):
            print('denklem çözümsüzdür')
            exit(1)
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

print(matris)

for n in range(boyut-1, 0, -1):
    for p in range(n-1, -1, -1):
        kat = int(matris[p][n])
        for q in range(boyut + 1):
            matris[p][q] = matris[p][q] - (matris[n][q] * kat)

print(matris)