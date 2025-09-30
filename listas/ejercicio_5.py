'''
Generar una lista con 100 números aleatorios entre 100 y 1000 
calcular el promedio de los valores de la lista
calcular el mayor y menor de los numeros
'''
import random
lista = []
for i in range(99):
    aleatorio = random.randint(100,1000)
    lista.append(aleatorio)
suma = 0
for i in range(len(lista)):
    suma += lista[i]
promedio = suma / len(lista)
print(f"promedio: {promedio:.2f}")
menor = min(lista)
print(f"menor: {menor}")
mayor = max(lista)
print(f"mayor: {mayor}")
