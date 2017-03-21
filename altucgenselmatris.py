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

print(matris)

for n in range(boyut):
    kat = int(matris[n][n])

if(kat==0):
a=1
while(n+a,boyut):
    matris[n],matris[n+1]=matris[n+1],matris[n]
    a=a+1
    if(kat==0):
    exit()
   
for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for b in range(boyut-1,-1,-1):
    for c in range(1,b+1):
         kat = float(matris[b-c][b])
         for d in range(boyut+1):
             matris[b-c][l] = float(matris[b-c][d])-float(matris[b][c])*(kat/float(matris[b][b]))
 
print(matris)		  
