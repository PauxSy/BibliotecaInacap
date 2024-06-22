class Devoluciones:
    def __init__(self, id_devolucion: int, id_prestamo: int, fecha_devolucion: str, estado_devolucion: str, conexion, cursor):
        self.id_devolucion = id_devolucion
        self.id_prestamo = id_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado_devolucion = estado_devolucion
        self.conexion = conexion
        self.cursor = cursor
        
#  Métodos para gestionar devoluciones
    def registrar_devoluciones(self):
        sql = "INSERT INTO devoluciones (id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion) VALUES (%s, %s, %s, %s)"
        valores = (self.id_devolucion, self.id_prestamo, self.fecha_devolucion, self.estado_devolucion)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

        sql_actualizar_prestamo = "UPDATE PRESTAMOS SET ESTADO_PRESTAMO = 'Devuelto' WHERE id_prestamo = %s"
        self.cursor.execute(sql_actualizar_prestamo, (self.id_prestamo,))
        self.conexion.commit()

    def listar_devoluciones(self):
        sql = "SELECT * FROM devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devoluciones in devoluciones:
            id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion = devoluciones
            print(f"ID_devoluciones: {id_devolucion}, id_prestamo: {id_prestamo}, fecha_devolucion: {fecha_devolucion}, Estado_devoluciones: {estado_devolucion}")


    def listar_devoluciones(self):
        sql = "SELECT * FROM Devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devolucion in devoluciones:
            id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion = devolucion
            print(f"ID_Devolucion: {id_devolucion}, id_prestamo: {id_prestamo}, Fecha_Devolucion: {fecha_devolucion}, Estado_Devolucion: {estado_devolucion}")
            
