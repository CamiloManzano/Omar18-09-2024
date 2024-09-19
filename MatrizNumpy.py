matrix = ([1,2,3], [4,5,6], [7,8,9])
# print(matrix[1][2])

'''
#for fila in range(3):
    for col in range(3):
        print(matrix[fila][col])
'''

'''
print('FILA POR FILA')
for fila in matrix:
    print(fila)
'''

print('Todos los elementos en formato de matriz')
for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()


