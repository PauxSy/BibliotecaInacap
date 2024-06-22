from datetime import datetime, date

class Prestamos:
    def __init__(self, id_prestamo: int, rut_usuario: str, isbn_libro: int, tipo_prestamo: str, estado_prestamo: str, fecha_prestamo: date):
        self.id_prestamo = id_prestamo
        self.rut_usuario = rut_usuario
        self.isbn_libro = isbn_libro
        self.tipo_prestamo = tipo_prestamo
        self.estado_prestamo = estado_prestamo
        self.fecha_prestamo = fecha_prestamo
        
    def agregar_prestamo(self, prestamo):
        sql = "INSERT INTO Prestamos (id_prestamo, rut_usuario, isbn_libro, tipo_prestamo, estado_prestamo, FECHA_PRESTAMO) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (prestamo.id_prestamo, prestamo.rut_usuario, prestamo.isbn_libro, prestamo.Tipo_De_Prestamo, prestamo.estado_prestamo, prestamo.Fecha_Prestamo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def listar_prestamos(self):
        sql = "SELECT * FROM Prestamos"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            id_prestamo, rut_usuario, isbn_libro, Tipo_De_Prestamo, estado_prestamo, Fecha_Prestamo = prestamo
            print(f"id_prestamo: {id_prestamo}, rut_usuario: {rut_usuario}, isbn_libro: {isbn_libro}, Tipo_De_Prestamo: {Tipo_De_Prestamo}, estado_prestamo: {estado_prestamo}, Fecha_Prestamo: {Fecha_Prestamo}")
