
#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("lagrange.txt")
degerler = []


for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    degerler.append(line)
dosya.close()

boyut=len(line)
alt,ust=1,1
j,toplam=0,0

for i in range(0,2):
	for j in range(0,boyut):
		degerler[i][j]=int(degerler[i][j])


x = int(input("hangi değerin hesaplanmasını istiyorsunuz: "))


for n in range(boyut-1):
	j=n
	if n==boyut-1:
		for i in range(boyut-2):
			ust=ust*(x-degerler[0][i])
		for i in range(boyut-2):
			alt=alt*(degerler[0][n]-degerler[0][i])
		toplam=toplam+(ust/alt)*(degerler[1][n])
		ust=1
		alt=1
	if n==0:
		for i in range(boyut-1):
			ust=ust*(x-degerler[0][i+1])
		for i in range(boyut-1):
			alt=alt*(degerler[0][0]-degerler[0][i+1])
		toplam=toplam+(ust/alt)*(degerler[1][0])
		ust=1
		alt=1

	else: 
		while j>0:
			ust=ust*(x-degerler[0][j-1])
			j-=1	
		j=n
		while j>0:
			alt=alt*(degerler[0][n]-degerler[0][j-1])
			j=j-1
		j=n	
		while j<boyut-1:
			ust=ust*(x-degerler[0][j+1])
			j+=1
		j=n
		while j<boyut-1:
			alt=alt*(degerler[0][n]-degerler[0][j+1])
			j=j+1

		toplam=toplam+(ust/alt)*degerler[1][n]
		ust=1
		alt=1



print(toplam)
