class Nodo():
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
  
class ListaCircular():
    def __init__(self):
        self.p = None
        
    def vacia(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            print("Se ha agregado el primer nodo:", valor)
         
        else:
            actual = self.p
            print("Agregando nodo al final:", valor)
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p

    # def mostrar_lista(self):
    #     if self.vacia():
    #         print("La lista esta vacia")
            
    #     else:
    #         actual = self.p
    #         print(actual.elemento, end=" -> ")
    #         while actual.siguiente != self.p:
    #             actual = actual.siguiente
    #             print(actual.elemento , end=(" -> "))
    #         print("ColaCircular")
            
    def mostrar_lista(self):
        if self.vacia():
            print("La lista esta vacia")
            
        else:
            actual = self.p
            while actual.siguiente != self.p:
                print(actual.elemento, end=" -> ")
                actual = actual.siguiente
            print(actual.elemento , end=(" -> ColaCircular\n"))
    
    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            print("Se ha agregado al inicio:", valor)
        
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            self.p = nuevo_nodo
            print("Se ha agregado al inicio:", valor)
            
    def eliminar_inicio(self):
        if self.vacia():
            print("La lista esta vacia")
            
        else:
            actual = self.p
            if self.p == actual.siguiente:
                self.p = None
                print("Se ha eliminado:", actual.elemento)
                
            else:
                while actual.siguiente != self.p:
                    actual = actual.siguiente
                print("Se ha eliminado del inicio:", self.p.elemento)
                actual.siguiente = self.p.siguiente
                self.p = actual.siguiente
                                
    def eliminar_final(self):
        if self.vacia():
            print("La lista esta vacia")
        else:
            actual = self.p
            if self.p == actual.siguiente:
                self.p = None
                print("Se ha eliminado:", actual.elemento)
                
            else:
                while actual.siguiente.siguiente != self.p:
                    actual = actual.siguiente
                print("Se ha eliminado del final:", actual.siguiente.elemento)
                actual.siguiente = self.p
    
    def girar_lista(self):
        self.p = self.p.siguiente
            

def eliminar_multiplos(lista):
    if lista.vacia():
        print("La lista está vacía")
        return

    actual = lista.p
    inicio = lista.p
    
    while lista.p.elemento % 2 == 0 and actual.siguiente != lista.p:
        print(f"Eliminando {lista.p.elemento} (múltiplo de 2, nodo cabeza)")
        lista.eliminar_inicio()
        actual = lista.p
        inicio = lista.p

    if lista.vacia():
        return
    
    actual = lista.p
    while actual.siguiente != inicio:
        if actual.siguiente.elemento % 2 == 0:
            print(f"Eliminando {actual.siguiente.elemento} (múltiplo de 2)")
            actual.siguiente = actual.siguiente.siguiente 
        else:
            actual = actual.siguiente
            
                
            
# ----- P R U E B A S -------        

# ListaNumerica1 = ListaCircular()
# ListaNumerica1.agregar_inicio(3)
# ListaNumerica1.agregar_inicio(9)
# ListaNumerica1.agregar_inicio(12)
# ListaNumerica1.agregar_inicio(6)
# ListaNumerica1.agregar_inicio(30)
# ListaNumerica1.agregar_final(21)
# ListaNumerica1.agregar_inicio(27)
# ListaNumerica1.agregar_final(24)
# ListaNumerica1.agregar_inicio(18)
# ListaNumerica1.mostrar_lista()
# eliminar_multiplos(ListaNumerica1)
# ListaNumerica1.mostrar_lista()




ListaCircular1 = ListaCircular()
ListaCircular1.agregar_final("Ana")
ListaCircular1.agregar_final("Pedro")
ListaCircular1.mostrar_lista()
ListaCircular1.agregar_inicio("Anthony")
ListaCircular1.mostrar_lista()
ListaCircular1.mostrar_lista()
ListaCircular1.agregar_inicio("James")
ListaCircular1.agregar_final("Zara")
ListaCircular1.mostrar_lista()
ListaCircular1.eliminar_final()
ListaCircular1.eliminar_inicio()
ListaCircular1.mostrar_lista()