#!/usr/bin/python3
# -*- coding: utf-8 -*-

#dizi=[1, 4, 3]
#dizi=[1, 1, -6, 0]
dizi=[1,-7, -3, 79, -46, -120] #polinomun sirasiyla x'lerin katsayilari girilmeli, en sona sabit deger varsa sabit deger, yoksa 0 girilmelidir.

yeni = []
for a in range(len(dizi)):
    yeni.append(dizi[a])
islem = []
kokler = []

while(1):
    xi = int(input("ilk deger girin: "))
    kacakadar = int(input("girdiginiz deger kaca kadar denensin: "))
    if(kacakadar == xi):
        print("girdiniz deger ile gidilmesi gereken uzaklik ayni olamaz!")
    else:
        break
xiyedek = xi
kacakadaryedek = kacakadar

if(xi > kacakadar):
    isaret = -1
else:
    isaret = 1
isaretyedek = isaret

def uzun_bol(yeni):
    boyut = len(yeni)
    islem.append(yeni[0])
    for i in range(boyut-1):
        islem.append(xi*islem[i]+yeni[i+1])
    if(islem[len(islem)-1] == 0):
        kokler.append(xi)
        yeni.clear()
        for a in range(len(islem)-1):
            yeni.append(islem[a])

while(xi !=  kacakadar):
    islem.clear()
    uzun_bol(yeni)
    xi = xi + isaret

if(len(yeni) != 1):
    kacakadar = -kacakadar
    xi = xiyedek
    isaret = -isaret
    while (xi != kacakadar):
        islem.clear()
        uzun_bol(yeni)
        xi = xi + isaret
   #tum kokler bulunamamissa
    if (len(kokler) + 1 != len(dizi)):
        print("Kokleri aradiginiz aralik cok dar, aralik artiriliyor...")
        print("Gidilmesini istediginiz eski uzaklik:", kacakadaryedek)
        kacakadar = kacakadaryedek+100
        print("Gidilecek yeni uzaklik:",kacakadar)
        xi = xiyedek
        isaret = isaretyedek
        while (xi != kacakadar):
            islem.clear()
            uzun_bol(yeni)
            xi = xi + isaret

        if (len(yeni) != 1):
            kacakadar = -kacakadar
            xi = xiyedek
            isaret = -isaret
            while (xi != kacakadar):
                islem.clear()
                uzun_bol(yeni)
                xi = xi + isaret

print("Kokler:",kokler)
