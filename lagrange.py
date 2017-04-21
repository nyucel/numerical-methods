
#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []


for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

boyut=len(line)
carpim=1
carpim2=1
j=0
x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
for n in range(boyut-1):
	if n==0:
		for i in range(boyut-1):
			carpim=carpim*(x-degerler[0][i+1])
		for i in range(boyut-1):
			carpim2=carpim2*(degerler[0][0]-degerler[0][i+1])
		toplam=toplam+(carpim/carpim2)*(degerler[1][0])
		carpim=1
		carpim2=1
              
	elif n==(boyut-1):
		for i in range(boyut-2):
			carpim=carpim*(x-degerler[0][i])
                for i in range(boyut-2):
			carpim2=carpim2*(degerler[0][n]-degerler[0][i])
		toplam=toplam+(carpim/carpim2)*(degerler[1][n])
		carpim=1
		carpim2=1

	j=n
		
	else: 
		while j>0:
			carpim=carpim*(x-degerler[0][j-1]
			j=j-1	
		j=n
		while j>0:
			carpim2=carpim2*(degerler[0][n]-degerler[0][j-1]
			j=j-1
		j=n	
		while j<boyut-1:
			carpim=carpim*(x-degerler[0][j+1])
			j=j+1
                j=n
		while j<boyut-1:
			carpim2=carpim2*(degerler[0][n]-degerler[0][j+1])
			j=j+1

		toplam=toplam+(carpim/carpim2)*degerler[1][n]
		carpim=1
		carpim2=1



		
	

x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))
