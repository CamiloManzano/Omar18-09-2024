primero = 0
segundo = 1
serie=[]


for i in range(0,100,1):
    cuenta=primero+segundo
    serie.append(cuenta)
    primero = segundo
    segundo = cuenta

print(serie)
