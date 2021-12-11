import pyodbc
from conexionhospital import ConexionHospital

# Eliminar enfermo
inscripcion = int(input("Introduzca el númeo de inscripción. "))

connection = ConexionHospital()

respuesta = connection.eliminar_enfermo(inscripcion)

print(f"Ha eliminado {respuesta} registro(s).")


# Modificar enfermo
inscripcion2 = input("Introduzca el número de inscripción. ")

apellido = input("Introduzca el nuevo apellido. ")

respuesta2 = connection.modificar_enfermo(apellido, inscripcion2)

print(f"Ha modificado {respuesta2} registro(s).")
