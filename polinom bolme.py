from math import *

pol = [1,-7,-3,79,-46,-120]
boyut = len(pol)
print(pol)

def f(x):
	fpol=0
	for i in range(boyut):
		fpol +=pol[i]*pow(x,boyut-i)
	return(fpol)

def fi(x):
	fipol=0
	for i in range(boyut-1):
		fipol+=pol[i]*(boyut-i-1)*pow(x,boyut-i-1)
	return(fipol)
	
def k(x):
	for i in range(100):
		x = x - f(x)/fi(x)
	return(x)

for i in range(boyut-1):
	x = float(input("bir baslangic degeri girin:"))
	kok = k(x)
	print("{}. kok: {}".format(i+1,kok))
	for i in range(1,boyut):
		pol[i]+=pol[i-1]*kok
