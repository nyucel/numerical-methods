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
    kat = float(matris[n][n])
    degis = n
    while kat == 0:
        degis = degis +1
        if degis==boyut-1:
            print('Hata: Satir islemlerinde sıfır(0) hatasi. Matrisi cozume ulastiramadim.')
        matris[n],matris[degis]=matris[degis],matris[n]
        kat = float(matris[degis][degis])
    print (matris)

    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for n in range (boyut-1,0,-1):
    for m in range (1,n+1,+1):
        matris[n-m][n] , matris[n-m][n+1] = matris[n-m][n]-matris[n-m][n]*matris[n][n] , matris[n-m][n+1]-matris[n-m][n+1]*matris[n][n+1]

print(matris)
    
