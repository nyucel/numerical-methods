'''
/**
 * created by cicek on 14.04.2018 04:06
 */
'''

def f(x):
    return x**2 # f(x)=x**2

x0, h = 0, 0
liste=[]
derece = int(input("kaçıncı dereceden bölünmüş sonlu olsun (0'dan büyük bir "
                   "tam sayı giriniz!): "))

if (derece == 1): # derece 1 ise 1 tane yazdırmalı
    print(f(x0))
    exit(1)

baslangic = derece # 1. derecede kaç kere fonksiyon hesaplanacak.

for i in range(h, baslangic): # 0. dereceden ileri sonlu değer.
    liste.append(f(x0+h))
    h += 1
print(liste)

h=1
for i in range(0, baslangic-1): # 1.dereceden itibaren istenilen yere kadar yapılan işlemler
    for i in range(0, len(liste)-1):
        liste[i] = int((liste[i+1] - liste[i]) / h)
        if (i+2) == len(liste):
            liste.pop(-1) # son eleman işimize yaramadığı için çıkartıyoruz.
            h += 1 # her yeni listeye geçince h değeri 1 artar ve h bölümü her liste için sabittir.
    print(liste)
