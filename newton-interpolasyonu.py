#!/usr/bin/python3
# -*- coding: utf-8 -*-
dosya=open("lagrange.txt")
degerler = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()
x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

for i in range(len(degerler)):
    for j in range(len(degerler[1])):
        degerler[i][j] = float(degerler[i][j])

xi,fxi,counter = degerler[0],degerler[1],1
result,increment = fxi[0],0
while(len(fxi) != 1):
    mul,f = 1,[]
    for i in range(len(fxi)-1):
        newvalue = (fxi[i+1]-fxi[i])/(xi[i+1+increment]-xi[i])
        f.append(newvalue)
    for index in range(counter):
        mul *= (x-xi[index])
    result += (mul*f[0])
    fxi,increment,counter = f,increment+1,counter+1
print(result)
