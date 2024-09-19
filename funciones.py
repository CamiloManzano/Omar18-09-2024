'''
def suma (numA, NumB):
    operacion = numA + NumB
    return operacion


print(suma(5, 5))'''


'''
def suma (*num):
    print(num)
    operacion = 0
    for i in num:
        print(i)
        operacion +=1
    return operacion

print(suma(5, 3, 8))

'''


def suma (**kwargs):
    '''Funcion para sumar N numeros
    hecho por Yosito Lindo'''
    operacion = 0
    for key, value in kwargs.items():
        print(key, value)
        operacion += value
    return operacion


'''di = {'a': 5, "b":3, 'c':8}'''

print(suma.__doc__)

help(suma)
