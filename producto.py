class Producto:
    def __init__(self, codigo, nombre, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio

    def get_precio(self):
        return self.precio   

    def get_nombre(self):
        return self.nombre     
    
    def get_codigo(self):
        return self.codigo
    
    def set_precio(self, precio):
        self.precio = precio
        return self.precio
    
    def __str__(self):
        return f"{self.nombre} -- {self.precio}"