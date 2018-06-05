#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("katsayilar.txt")
matris = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    matris.append(line)
dosya.close()
boyut = len(matris)

print("Matrisin saf hali :", matris)

kat = int(matris[0][0])
for n in range(boyut):
    sayac = n
    while(kat == 0):
        matris[n], matris[sayac] = matris[sayac], matris[n]
        kat = int(matris[n][n])
        sayac += 1


print("Matrisin köşegeninde 0 olmayacak biçimde düzenlenmiş hali :", matris)

for n in range(boyut):
    kat = int(matris[n][n])
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
print("Alt üçgensel matrise çevrilmiş hali :", matris)
for n in range(boyut - 1, -1, -1):
    deger = matris[n][boyut]
    for m in range(n -1, -1, -1):
        matris[m][boyut] = matris[m][boyut] - deger * matris[m][n]
        matris[m][n] = 0

for n in range(0, boyut):
    print(n + 1, ". değişkenin değeri :", matris[n][boyut])
