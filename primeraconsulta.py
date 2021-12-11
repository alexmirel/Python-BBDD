import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd +
"; UID=" + usuario + "; PWD=" + password)


conexion = pyodbc.connect(cadena_conexion)

# Cursor se crea con una conexión abierta
cursor = conexion.cursor()

# Necesitamos una consulta
# El cursor maneja tanto consultas de selección como consultas de acción
# No es conveniente utilizar *

sql = "select dept_no, dnombre, loc from dept"

# Hay que ejecutar la consulta
cursor.execute(sql)

# Podemos recorrer las filas:
# for row in cursor:
#     # Elegimos el índice de la columna
#     print(row[1])

#     # Podemos elegir una columna, es case-sensitive
#     print(row.LOC)


# Podemos recorrer un cursor para asignar cada columna con cada variable

# for row in cursor:
#     numero = row.dept_no
#     nombre = row.dnombre
#     localidad = row.loc

for numero, nombre, localidad in cursor:
    print(str(numero), nombre, localidad)

# Siempre debemos cerrar el cursor después de leer
cursor.close()

conexion.close()
