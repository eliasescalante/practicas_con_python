"""
Cree una función lamba que compruebe si un número es par o impar.
"""
numero = lambda  x: "El numero es Par" if x % 2 == 0 else "El numero es Impar"


print(numero(7))
print(numero(10))