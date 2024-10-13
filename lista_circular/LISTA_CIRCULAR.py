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

    def mostrar_lista(self):
        if self.vacia():
            print("La lista esta vacia")
            
        else:
            actual = self.p
            print(actual.elemento, end=" -> ")
            while actual.siguiente != self.p:
                actual = actual.siguiente
                print(actual.elemento , end=(" -> "))
            print("ColaCircular")
            
    # def mostrar_lista(self):
    #     if self.vacia():
    #         print("La lista esta vacia")
            
    #     else:
    #         actual = self.p
            
    #         while actual.siguiente != self.p:
    #             print(actual.elemento, end=" -> ")
    #             actual = actual.siguiente
    #         print(actual.elemento , end=(" -> ColaCircular"))
    #         print()


# ----- P R U E B A S -------    
ListaCircular1 = ListaCircular()
ListaCircular1.agregar_final("Ana")
ListaCircular1.agregar_final("Pedro")
ListaCircular1.mostrar_lista()
ListaCircular1.agregar_final("anthony")
ListaCircular1.mostrar_lista()