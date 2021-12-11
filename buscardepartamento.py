import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd +
"; UID=" + usuario + "; PWD=" + password)


conexion = pyodbc.connect(cadena_conexion)

cursor = conexion.cursor()

# Vamos a pedir el número de departamento

numero = input("Introduzca el número del departamento. ")

sql = "select dept_no, dnombre, loc from dept where dept_no = " + numero

cursor.execute(sql)

row = cursor.fetchone()

if not row:
    print("No existe el departamento.")
else:
    print(row.dnombre, row.loc)

cursor.close()

conexion.close()
