# Definimos el tamaño de la matriz

filas = int(input("Ingrese el tamaño de las filas: "))
cols = int(input("Ingrese el tamaño de las columnas: "))


# Creamos la matriz con el tamaño deseado


matrix = []


for i in range(filas):
    row=[]
    for element in range(cols):
        row.append(int(input(f"Ingrese el elemento {element} de la fila{i}")))
    matrix.append(row)

# Mostrar la matriz
# matriz[0][1]=10 Cambiar un número de una fila en especifico.

matrix.sort()

for fila in matrix:
    print(fila)