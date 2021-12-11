import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"


class ConexionHospital:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE="+ bbdd + "; UID=" + usuario + "; PWD=" + password)

    def eliminar_enfermo(self, inscripcion):
        cursor = self.conexion.cursor()
        sqldelete = "DELETE FROM ENFERMO WHERE INSCRIPCION = ?"
        cursor.execute(sqldelete, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados
    
    def modificar_enfermo(self, apellido, inscripcion):
        cursor = self.conexion.cursor()
        sqlupdate = "UPDATE ENFERMO SET APELLIDO = ? WHERE INSCRIPCION = ?"
        cursor.execute(sqlupdate, (apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados
