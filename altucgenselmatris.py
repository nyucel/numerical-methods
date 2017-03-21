#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
dosya=open("katsayilar.txt")
matris = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    matris.append(line)
dosya.close()
boyut = len(matris)

for n in range(boyut):
    kat = int(matris[n][n])
    while kat==0:
        if(n!=boyut):
            for i in range(1,boyut-n):
                for j in range(boyut+1):
                    matris[n][j],matris[n+i][j] = matris[n+1][j],matris[n][j]
                kat = int(matris[n][n])
                if(kat==0 and n+i==boyut):
                    print("verilen matris cozumsuzdur")
                    sys.exit()
        else:
            print("verilen matris cozumsuzdur")
            sys.exit()
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
for n in range(boyut-1,-1,-1):
    for p in range(1,n+1):
        kat = float(matris[n-p][n])
        for q in range(boyut+1):
            matris[n-p][q]=float(matris[n-p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
print(matris)
