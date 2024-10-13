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
        # aux = self.P
        
        
        if self.P is not None:
            self.P = self.P.siguiente
        # return aux
    
    def eliminar_final(self):
        if self.P == None:
            print("Lista Vacia")
            
        elif self.P.siguiente is None:
            self.P = None
            
        else:
            actual = self.P
            while actual.siguiente:
                anterior = actual
                actual = actual.siguiente
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
