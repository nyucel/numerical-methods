def f(x):
	return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)
def f(dizi,xi):
	toplam=0;
	a=0
	for i in range(len(dizi)-1,-1,-1):
		toplam=toplam+dizi[a]*xi**i
		a+=1
	return toplam
def fi(dizi,xi):
	toplam=0
	a=0
	for i in range(len(dizi)-1,0,-1): 
		toplam=toplam+a*i*xi**i-1
		a+=1
	return toplam
def kokbul(dizi,xi):
	for i in range(100):
		x2=xi-f(x1)/fi(xi)
		xi=x2
	return (xi)     
dizi=[]
dizi2=[]
derece=int(input("kacinci dereceden denklem olacak:"))
for i in range(derece+1):
	xk=float(input("%d derecenin sayisini giriniz:"%(i)))
	dizi.append(xk)
xi = float(input("bir baslangic degeri girin: "))
while(len(dizi)-2):
	xi=kokbul(dizi,xi)
	dizi2.append(xi)
	for i in range(1,len(dizi)-1):
		dizi[i]=xi*dizi[i-1]+dizi[i]
	dizi.pop()
print(x1,x2,x3,x4,x5)
input()