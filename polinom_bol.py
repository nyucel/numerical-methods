def liste_oku():
    dosya = open("katsayilar.txt")
    for line in dosya.readlines():
        line = line.split(' ')
    dosya.close()
    return line


def polinom_bol(k, a):
    i = 1
    b = []
    if(a.length > 2):
        b[i] = a[i]
        while i < (a.length - 1):
            i = i + 1
            b[i] = a[i] + a[i - 1] * k
        return b


def f(a, x):
    n = len(a)
    r = 0
    sonuc = 0
    for n in range(n, -1, -1):
        sonuc = sonuc + x ** (n - r - 1) * a[n]
        r = r + 1
    return sonuc


def hata(x1, x2):
    return((x1 - x2) / x1)


def kokbul(a, x1, x3):
    while(hata < 0.000000000001):
        x2 = x1 - (f(a, x1) * (x3 - x1)) / (f(a, x3) - f(a, x1))
        x1, x3 = x3, x2
    return x2


kokx1 = int(input("bir başlangıç değeri girin: "))
kokx2 = int(input("ikinci başlangıç değerini girin: "))
liste = liste_oku()
kok = []
while (liste.length > 2):
    x = kokbul(liste, kokx1, kokx2)
    kok.add(x)
    liste = polinom_bol((-x), liste)

kok.add(-(liste[1] / liste[0]))
print(kok)
