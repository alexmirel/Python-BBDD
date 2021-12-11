import pyodbc

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LOCALHOST\SQLEXPRESS; DATABASE=HOSPITAL; UID=sa; PWD=azure")

incremento = input("Introduzca el incremento en el salario. ")
oficio = input("Introduzca el oficio. ")

cursor = conexion.cursor()

sql = f"UPDATE EMP SET SALARIO += {incremento} WHERE OFICIO = '{oficio}'"

cursor.execute(sql)

print(f"Ha incrementado el salario de {cursor.rowcount} empleados.")

cursor.commit()

sql2 = f"SELECT APELLIDO, OFICIO, SALARIO FROM EMP WHERE OFICIO = '{oficio}'"

cursor.execute(sql2)

for apellido, oficio, salario in cursor:
    print(f"Apellido: {apellido}, Oficio: {oficio}, Salario: {salario}")

cursor.close()

conexion.close()
