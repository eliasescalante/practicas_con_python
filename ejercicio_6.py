"""
Cree una función que tome la  siguiente  lista  y  reordene  de  menor  a 
mayor  sus componentes:
[3, 44, 21, 78, 5, 56, 9]
"""

def  ordenar_lista(lst):
    lista = lst    

    for  i in range(len(lista)):
        posicion_minima = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[posicion_minima]:
                posicion_minima = j
                
        lista[i], lista[posicion_minima] = lista[posicion_minima], lista[i]
        
    return lista
    
