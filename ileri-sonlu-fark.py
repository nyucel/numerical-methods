'''
/**
 * created by cicek on 13.04.2018 20:41
 */
'''

def f(x):
    return x**3 + 2*x + 8 #hocanın derste yazdığı fonksiyon

x0, h = 1, 0
liste=[]
derece = int(input("kaçıncı dereceden ileri sonlu olsun: "))

if (derece == 0): # derece 0 ise 1 tane yazdırmalı
    print(f(x0+h))
    exit(1)

baslangic = derece + 1 #derecenin 1 fazlası 0. derecenin kaçtan başlayacağını belirler

for i in range(h, baslangic): # 0. dereceden ileri sonlu değer.
    liste.append(f(x0+h))
    h += 1
print(liste)

for i in range(0, baslangic-1): #1.dereceden itibaren istenilen yere kadar yapılan işlemler
    for i in range(0, len(liste)-1):
        liste[i] = (liste[i+1] - liste[i])
        if (i+2) == len(liste):
            liste.pop(-1)
    print(liste)
