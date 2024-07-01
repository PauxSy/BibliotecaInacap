from datetime import date, timedelta
class Devoluciones:
    def __init__(self, id_prestamo: int, fecha_devolucion: date, estado_devolucion: str, conexion, cursor):
        self.id_prestamo = id_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado_devolucion = estado_devolucion
        self.conexion = conexion
        self.cursor = cursor
        self.id_devolucion = self.generar_id_devolucion()

    def generar_id_devolucion(self):
        self.cursor.execute("SELECT IFNULL(MAX(id_devolucion), 0) + 1 FROM devoluciones")
        return self.cursor.fetchone()[0]

    @staticmethod
    def calcular_fecha_devolucion(rut_usuario, fecha_prestamo, cursor):
        sql = "SELECT tipo_usuario FROM Usuarios WHERE rut_usuario = %s"
        cursor.execute(sql, (rut_usuario,))
        tipo_usuario = cursor.fetchone()[0]

        if tipo_usuario.lower() == "alumno":
            return fecha_prestamo + timedelta(days=7)
        elif tipo_usuario.lower() == "docente":
            return fecha_prestamo + timedelta(days=20)
        else:
            raise ValueError("Tipo de usuario no válido")

    def registrar_devoluciones(self):
        # Verificar si ya existe una devolución para el id_prestamo
        sql_check = "SELECT * FROM devoluciones WHERE id_prestamo = %s"
        self.cursor.execute(sql_check, (self.id_prestamo,))
        devolucion_existente = self.cursor.fetchone()

        if devolucion_existente:
            # Si existe, actualizar el estado de la devolución a 'Devuelto'
            sql_update = "UPDATE devoluciones SET estado_devolucion = %s WHERE id_prestamo = %s"
            valores_update = ('Devuelto', self.id_prestamo)
            self.cursor.execute(sql_update, valores_update)
            self.conexion.commit()
            print("Devolución actualizada exitosamente a 'Devuelto'.")

            # Actualizar el estado del préstamo y el stock del libro
            sql_prestamo = "UPDATE Prestamos SET estado_prestamo = %s WHERE id_prestamo = %s"
            valores_prestamo = ('Inactivo', self.id_prestamo)
            self.cursor.execute(sql_prestamo, valores_prestamo)
            self.conexion.commit()

            # Actualizar el stock del libro
            self.actualizar_stock_libro(1)
        else:
            # Si no existe, insertar una nueva devolución
            sql_insert = "INSERT INTO devoluciones (id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion) VALUES (%s, %s, %s, %s)"
            valores_insert = (self.id_devolucion, self.id_prestamo, self.fecha_devolucion, self.estado_devolucion)
            self.cursor.execute(sql_insert, valores_insert)
            self.conexion.commit()

    def actualizar_stock_libro(self, cantidad):
        sql_libro = "SELECT isbn_libro FROM Prestamos WHERE id_prestamo = %s"
        self.cursor.execute(sql_libro, (self.id_prestamo,))
        isbn_libro = self.cursor.fetchone()[0]

        sql_update_stock = "UPDATE Libros SET stock = stock + %s WHERE isbn_libro = %s"
        self.cursor.execute(sql_update_stock, (cantidad, isbn_libro))
        self.conexion.commit()

    def listar_devoluciones(self):
        sql = "SELECT * FROM devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devolucion in devoluciones:
            id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion = devolucion
            print(f"id_devolucion: {id_devolucion}, id_prestamo: {id_prestamo}, fecha_devolucion: {fecha_devolucion}, estado_devolucion: {estado_devolucion}")


