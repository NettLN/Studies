#Ordenar una pila de forma descendente de tal manera de que el elemnto menor aparesca en el tope de la pila utilizando una pila auxiliar
#El resultado debe mostrarse en la pila original

from pilas import Pila

def ordenar_pila(pila):
    if pila.vacia():
        print("La pila esta vacia")
        return None
    else:
        pila_aux = Pila()
        maximo = pila.peek()
        tamaño = pila.size()
        while tamaño > 1:
            if not pila.vacia():
                while not pila.vacia():
                    if pila.peek() <= maximo:
                        pila_aux.push(pila.pop())
                    else:
                        maximo = pila.peek()
                        print(maximo)
            else:
                pila.push(maximo)
                while not pila_aux.vacia():
                    if maximo > pila_aux.peek():
                        pila.push(pila_aux.pop())
                        print()

                    elif maximo == pila_aux.peek():
                        maximo = pila_aux.pop() 


        




                    
            tamaño -= 1
            
pila1 = Pila()
pila1.push(1)
pila1.push(7)
pila1.push(9)
pila1.push(2)
pila1.push(5)

pila1.mostrar()

ordenar_pila(pila1)

pila1.mostrar()

