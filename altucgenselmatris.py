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
        index=1
        while(kat==0 and index+n<boyut):
            matris[n],matris[n+index]=matris[n+index],matris[n]
            index=index+1
            kat = int(matris[n][n])
        if(kat==0):
            print("Denklem sisteminin cozumu yok.")
            sys.exit()
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

print(matris)

for n in range(boyut):                                  
    for p in range(1,boyut-n):
        kat=float(matris[boyut-n-p-1][boyut-n-1])
        for q in range(boyut+1):
            matris[boyut-n-p-1][q]=float(matris[boyut-n-p-1][q])-float(matris[boyut-n-1][q])*(kat/float(matris[boyut-n-1][boyut-n-1]))
print(matris)

for i in range(boyut):
    print("x",i+1,"=",matris[i][boyut])
