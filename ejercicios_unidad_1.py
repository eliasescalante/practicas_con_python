# ELIAS ESCALANTE


## AGREGO LAS LIBRERIAS PARA UTLIZAR ALGUNOS METODOS
import sys
import math


# ejercicio 1
# programa que tome tres valores por consola multiplique el primer valor por el segundo
# y le sume el tercero. presente el resultado en la terminal del editor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("ingrese el tercer número: "))
result = (num1 * num2) + num3

print(f"los valores ingresados son : {num1} , {num2} y {num3}")

print(f"el resultado de la cuenta es: {result}")


# ejercicio 2
# Cree  un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
# son múltiplos de dos.




def multiples_numbers_of_2(num1, num2, num3):
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        return True

arg = sys.argv

print(f"ingresaste los siguientes números: {arg}")
if len(sys.argv) != 4:
    print("debes introducir exactamente 3 argumentos")
else :
    print(multiples_numbers_of_2(*map(int, arg[1:])))

""" ejercicio 3 y 4
Escriba un programa que solicite el radio de una circunferencia y
permita calcular el perimetro. Presente el resultado en la terminal del editor
utilizar la siguiente formula
 L = 2.pi * r
l = longitud de perimetro
pi = numero pi igual a ,1416
radio """



def calculation_circ(radio):
    #funcion para calcular la longitud de la circunferencia
    pi = math.pi
    longitud = 2 * radio * pi

    return longitud




def calculation_aerea(radio):
    # funcion para calcular el aerea
    pi = math.pi
    area = pi * (radio ** 2)

    return area

# pido por input el ingreso del radio
radio = float(input("ingresa el radio de la circunferencia: "))

# agrego una variable para poner una condicion de corte al while
validacion = 0
# mientras valga 0 el ciclo se repite.
while validacion == 0:
    # utilizo otra variable para determinar que se quiere calcular.
    choice = int(input("elige que deseas calcular: 1 para calcular la longitud y 2 para calcular el aerea: \n"))
    if choice == 1:
        print("el perimetro de la circunferencia es: ", calculation_circ(radio))
        # cambio el valor de la variable para cortar el ciclo
        validacion = 1
    elif choice == 2:
        print("\nla superficie de la circunferencia es: ", calculation_aerea(radio))
        # cambio el valor de la variable para cortar el ciclo
        validacion = 1
    else:
        print("opcion invalida")
        
# EJERCICIO 5

# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal del
# editor el valor incrementado en un 10%

#funcion para calcular el 10% de un numero y aumentarlo
def diez_porciento_del_valor(valor):
    diez_porciento_de_valor = valor * 0.1
    resultado = diez_porciento_de_valor + valor
    return resultado

valor = float(input("ingresa un numero: "))
print(f"el valor aumentado en un 10% del {valor} es {diez_porciento_del_valor(valor)}")


