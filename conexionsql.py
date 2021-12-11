import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd + "; UID=" + usuario + "; PWD=" + password)

# cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd + "; Trusted_connection=yes")

try:
    print("Intentando conectar...")
    conexion = pyodbc.connect(cadena_conexion)
    print("¡Conexión establecida!")
except:
    print("Ha ocurrido un error.")
finally:
    conexion.close()
