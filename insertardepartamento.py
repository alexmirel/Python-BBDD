import pyodbc

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LOCALHOST\SQLEXPRESS; DATABASE=HOSPITAL; UID=sa; PWD=azure")

dept_no = input("Introduzca el número del departamento. ")
nombre = input("Introduzca el nombre del departamento. ")
loc = input("Introduzca la ubicación del departamento. ")

cursor = conexion.cursor()

sql = f"INSERT INTO DEPT VALUES ({dept_no}, '{nombre}', '{loc}')"

cursor.execute(sql)

# Rowcount devuelve el número de filas afectadas por la consulta
print("Rowcount: " + str(cursor.rowcount))

# Cuando realizamos consultas de acción, todas las acciones son temporales, no se llevan a la BBDD
# Para llevar las consultas de acción a la BBDD de forma permanente, debemos realizar un commit sobre cursor
cursor.commit()

sql2 = "SELECT DEPT_NO, DNOMBRE, LOC FROM DEPT"

cursor.execute(sql2)

for numero, nombre, localidad in cursor:
    print(str(numero), nombre, localidad)

cursor.close()

conexion.close()
