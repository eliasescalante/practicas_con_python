"""
Ejercicio 7 – Dificultad muy alta
 isinstance(x, list) permite consultar si el elementos x es del tipo lista.
A partir de la siguiente función recursiva que permite
 
lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]
 
def recorre_lista(item): 
    for x in item: 
        if isinstance(x, list): 
            recorrer_lista(x) 
        else: 
            print(x) 
 
recorrer_lista(lista) 
 
Optimice el código de forma que el programa considere:
 
permite consultar si el elementos x es del tipo lista. 
A partir de la siguiente función recursiva que permite recorrer los niveles de una lista:
lista = ["elemento1n1", "elemento2n1", "elemento3n1", 
["elemento1n2", "elemento2n2", "elemento3n2", 
["elemento1n3", "elemento2n3", "elemento3n3"]]] 

"""

lista = ["elemento1n1", "elemento2n1", "elemento3n1", ["elemento1n2", "elemento2n2", "elemento3n2", ["elemento1n3", "elemento2n3", "elemento3n3"]]]
 
def recorrer_lista(item, nivel=0): 
    for x in item: 
        if isinstance(x, list): 
            recorrer_lista(x, nivel + 1)  # Incrementa el nivel de anidamiento
        else: 
            # Imprime el elemento con el nivel de anidamiento
            print("    " * nivel + str(x)) 


recorrer_lista(lista)

