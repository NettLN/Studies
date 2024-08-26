from pilas import Pila

def ordenar_pila(pila):
    if pila.vacia():
        print("La pila está vacía")
        return
    
    pila_aux = Pila()

    while not pila.vacia():
        maximo = pila.pop()

        # Transferimos los elementos de pila_aux a pila si son menores que maximo
        while not pila_aux.vacia() and pila_aux.peek() > maximo:
            pila.push(pila_aux.pop())
        
        pila_aux.push(maximo)

    while not pila_aux.vacia():
        pila.push(pila_aux.pop())

pila1 = Pila()
pila1.push(1)
pila1.push(7)
pila1.push(9)
pila1.push(2)
pila1.push(5)

print("Pila original:")
pila1.mostrar()

ordenar_pila(pila1)

print("Pila ordenada:")
pila1.mostrar()
