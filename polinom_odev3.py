def bolme(bolen,katsayilar): 
    i=1 
    sonrakiadim=[] 
    if(len(katsayilar)>2): 
        sonrakiadim[i]=katsayilar[i] 
        while(i<(len(katsayilar)-1)):
     i+=1  
            sonrakiadim[i]=katsayilar[i]+katsayilar[i-1]*bolen 
        return sonrakiadim 
def f(katsayi,x): 
    n=len(katsayi) 
    us=0 
    sonuc=0 
    for n in range(n,-1,-1): 
        sonuc+=x**(n-us-1)*katsayi[n] 
        us+=1 
    return sonuc  
def kok(katsayilar, s1, s2): 
    for i in range(100):
        s3=s1-(f(katsayilar,s1)*(s2-s1))/(f(katsayilar,s2)-f(katsayilar,s1)) 
 s1,s2=s2,s3
    return s3
tahmin1=int(input("bir baslangic degeri girin: ")) 
tahmin2=int(input("ikinci baslangic degerini girin: "))

derece=int(input("Kacinci dereceden polinom girmek istiyorsunuz?")) 
katsayilar=[] 
for i in range(derece+1): 
    print("katsayilari giriniz ")
    katsayi=int(input())
    katsayilar.append(katsayi) 
    
  
kokler=[] 
while (len(katsayilar)>2): 
    x=kok(katsayilar,tahmin1,tahmin2) 
    kokler.append(x) 
    katsayilar = bolme((-x), katsayilar) 
    kokler.append(-(katsayilar[1] / katsayilar[0])) 
print(kokler)

