dosya=open("katsayilar.txt")
matris = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    matris.append(line)
dosya.close()
boyut = len(matris)

for n in range(boyut):
    kat = int(matris[n][n])
    for m in range(boyut+1):
        matris[n][m]=int(matris[n][m])/kat
    for p in range(1,boyut-n):
        kat = float(matris[n+p][n])
        for q in range(boyut+1):
            matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

for m in range(boyut-1,0,-1):
    for n in range(boyut-1,0,-1):
        if(matris[n][m]==0):
            continue
        for p in range(1,boyut):
            if(matris[n-p][m]==0):
                continue
            kat=float(matris[n-p][m])/float(matris[boyut-p][boyut-p])
            for q in range(boyut+1):
                matris[n-p][q]=float(matris[n-p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

print(matris)
