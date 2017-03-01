#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import e
x = 42
for i in range(100):
    x = pow(e,-x)
print(x)
