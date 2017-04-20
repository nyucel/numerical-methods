#!/usr/bin/python3
# -*- coding: utf-8 -*-
def P(liste,x):
    fonksiyon=0.0
    # sayac=0 ,f(x) degerinin kacinci deger oldugu
    for sayac in range(len(liste[0])):
        pay=1.0
        payda=1.0
        for i in range(0,len(liste[0])):
            if (sayac==i):
                i=i+1
                if (i>=len(liste[0])):
                    continue;
                    
            pay = pay*(x-int(liste[0][i]))
        for h in range(0,len(liste[0])):
            if (sayac==h):
                h=h+1
                if (h>=len(liste[0])):
                    continue;
                
            payda = payda*(int(liste[0][sayac])-int(liste[0][h]))
        fonksiyon = fonksiyon + (pay*int(liste[1][sayac]))/payda
    return (fonksiyon)
dosya=open("lagrange.txt")
liste = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    liste.append(line)
boyut=len(liste[0])
dosya.close()

while True:
    x = float(input("hangi degerin hesaplanmasini istiyorsunuz: "))
    print (P(liste,x))

