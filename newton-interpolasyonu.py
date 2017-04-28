#!/usr/bin/python3
# -*- coding: utf-8 -*-
dosya=open("lagrange.txt")
degerler = []
for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()
for m in range(len(degerler)):
   for n in range(len(degerler[0])):
       degerler[m][n]=float(degerler[m][n])
x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
def gerifark(boyut,dizi):
    gfarkdizi = []
    cevap=[]
    eleman=0
    for i in range(boyut):
        eleman=eleman+i
    for i in range(boyut-1):
        sonuc= (dizi[1][i+1]-dizi[1][i])/(dizi[0][i+1]-dizi[0][i])
        gfarkdizi.append(sonuc) 
    kontrol=len(gfarkdizi)
    r=1
    t=0
    for i in range(eleman):
        if(i+1==kontrol):
            kontrol-=1
            t=0
            i+=1
        if(eleman== (int(len(gfarkdizi)+1))):
            sonuc=(float((gfarkdizi[i+1]-gfarkdizi[i]))/float((dizi[0][boyut-1]-dizi[0][0])))
            cevap.extend(gfarkdizi)
            cevap.append(sonuc)
            return cevap
        sonuc=((gfarkdizi[i+1]-gfarkdizi[i])/(dizi[0][t+2]-dizi[0][t]))
        gfarkdizi.append(sonuc)
        t+=1
boyut= int(len(degerler[0]))    
yeni=[]
yeni.extend(gerifark(boyut,degerler))
sonuc,carp=1,1
a,r=0,boyut-1
toplam=0
for i in range (boyut-1):
    sonuc=sonuc*(x-degerler[0][i])
    carp=sonuc*yeni[a]
    toplam=toplam+carp
    a=a+r
    r=r-1
f=degerler[1][0]+toplam
print (f)












