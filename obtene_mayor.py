from pilas import Pila
from producto import Producto

def obtener_mayor(pila):
    if pila.vacia():
        return None
    pila_auxiliar = Pila()
    maximo_precio = pila.pop()
    pila_auxiliar.push(maximo_precio)
    while not pila.vacia():
        elemento = pila.pop()
        if elemento.get_precio() > maximo_precio.get_precio():
            maximo_precio = elemento
        pila_auxiliar.push(elemento)

    while not pila_auxiliar.vacia():
        pila.push(pila_auxiliar.pop())

    return maximo_precio   

pila_productos = Pila()
pila_productos.push(Producto(1,"pantalon", 70.0))
pila_productos.push(Producto(2,"zapatos",350.0))
pila_productos.push(Producto(3,"camisa",150.0))

print ("La pila antes: ", pila_productos.mostrar())

mayor = obtener_mayor(pila_productos)

print (f"El producto con mayor precio es: {mayor}" )

print ("La pila despuess: ", pila_productos.mostrar())

