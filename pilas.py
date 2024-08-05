class Pila():
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)
        print(f"El elemento {dato} ha sido apilado")      
        
    def pop(self):
        if not self.datos:
            print("La pila esta vacia")
        else:
            dato = self.datos.pop()
            print(f"El elemento {dato} ha sido desapilado")
            return dato

    def mostrar(self):
        print(f"La pila completa es: {self.datos}")

objeto = Pila()
objeto.push(5)
objeto.push(3)
objeto.push(8)
objeto.push(7)
objeto.mostrar()
objeto.pop()
objeto.mostrar()
objeto.pop()
objeto.pop()
objeto.pop()
objeto.pop()
objeto.push(2)

