#!/usr/bin/python3
# -*- coding: utf-8 -*-
# e sayısının ilk hesaplanmasında standart python kitaplığı kullanılırken ikinci hesaplamada decimal modülü kullanılmıştır.
# iki çıktı sırasıyla aşağıdaki gibidir:
# 2.7182818284590455
# 2.7182818284590452

from math import factorial
n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += 1/factorial(n)
    n += 1
print(e)

from decimal import *

getcontext().prec = 17

n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += Decimal(1/factorial(n))
    n += 1
print(e)

# Burada da yukarıda yapılan işlemin her bir iterasyonunda elde edilen çıktılar görünmektedir.
e = 0
for n in range(20):
    e += Decimal(1/factorial(n))
    print(e)
