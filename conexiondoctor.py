import pyodbc
from doctor import Doctor, Centro

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd + "; UID=" + usuario + "; PWD=" + password)

class Hospital:
    def __init__(self):
        self.conexion = pyodbc.connect(cadena_conexion)

    def nuevo_doctor(self, codigo_hospital, apellido, especialidad, salario):
        cursor = self.conexion.cursor()
        sqlinsert = "INSERT INTO DOCTOR VALUES (?, (SELECT MAX(DOCTOR_NO)+1 FROM DOCTOR), ?, ?, ?)"
        cursor.execute(sqlinsert, (codigo_hospital, apellido, especialidad, salario))
        resultado = cursor.rowcount
        cursor.commit()
        cursor.close()
        return resultado

    def modificar_salario(self, incremento, numero):
        cursor = self.conexion.cursor()
        sqlupdate = "UPDATE DOCTOR SET SALARIO += ? WHERE DOCTOR_NO = ?"
        cursor.execute(sqlupdate, (incremento, numero))
        resultado = cursor.rowcount
        cursor.commit()
        cursor.close()
        return resultado
    
    def eliminar_doctor(self, numero):
        cursor = self.conexion.cursor()
        sqldelete = "DELETE FROM DOCTOR WHERE DOCTOR_NO = ?"
        cursor.execute(sqldelete, (numero))
        resultado = cursor.rowcount
        cursor.close()
        return resultado
    
    def buscar_doctor(self, numero):
        cursor = self.conexion.cursor()
        sqlselect = "SELECT HOSPITAL_COD, DOCTOR_NO, APELLIDO, ESPECIALIDAD, SALARIO FROM DOCTOR WHERE DOCTOR_NO = ?"
        cursor.execute(sqlselect, (numero))
        row = cursor.fetchone()
        cursor.close()
        if row:
            doctor = Doctor(row.HOSPITAL_COD, row.DOCTOR_NO, row.APELLIDO, row.ESPECIALIDAD, row.SALARIO)
            return doctor
    
    def mostrar_doctores(self):
        cursor = self.conexion.cursor()
        sqlselect = "SELECT HOSPITAL_COD, DOCTOR_NO, APELLIDO, ESPECIALIDAD, SALARIO FROM DOCTOR"
        cursor.execute(sqlselect)
        doctores = []
        for row in cursor:
            doctores.append(Doctor(row.HOSPITAL_COD, row.DOCTOR_NO, row.APELLIDO, row.ESPECIALIDAD, row.SALARIO))
        cursor.close()
        return doctores

    def mostrar_hospitales(self):
        cursor = self.conexion.cursor()
        sqlselect = "SELECT HOSPITAL_COD, NOMBRE FROM HOSPITAL"
        cursor.execute(sqlselect)
        hospitales = []
        for row in cursor:
            hospitales.append(Centro(row.HOSPITAL_COD, row.NOMBRE))
        cursor.close()
        return hospitales
