from pilas import Pila

def invertir_pila(pila):
    if pila.vacia():
        print("La pila esta vacia")
        return None
    else:
        pila_aux1 = Pila()
        pila_aux2 = Pila()

        while not pila.vacia():
            pila_aux1.push(pila.pop())

        while not pila_aux1.vacia():
            pila_aux2.push(pila_aux1.pop())

        while not pila_aux2.vacia():
            pila.push(pila_aux2.pop())

mipila = Pila()
mipila.push(3)
mipila.push(56)
mipila.push(2)
mipila.push(6)

print("Pila antes de invertir: ")
mipila.mostrar()

invertir_pila(mipila)

print("Pila inverida: ")
mipila.mostrar()