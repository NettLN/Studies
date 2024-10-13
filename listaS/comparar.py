from LISTA import Lista
from NODO import Nodo
    
# def valores_iguales(lista1, lista2):
#     comunes = []
#     if lista1 is None or lista2 == None:
#         print("Una o ambas listas estan vacias")        
#     else:
#         actual1 = lista1.P
#         while actual1:
#             actual2 = lista2.P
#             while actual2:
#                 if  actual1.elemento == actual2.elemento:
#                     comunes.append(actual1.elemento)
#                 actual2 = actual2.siguiente
#             actual1 = actual1.siguiente
#         return comunes
    
# def ad_telefono(lista , i, numero):
#     pass
#     nuevo = Nodo(numero)
#     Actual.lista.P
#     existe = False
#     while Actual:
#         if Actual.elemento == numero:
#             existe = True
#             break
#         Actual = Actual.siguiente
#     if existe:
#         print("El numero ya existe en la lista")
#     else:
#         Actual1 = lista.P
#         auxiliar = 1
#         while Actual1 and auxiliar:
#             Actual = Actual1.siguiente
#             auxiliar += 1

#     if Actual1 is None:
#         print("La posicicion i-enesima no existe") 
#     else:
#         nuevo.siguiente = Actual1.siguiente
#         Actual.siguiente = nuevo
    
def edad(lista, z):
    if lista is None:
        print("Lista Vacia")
    else: 
        Actual = lista.P
        contador = 0
        while Actual:
            if Actual.elemento == z:
                contador += 1
            Actual = Actual.siguiente
    return print(contador)

def edad20(lista):
    if lista is None:
        print("Lista Vacia")
    else: 
        Actual = lista.P
        contador = 0
        while Actual:
            if Actual.elemento >= "20":
                contador += 1
            Actual = Actual.siguiente
    return print(contador)

# p1 = Lista()
# p2 = Lista()

# p1.agregar_final("ANA")
# p1.agregar_final("POL")
# p1.agregar_final("MARTIN")
# p1.agregar_final("JUAN")

# p2.agregar_final("POL")
# p2.agregar_final("JUAN")

# p1.mostrar_lista()
# p2.mostrar_lista()

# comun = valores_iguales(p1, p2)
# print(f"Elementos en comun: {comun}")

p1 = Lista()

p1.agregar_final("23")
p1.agregar_final("19")
p1.agregar_final("26")
p1.agregar_final("19")
p1.agregar_final("19")
p1.agregar_final("45")

p1.mostrar_lista()


# ad_telefono(p1, 7, 234452552)

edad(p1, "19")
edad20(p1)
