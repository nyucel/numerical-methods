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
    if(kat==0):
        sayac=1
        while(sayac+n<boyut and kat==0):
            matris[n],matris[n+sayac]=matris[n+sayac],matris[n]
            sayac=sayac+1
            kat=int(matris[n][n])
        if(kat==0):
            sys.exit()
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
for n in range(boyut-1,0,-1):
    kat=matris[n][n]
    for i in range(boyut):
        if(i==n):
            break
        matris[i][n]=float(matris[i][n])-(kat*float(matris[i][n]))
print(matris)
