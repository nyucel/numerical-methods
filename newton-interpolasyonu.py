dosya=open("lagrange.txt")
d = []
e=[-1] 

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    d.append(line)
dosya.close()
#print(d)

def bolunmusfark(a,e,boyut):
    b=a
    i=0
    c=[]
    c=e
    e=[]
    
    while((boyut-1-a)>0):
        e.append((float(c[i])-float(c[i+1]))/(float(d[0][i])-float(d[0][b+1])))
        b=b+1
        i=i+1
        a=a+1
    return(e)
x = float(input("hangi değerin hesaplanmasını istiyorsunuz: "))
fonksiyon = float(d[1][0])
carpim=1.0
boyut=len(d[0]) #4
e=d[1]
for a in range(boyut-1):
    u=bolunmusfark(a,e,boyut)
    carpim=carpim*(x-float(d[0][a]))
    #print("\n")
    e=[]
    e=u
    #print(e)
    fonksiyon = fonksiyon + carpim*u[0]

print(fonksiyon)



        
    

    
