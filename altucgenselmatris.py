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
        i=1
        while(n+i < boyut):
            matris[n] , matris[n+i] = matris[n+i] , matris[n]
            kat = int(matris[n][n])
            i = i + 1
        if(kat == 0):
            print("Bir satır başka bir satırın katı... Çıkılıyor...")
            exit()
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for i in range(boyut-1,-1,-1):
    for k in range(1,i+1):
        kat = float(matris[i-k][i])
        for l in range(boyut+1):
            matris[i-k][l] = float(matris[i-k][l])-float(matris[i][l])*(kat/float(matris[i][i]))

print(matris)
for i in range(1,boyut+1):
    print('x{0} = {1}'.format(i, matris[i-1][boyut]))
