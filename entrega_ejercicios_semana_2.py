"""
E-1
Escriba un programa que consulte al usuario si desea permanecer en el sitio 
web y si la respuesta es afirmativa imprimir en pantalla “Bienvenido”, 
en caso contrario escribir en pantalla “Nos vemos pronto”
"""


def bienvenida():
    continuar = input("Desea permanecer en el sitio web? s/n: ")
    #  verifico si la respuesta fue s o S, o n  o N .
    if continuar.lower() == "s":
        return "Bienvenido"
    elif continuar.lower() == "n":
        return "Nos vemos pronto"
    else:
        return "Responda solo con s o n"

# llamada a la función para mostrar los mensajes de bienvenida


print(bienvenida())



"""
E-2
Escriba un programa que solicite el ingreso de un número
y muestre en pantalla si es par o impar.
"""


def par_o_impar():
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"


print(par_o_impar())


"""
E-3
Escriba un programa que consulte por la edad de la persona e informe:
Si la persona no está en edad de trabajar.
Si la persona está en edad de trabajar, con su edad.
Si la persona está a un año de jubilarse.
"""


def  consulta_edad(edad):
    if edad < 18:
        return "No esta en edad de trabajar."
    elif 18 <= edad < 50:
        return f"La persona tiene {edad} años. Está en edad de trabajar."
    else:
        anios_restantes = 65 - edad
        return f"La persona tiene {edad} años. Esta a un año de jubilarse ({anios_restantes} años)."


edad = int(input("Ingrese su edad: "))


print(consulta_edad(edad))


"""
E-4
Escriba un programa que solicite la edad de la persona
e imprima todos los años que la persona ha cumplido.
"""


edad = int(input("ingrese su edad: "))


def  imprimir_edades(n):
    edades = []
    for i in range(1, (n + 1)):
        edades = edades + [i]
    
    return edades


print(f"has cumplido {imprimir_edades(edad)}  años")



"""
E-5
Escriba un programa que guarde en una variable una contraseña y
consulte al usuario por la contraseña hasta que esta sea correcta.
El programa debe informar al usuario si la contraseña fue correcta o no.
"""


def registro(base_datos):
    #registra el usuario y su contraseña dentro de un diccionario
    usuario = input("\tIngrese el nombre de usuario... ")
    contraseña = input("\tIngrese su contraseña... ")

    return base_datos.update({usuario: contraseña})


def login(base_datos):
    #verifica si el usuario existe en el diccionario y devuelve True o False

    usuario = input("ingrese su nombre de usuario: ")
    if usuario in bd:
        passw = input("Contraseña: ")
        if passw == bd[usuario]:
            print("\n\t¡Acceso permitido!")
            return True
        else:
            print("\t¡Error en la contraseña!")
            return False
    else:
        print("\tUsuario desconocido.")
        return False

#llamado a las funciones


bd = {}
registro(bd)
login(bd)


"""
E-6
Escriba un programa que consulte al usuario por una oración y comente al
usuario cuantas veces aparece la letra “a”. 
"""

frase = input("ingrese una oracion a analizar: ")
letra = input("indique que letra desea contar: ")

def  contador_de_letras(frase, letra):
    # Se convierte todo a minúsculas para no confundir las mayúsculas con las minúsculas.
    frase = frase.lower()
    letra = letra.lower()
    
    # Inicializa el contador en cero.
    contador = 0
    
    # Recorre cada letra de la frase.
    for l in frase:
        # Si la letra actual es igual a la que se quiere contar, incrementa el contador.
        if l == letra:
            contador +=1
            
    return contador

# Llama a la función e imprime el resultado.
print("la letra", letra, "aparece",contador_de_letras(frase,letra), "veces")