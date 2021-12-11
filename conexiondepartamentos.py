import pyodbc
from departamento import Departamento

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadena_conexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd + "; UID=" + usuario + "; PWD=" + password)

class Hospital:
    def __init__(self):
        self.conexion = pyodbc.connect(cadena_conexion)

    def ver_departamentos(self):
        cursor = self.conexion.cursor()
        sqlselect = "SELECT DEPT_NO, DNOMBRE, LOC FROM DEPT"
        cursor.execute(sqlselect)
        departamentos = []
        for row in cursor:
            departamentos.append(Departamento(row.DEPT_NO, row.DNOMBRE, row.LOC))
        cursor.close()
        return departamentos

    def buscar_departamento(self, numero):
        cursor = self.conexion.cursor()
        sqlselect = "SELECT DEPT_NO, DNOMBRE, LOC FROM DEPT WHERE DEPT_NO = ?"
        cursor.execute(sqlselect, (numero))
        row = cursor.fetchone()
        cursor.close()
        if row:
            departamento = Departamento(row.DEPT_NO, row.DNOMBRE, row.LOC)
            return departamento

    def nuevo_departamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlinsert = "INSERT INTO DEPT VALUES (?, ?, ?)"
        cursor.execute(sqlinsert, (numero, nombre, localidad))
        nuevo = cursor.rowcount
        cursor.commit()
        cursor.close()
        return nuevo

    def modificar_departamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlupdate = "UPDATE DEPT SET DNOMBRE = ?, LOC = ? WHERE DEPT_NO = ?"
        cursor.execute(sqlupdate, (nombre, localidad, numero))
        modificado = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificado

    def eliminar_departamento(self, numero):
        cursor = self.conexion.cursor()
        sqldelete = "DELETE FROM DEPT WHERE DEPT_NO = ?"
        cursor.execute(sqldelete, (numero))
        eliminado = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminado
