import pyodbc

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LOCALHOST\SQLEXPRESS; DATABASE=HOSPITAL; UID=sa; PWD=azure")

incremento = int(input("Introduzca el incremento en el salario. "))
oficio = input("Introduzca el oficio. ")

cursor = conexion.cursor()

sql = "UPDATE EMP SET SALARIO += ? WHERE OFICIO = ?"

cursor.execute(sql, (incremento, oficio))

print(f"Ha incrementado el salario de {cursor.rowcount} empleados.")

cursor.commit()

sql2 = "SELECT APELLIDO, OFICIO, SALARIO FROM EMP WHERE OFICIO = ?"

cursor.execute(sql2, (oficio))

for apellido, oficio, salario in cursor:
    print(f"Apellido: {apellido}, Oficio: {oficio}, Salario: {salario}")

cursor.close()

conexion.close()
