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
    if(kat==0):
        j=0
        while(j<=boyut):
            matris[n][j],matris[n+1][j]=matris[n+1][j],matris[n][j]
            kat=int(matris[n][n])
            j=j+1
    if(kat==0):
        break
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

print(matris)

        
for i in range(boyut-1, -1, -1):
    for j in range(1,i+1):
        kat = float(matris[i - j][i])
        for k in range(boyut+1):
            matris[i - j][k] = float(matris[i - j][k]) - float(matris[i][k]) * (kat / float(matris[i][i]))


print(matris)

