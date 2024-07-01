from datetime import date, timedelta
from devoluciones import Devoluciones

class Prestamos:
    def __init__(self, rut_usuario: str, isbn_libro: int, tipo_de_prestamo: str, estado_prestamo: str, fecha_prestamo: date, conexion, cursor):
        self.rut_usuario = rut_usuario
        self.isbn_libro = isbn_libro
        self.tipo_de_prestamo = tipo_de_prestamo
        self.estado_prestamo = estado_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.conexion = conexion
        self.cursor = cursor
        self.id_prestamo = self.generar_id_prestamo()

    def generar_id_prestamo(self):
        self.cursor.execute("SELECT IFNULL(MAX(id_prestamo), 0) + 1 FROM Prestamos")
        return self.cursor.fetchone()[0]

    def agregar_prestamo(self):
        if not self.verificar_limite_prestamos():
            print("El usuario ya tiene el máximo permitido de préstamos activos.")
            return

        # Verificar stock del libro
        if not self.verificar_stock():
            print("No hay suficiente stock para el libro solicitado.")
            return

        # Actualizar stock del libro
        self.actualizar_stock(-1)

        sql = "INSERT INTO Prestamos (id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_prestamo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.id_prestamo, self.rut_usuario, self.isbn_libro, self.tipo_de_prestamo, self.estado_prestamo, self.fecha_prestamo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    # Método para renovar préstamo
    def renovar_prestamo(self, id_prestamo_original, nueva_fecha_prestamo):
        # Obtener datos del préstamo original
        sql = "SELECT rut_usuario, isbn_libro FROM Prestamos WHERE id_prestamo = %s"
        self.cursor.execute(sql, (id_prestamo_original,))
        resultado = self.cursor.fetchone()
        if resultado:
            rut_usuario, isbn_libro = resultado

            # Cambiar el estado del préstamo original a 'Inactivo'
            sql_update_prestamo = "UPDATE Prestamos SET estado_prestamo = 'Inactivo' WHERE id_prestamo = %s"
            self.cursor.execute(sql_update_prestamo, (id_prestamo_original,))
            self.conexion.commit()

            # Cambiar el estado de la devolución a 'Devuelto'
            sql_update_devolucion = "UPDATE Devoluciones SET estado_devolucion = 'Devuelto' WHERE id_prestamo = %s"
            self.cursor.execute(sql_update_devolucion, (id_prestamo_original,))
            self.conexion.commit()

            # Registrar un nuevo préstamo con los mismos datos del original
            nuevo_prestamo = Prestamos(rut_usuario, isbn_libro, 'Renovación', 'Activo', nueva_fecha_prestamo, self.conexion, self.cursor)
            nuevo_prestamo.agregar_prestamo()

            # Registrar automáticamente una nueva devolución para el nuevo préstamo
            fecha_devolucion = nueva_fecha_prestamo + timedelta(days=3)
            nueva_devolucion = Devoluciones(nuevo_prestamo.id_prestamo, fecha_devolucion, 'Pendiente', self.conexion, self.cursor)
            nueva_devolucion.registrar_devoluciones()
        else:
            print("Préstamo original no encontrado.")
    
    def verificar_limite_prestamos(self):
        sql = "SELECT COUNT(*) FROM Prestamos WHERE rut_usuario = %s AND estado_prestamo = 'Activo'"
        self.cursor.execute(sql, (self.rut_usuario,))
        prestamos_activos = self.cursor.fetchone()[0]

        sql = "SELECT tipo_usuario FROM Usuarios WHERE rut_usuario = %s"
        self.cursor.execute(sql, (self.rut_usuario,))
        tipo_usuario = self.cursor.fetchone()[0]

        if tipo_usuario.lower() == "alumno" and prestamos_activos >= 4:
            return False
        return True

    def verificar_stock(self):
        sql = "SELECT stock FROM Libros WHERE isbn_libro = %s"
        self.cursor.execute(sql, (self.isbn_libro,))
        stock = self.cursor.fetchone()[0]
        return stock > 0

    def actualizar_stock(self, cantidad):
        sql = "UPDATE Libros SET stock = stock + %s WHERE isbn_libro = %s"
        self.cursor.execute(sql, (cantidad, self.isbn_libro))
        self.conexion.commit()
    
    def listar_prestamos(self):
        sql = "SELECT * FROM Prestamos"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_Prestamo = prestamo
            print(f"id_prestamo: {id_prestamo}, rut_usuario: {rut_usuario}, isbn_libro: {isbn_libro}, Tipo_De_Prestamo: {tipo_de_prestamo}, estado_prestamo: {estado_prestamo}, Fecha_Prestamo: {fecha_Prestamo}")

    def listar_renovaciones(self):
        sql = "SELECT * FROM Prestamos WHERE tipo_de_prestamo = 'renovacion'"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_Prestamo = prestamo
            print(f"id_prestamo: {id_prestamo}, rut_usuario: {rut_usuario}, isbn_libro: {isbn_libro}, Tipo_De_Prestamo: {tipo_de_prestamo}, estado_prestamo: {estado_prestamo}, Fecha_Prestamo: {fecha_Prestamo}")



