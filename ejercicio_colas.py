class COLA():
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * max_size
        self.front = 0
        self.back = 0

    def vacia(self):
        return self.front == 0 and self.back == 0

    def lleno(self):
        return self.back == self.max
    
    def size(self):
        return self.back - self.front

    def enqueue(self, elemento):
        if not self.lleno():
            self.cola[self.back] = elemento
            self.back += 1
            print(f"Agregado: {elemento}")
        else:
            print("Cola llena...")
            print(f"No se agrego: {elemento}")        
    
    def dequeue(self):
        elemento = None
        if not self.vacia():
            elemento = self.cola[self.front]
            self.cola[self.front] = None
            self.front += 1
            if self.front == self.back:
                self.front = 0
                self.back = 0
            return elemento
        else:
            print("Cola vacía...")
            return None
                
    def obtener_maximo(self):
        if self.vacia():
            print("La cola está vacía")
            return None
        
        maximo = self.cola[self.front]
        for i in range(self.front, self.back):
            if self.cola[i] is not None and self.cola[i] > maximo:
                maximo = self.cola[i]
        print(f"Máximo: {maximo}")
        return maximo
    
    def obtener_pares(self):
        if self.vacia():
            print("La cola está vacía")
            return None
        
        pares = []
        for i in range(self.front, self.back):
            if self.cola[i] is not None and self.cola[i] % 2 == 0:
                pares.append(self.cola[i])
        print(f"Pares: {pares}")
        return pares

    def mostrar(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            print(self.cola[self.front : self.back])


# tamaño = int(input("Tamaño de la cola: "))

# cola = COLA(tamaño)

# while True:
#     print("Opciones:\n",
#           "1 : Agregar elemento\n",
#           "2 : Quitar\n",
#           "3 : Mostrar estado actual\n",
#           "4 : Mostrar elemento maximo\n",
#           "5 : Mostrar elementos pares\n",
#           "6 : Terminar Programa")
#     opcion = int(input("Elijo: "))
    
#     if opcion == 1:
#         aux = int(input("Digito: "))
#         cola.enqueue(aux)
        
#     elif opcion == 2:
#         print("Elemento quitado")
#         cola.dequeue()
#         print("\n")
        
#     elif opcion == 3:
#         print("Estado actual de la Cola")
#         cola.mostrar()
#         print()
    
#     elif opcion == 4:
#         cola.obtener_maximo()
        
#     elif opcion == 5:
#         cola.obtener_pares()
            
#     elif opcion == 6:
#         print("Resustado de la cola")
#         cola.mostrar()
#         print("Fin del programa\n")
#         break
    
#     else:
#         print("Opcion invalida")

    





# print("*******COLAS*********")
# print("Bienvenido al mundo las colas")

# while True:
#     print("******************COLAS*********")
#     print("Bienvenido al mundo las colas")
#     print("Opciones:\n",
#           "1 : Agregar elemento\n",
#           "2 : Quitar\n",
#           "3 : Terminar Programa\n"
#           )
#     opcion = int(input())
#     break    
ejemplo = COLA(6)
ejemplo.enqueue(3)
ejemplo.enqueue(9)
ejemplo.enqueue(27)
ejemplo.enqueue(91)
ejemplo.enqueue(73)
ejemplo.enqueue(23)

ejemplo.mostrar()
ejemplo.obtener_pares()

ejemplo.dequeue()
ejemplo.dequeue()
ejemplo.dequeue()


ejemplo.mostrar()
