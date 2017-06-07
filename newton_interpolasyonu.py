#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("newton.txt")
d = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    d.append(line)
dosya.close()

x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))

boyut = len(line)
boyut2= len(d)

for m in range(boyut2):
    for i in range(boyut):
        d[m][i] = float(d[m][i])

def b_f(xi, yi):
    return ((d[1][yi] - d[1][xi]) / (d[0][yi] - d[0][xi]))

a = b_f(0, 1)
b = (x-d[0][1]) * (b_f(2, 1) - b_f(1, 0)) / (d[0][2] - d[0][0])
c = (x-d[0][1]) * (x-d[0][2]) * ((((b_f(3, 2) - b_f(2, 1)) / (d[0][3]-d[0][1])) - ((b_f(2, 0)-b_f(1, 0)) / (d[0][2]-d[0][0]))) / (d[0][3] - d[0][0]))

genelsonuc = d[1][0] + (x-d[0][0]) * (a + b + c)

print(genelsonuc)
