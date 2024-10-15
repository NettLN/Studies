from NODO import Nodo

class Lista:
    def __init__(self):
        self.P = None
    
    def es_vacia(self):
        return self.P is None
    
    def mostrar_lista(self):
        A = self.P
        while A:
            print(A.elemento, end=" -> ")
            A = A.siguiente
        print("None")
            
    def contar_nodos(self):
        A = self.P
        cont = 0
        while A is not None:
            cont += 1
            A = A.siguiente
        return cont

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.P
        self.P = nuevo_nodo
    
    def agregar_final(self, dato):
        nuevo_nodo= Nodo(dato)
        if self.P == None:
            self.P = nuevo_nodo
        elif self.P.siguiente == None:
            self.P.siguiente = nuevo_nodo 
        else:
            actual=self.P
            while actual.siguiente: 
                actual = actual.siguiente     
            actual.siguiente = nuevo_nodo
    
    def eliminar_inicio(self):
        if self.P == None:
            print("Lista Vacia")
            
        elif self.P.siguiente is None:
            print("Se ha eliminado:", self.P)
            self.P = None
            
        else:
            print("Se ha eliminado del inicio:", self.P.elemento)
            actual = self.P
            self.p = actual.siguiente
            
        if self.P is not None:
            self.P = self.P.siguiente
        # return aux
    
    def eliminar_final(self):
        if self.P == None:
            print("Lista Vacia")
            
        elif self.P.siguiente is None:
            print("Se ha eliminado:", self.P)
            self.P = None
            
        else:
            actual = self.P
            while actual.siguiente:
                anterior = actual
                actual = actual.siguiente
            print("Se ha eliminado del final:", actual.elemento)
            anterior.siguiente = None

# def valores_iguales(self, lista1, lista2):
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
#                     break
#                 actual2 = actual2.siguiente
#                 else:
#                     print("No hay elemento iguales")

def eliminar2(lista):
    if lista.es_vacia():
        print("La lista esta vacia")
    
    else:
        actual = lista.P
        while lista.P.elemento % 2 == 0 and actual.siguiente != lista.P:
            print("Se ha eliminado:", lista.P.elemento)
            lista.P = lista.P.siguiente

        actual = lista.P            
        while actual.siguiente != None:
            if actual.siguiente.elemento % 2 == 0:
                print("Se ha eliminado:", actual.siguiente.elemento)
                actual.siguiente =  actual.siguiente.siguiente
            else:
                actual = actual.siguiente
                
def comparar(lista1, lista2):
    if lista1.es_vacia() and lista2.es_vacia():
        print("Ambas listas están vacías")
        return
    elif lista1.es_vacia():
        print("La lista 1 está vacía")
        lista2.mostrar_lista()
        return
    elif lista2.es_vacia():
        print("La lista 2 está vacía")
        lista1.mostrar_lista()
        return

    actual1 = lista1.P
    max1 = actual1.elemento
    while actual1:
        if actual1.elemento > max1:
            max1 = actual1.elemento
        actual1 = actual1.siguiente
        
    actual2 = lista2.P
    max2 = actual2.elemento
    while actual2:
        if actual2.elemento > max2:
            max2 = actual2.elemento
        actual2 = actual2.siguiente
        
    if max1 > max2:
        print(f"El mayor elemento {max1} es de la lista:")
        lista1.mostrar_lista()
    
    elif max2 > max1:
        print(f"El mayor elemento {max2} es de la lista:")
        lista2.mostrar_lista()
    
def juntar_listas(lista1, lista2):
    if lista1.es_vacia() and lista2.es_vacia():
        print("Ambas listas están vacías")
        return
    elif lista1.es_vacia():
        print("La lista 1 está vacía")
        lista2.mostrar_lista()
        return
    elif lista2.es_vacia():
        print("La lista 2 está vacía")
        lista1.mostrar_lista()
        return
    
    actual = lista1.P
    while actual.siguiente:
        actual = actual.siguiente
        
    actual.siguiente = lista2.P
    
    lista1.mostrar_lista()
    return lista1

def ordenar_lista(lista):
    if lista.es_vacia() or lista.P.siguiente is None:
        return 
    
    intercambiado = True
    while intercambiado:
        actual = lista.P
        intercambiado = False
        
        while actual.siguiente:
            if actual.elemento > actual.siguiente.elemento:
                actual.elemento, actual.siguiente.elemento = actual.siguiente.elemento, actual.elemento
                intercambiado = True
            actual = actual.siguiente
           
# prueba = Lista()
# prueba.agregar_inicio(2)
# prueba.agregar_inicio(65)
# prueba.mostrar_lista()
# prueba.agregar_final(43)
# prueba.agregar_final(56)
# prueba.mostrar_lista()
# print(str(prueba.contar_nodos()))
# prueba.eliminar_final()
# prueba.mostrar_lista()
# prueba.eliminar_inicio()
# prueba.mostrar_lista()

# lista_numeros = Lista()
# lista_numeros.agregar_final(6)
# lista_numeros.agregar_final(6)
# lista_numeros.agregar_final(9)
# lista_numeros.agregar_final(12)
# lista_numeros.agregar_final(15)
# lista_numeros.agregar_final(21)
# lista_numeros.agregar_final(30)
# lista_numeros.mostrar_lista()

# eliminar2(lista_numeros)
# lista_numeros.mostrar_lista()

listaA = Lista()
listaA.agregar_final("a")
listaA.agregar_final("Z")
listaA.agregar_final("z")
listaA.agregar_final("h")

listaB = Lista()
listaB.agregar_final("a")
listaB.agregar_final("t")
listaB.agregar_final("B")
listaB.agregar_final("x")

listaA.mostrar_lista()
listaB.mostrar_lista()

comparar(listaA, listaB)

lista_unida = juntar_listas(listaA, listaB)

ordenar_lista(lista_unida)
lista_unida.mostrar_lista()


