from datetime import datetime, date
import biblioteca

class devoluciones:
    def __init__(self, id_devolucion: int, id_prestamo: int, fecha_devolucion: date, estado_devolucion: str):
        self.id_devoluciones = id_devolucion
        self.id_prestamo = id_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado_devolucion = estado_devolucion
        
#  Métodos para gestionar devoluciones
    def registrar_devoluciones(self, devoluciones):
        sql = "INSERT INTO devoluciones (ID_devoluciones, id_prestamo, fecha_devoluciones, ESTADO_devoluciones) VALUES (%s, %s, %s, %s)"
        valores = (devoluciones.ID_devoluciones, devoluciones.id_prestamo, devoluciones.fecha_devoluciones, devoluciones.Estado_devoluciones)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

        sql_actualizar_prestamo = "UPDATE PRESTAMOS SET ESTADO_PRESTAMO = 'Devuelto' WHERE id_prestamo = %s"
        self.cursor.execute(sql_actualizar_prestamo, (devoluciones.id_prestamo,))
        self.conexion.commit()

    def listar_devoluciones(self):
        sql = "SELECT * FROM devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devoluciones in devoluciones:
            ID_devoluciones, id_prestamo, fecha_devoluciones, Estado_devoluciones = devoluciones
            print(f"ID_devoluciones: {ID_devoluciones}, id_prestamo: {id_prestamo}, fecha_devoluciones: {fecha_devoluciones}, Estado_devoluciones: {Estado_devoluciones}")


    def listar_devoluciones(self):
        sql = "SELECT * FROM Devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devolucion in devoluciones:
            ID_Devolucion, id_prestamo, Fecha_Devolucion, Estado_Devolucion = devolucion
            print(f"ID_Devolucion: {ID_Devolucion}, id_prestamo: {id_prestamo}, Fecha_Devolucion: {Fecha_Devolucion}, Estado_Devolucion: {Estado_Devolucion}")
            
    def registrar_devolucion(self, devolucion):
        sql = "INSERT INTO Devoluciones (ID_DEVOLUCION, id_prestamo, FECHA_DEVOLUCION, ESTADO_DEVOLUCION) VALUES (%s, %s, %s, %s)"
        valores = (devolucion.ID_Devolucion, devolucion.id_prestamo, devolucion.Fecha_Devolucion, devolucion.Estado_Devolucion)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

        sql_actualizar_prestamo = "UPDATE Prestamos SET estado_prestamo = 'Devuelto' WHERE id_prestamo = %s"
        self.cursor.execute(sql_actualizar_prestamo, (devolucion.id_prestamo,))
        self.conexion.commit()