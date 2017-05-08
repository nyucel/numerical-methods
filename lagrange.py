#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Ata Osman Özgüz
#160401073
#pxhım n,t vsşodös frhoşfot 
def floatYap(matris,en,boy):
    for i in range (en):
        for j in range (boy):
            matris[i][j] = float(matris[i][j])
            #return matris
def hesapla(matris,en,boy,deger):
    sonuc = 0.0
    for i in range (en):
        pay = 1.0
        payda = 1.0
        for  j in range(boy):
            if (i==j):
                continue
            else:
                pay = pay * (x - degerler[0][j])
                payda = payda * (degerler[0][i] - degerler[0][j])
                sonuc = sonuc + ((pay / payda) * degerler[1][i])
    print(f"{deger} degeri icin cozum: {sonuc}")

dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()



#print(degerler)
#print(len(degerler))
#print(len(degerler[0]))
floatYap(degerler,len(degerler),len(degerler[0]))
#print(degerler)
print("-------Lagrange Iterasyonu----------")

print(f"Asagidaki degerlerden yararlanılarak \n{degerler}  ")
x = float(input("Hangi değerin hesaplanmasını istiyorsunuz: "))
hesapla(degerler,len(degerler),len(degerler[0]),x)
