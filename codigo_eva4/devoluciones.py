class Devoluciones:
    def __init__(self, ID_Devolucion: int, ID_Prestamo: int, Fecha_Devolucion: date, Estado_Devolucion: str):
        self.ID_Devolucion = ID_Devolucion
        self.ID_Prestamo = ID_Prestamo
        self.Fecha_Devolucion = Fecha_Devolucion
        self.Estado_Devolucion = Estado_Devolucion
        
#  Métodos para gestionar devoluciones
    def registrar_devolucion(self, devolucion: Devolucion):
        sql = "INSERT INTO DEVOLUCIONES (ID_DEVOLUCION, ID_PRESTAMO, FECHA_DEVOLUCION, ESTADO_DEVOLUCION) VALUES (%s, %s, %s, %s)"
        valores = (devolucion.ID_Devolucion, devolucion.ID_Prestamo, devolucion.Fecha_Devolucion, devolucion.Estado_Devolucion)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

        sql_actualizar_prestamo = "UPDATE PRESTAMOS SET ESTADO_PRESTAMO = 'Devuelto' WHERE ID_PRESTAMO = %s"
        self.cursor.execute(sql_actualizar_prestamo, (devolucion.ID_Prestamo,))
        self.conexion.commit()

    def listar_devoluciones(self):
        sql = "SELECT * FROM DEVOLUCIONES"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devolucion in devoluciones:
            ID_Devolucion, ID_Prestamo, Fecha_Devolucion, Estado_Devolucion = devolucion
            print(f"ID_Devolucion: {ID_Devolucion}, ID_Prestamo: {ID_Prestamo}, Fecha_Devolucion: {Fecha_Devolucion}, Estado_Devolucion: {Estado_Devolucion}")


    # Listar devoluciones existentes
    biblioteca.listar_devoluciones()