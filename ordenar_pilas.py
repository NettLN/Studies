from pilas import Pila

# Función para ordenar la pila usando una pila auxiliar
def ordenar_pila(pila):
    pila_auxiliar = Pila()

    while not pila.vacia():
        # Extraer el elemento de la pila original
        temp = pila.pop()

        # Mover elementos de pila_auxiliar a pila si son mayores que temp
        while not pila_auxiliar.vacia() and pila_auxiliar.peek() > temp:
            pila.push(pila_auxiliar.pop())

        # Apilar temp en la pila auxiliar
        pila_auxiliar.push(temp)

    # Mover los elementos de pila_auxiliar de regreso a la pila original
    while not pila_auxiliar.vacia():
        pila.push(pila_auxiliar.pop())

mi_pila = Pila()
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(6)
mi_pila.push(5)
mi_pila.push(8)
mi_pila.push(5)
mi_pila.push(4)

print("Pila antes de ordenar:")
mi_pila.mostrar()

ordenar_pila(mi_pila)

print("Pila después de ordenar:")
mi_pila.mostrar()