class Doctor():
    def __init__(self, codigo_hospital, numero, apellido, especialidad, salario):
        self.codigo_hospital = codigo_hospital
        self.numero = numero
        self.apellido = apellido
        self.especialidad = especialidad
        self.salario = salario
    
    def __str__(self):
        return f"{self.codigo_hospital} - {self.numero} - {self.apellido} - {self.especialidad} - {self.salario}"

class Centro:
    def __init__(self, codigo_hospital, nombre):
        self.codigo_hospital = codigo_hospital
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.codigo_hospital} - {self.nombre}"
