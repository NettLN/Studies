class Pila():
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)
        #print(f"El elemento {dato} ha sido apilado")      
        
    def pop(self):
        if not self.datos:
            print("La pila esta vacia")
        else:
            dato = self.datos.pop()
            #print(f"El elemento {dato} ha sido desapilado")
            return dato

    def mostrar(self):
        print(f"La pila completa es: {self.datos}")

    def vacia(self):
        return len(self.datos) == 0

    def peek(self):
        if not self.vacia():
            return self.datos[-1]  
        else:
            return None

    def size(self):
        return len(self.datos)