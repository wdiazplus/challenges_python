# RETO

# Generar una lista de 50 números aleatorios.
# Dada la lista, mostrar en pantalla todos los números pares mayores a 50

from random import randint

numbers = []*50
lodeseado= []



#Creamos la lista de 50 números cualequiera entre 0 y 100
for number in range(0,50):
    number =  randint(0,100)
    numbers.extend([number])

for i in range(0,50):
    if numbers[i] >50 and (numbers[i]%2 == 0) :
        lodeseado.extend([numbers[i]])

print(lodeseado)
print(f'De los números aleatorios dados, hay {len(lodeseado)} que cumplen con la condición')




#  Mostraré aquí la solución dada por el creador del reto

# from random import randint

# if __name__ == '__main__':
#     numeros = [randint(0, 100) for _ in range(50)]

#     for numero in numeros:
#         if numero % 2 == 0 and numero > 50:
#             print(numero)