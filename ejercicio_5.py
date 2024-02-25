"""
Cree un programa que utilizando una función, solicite la edad de la persona e
imprima todos los años que la persona ha cumplido según el siguiente formato
de ejemplo
1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1
"""

def edades_descendente(edad):
    anios = edad
    while 1 < anios > 0:
        anios -= 1
        print(anios, end=", ")
    print(anios - 1)



def edades_ascendente(edad):
    anios = edad
    contador = 0

    while  contador < (edad - 1):
        print(contador + 1, end=", ")
        contador += 1
    print(contador + 1)

edades_ascendente(5)
edades_descendente(5)
