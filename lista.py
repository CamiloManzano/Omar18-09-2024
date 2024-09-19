aprendiz=["Hugo", "Paco", "Luis", "Beyota", "Bombom", "Burbuja"]
edad=list()
aprendiz.append("Mojojojo")
aprendiz.append("Dexter")
aprendiz=aprendiz+["Cosmo"]
aprendiz[2]="Pedro"

for i in range(len(aprendiz)):
    print(i)
    miEdad=input("Digite la edad del personaje "+str(i + 1))
    edad.append(miEdad)

print("Desordenado",aprendiz)
aprendiz.sort()
print("Ordenado",aprendiz)

print(edad)

saludo = "ADSO 06"

print(sorted(saludo.split(),key=len))

