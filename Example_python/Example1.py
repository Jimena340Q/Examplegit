"""
    Fecha:18/09/2023
    Autor: Ximena Quintana
    Objetivo: Ejemplo de versionamiento con got desde python
"""
import random

print("Número aleatrorio entre 1 y 10")

random_number = random.randint(1, 10) #Genera un numero aleatrotio entre (randint)
print(random_number)

print("----------------------------------------------------------------")

for i in range(0, 10):
    random_number = random.randrange(20, 100, 5)#Genera numeros mutiplos de el tercer numero (randrange)
    print(random_number)

print("----------------------------------------------------------------")

for i in range(0, 10):
    random_number = random.random() #random.random : numeros decimales 
    print(random_number)

print("----------------------------------------------------------------")

for i in range(0, 10):
    random_number = random.uniform(10.5, 20.6) # random.uniform : numeros decimales de un rango ()
    print(random_number)

