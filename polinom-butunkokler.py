#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)


+ def fonk(dizi,x):
+     toplam=0
+     sayac=0
+     for i in range(len(dizi)-1,-1,-1):
+         toplam=toplam+(dizi[sayac])*pow(x,i)
+         sayac=sayac+1
+     return(toplam)

+ def fonksiyon(dizi,x):
+     toplam=0
+     sayac=0
+     for i in range(len(dizi)-1,-1,-1):
+         if(i==0):
+             break
+         toplam=toplam+(dizi[sayac])*pow(x,i-1)*i
+         sayac=sayac+1
+     return(toplam)


+ denklem=[]
+ derece=int(input("kaçıncı dereceden denklem girilecek "))
+ for i in range(derece+1):
+     if(i==derece):
+         katsayi=float(input("sabit terimin katsayisi nedir  "))
+         denklem.append(katsayi)
+         continue
+     katsayi=float(input("x in %d . kuvvetinin katsayisini girin  "%(derece-i)))
+     denklem.append(katsayi)


+def denk(dizi,xi):
+    x1 = xi
+    for i in range(10000):
+        x2 = x1 - (fonk(dizi,x1)/fonksiyon(dizi,x1))
+        x1 = x2
+    return(x1)

xi = float(input("bir başlangıç değeri girin: "))

+cozum = []
+while(len(denklem)!=2):
+    kok= denk(denklem,xi)
+    xi = kok
+    cozum.append(kok)
+    for i in range(len(denklem)):
+        if(i == 0):
+            continue
+        denklem[i]=kok*(denklem[i-1]) + denklem[i]
+    denklem = denklem[:len(denklem)-1]
+    if(len(denklem) == 2):
+        ve = -denklem[1]/denklem[0]
+        cozum.append(ve)

print(x1,x2,x3,x4,x5)

+for i in range(derece):
+    print("%d. kok="%(i+1),cozum[i])
