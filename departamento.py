class Departamento:
    def __init__(self, numero, nombre, localidad):
        self.numero = numero
        self.nombre = nombre
        self.localidad = localidad

    def __str__(self):
        return f"{self.numero} - {self.nombre} - {self.localidad}"
