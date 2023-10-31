# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# ALEJANDRO SIERRA
# LAB 1 MONITORIA GRUPO 52
#SUMA DE DIGITOS

import random

def addition():
    # Extracción y suma de digitos 
    one = int(str(number)[0])
    two = int(str(number)[1])
    three = int(str(number)[2])
    sum1 = one + two + three
    
    five = int(str(number)[-1])
    four = int(str(number)[-2])
    sum2 = five + four
    
    if sum1 == sum2: # Comparación de  los resultados
        print(f" {sum1} and {sum2} they are PAIRS\n") # Impresión
    else:
        print(f" {sum1} and {sum2} they are: ODD\n")
    
if __name__ == '__main__': # Punto de entrada
    number = random.randint(10000, 99999) # Generando numero aleatorio
    print(f"\n The number is {number}")
    addition()