#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10."""
__version__= "0.1.2"
__author__ = "Will Santos"
__license__ = "Unlicense"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range (1, 11))

print(numeros)

#iteração (percorrivel)

for numero in numeros:
    print("Tabuada do", numero)
    for outro_numero  in numeros:
        resultado =  numero * outro_numero
        #print(numero + " X " + outro_numero + " = " + resultado)
        print("{:^18}".format(f"{numero} x {outro_numero} = {resultado}"))
    print("-" * 12)