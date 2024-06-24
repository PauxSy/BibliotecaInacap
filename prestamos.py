from datetime import date
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
        sql = "INSERT INTO Prestamos (id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_prestamo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.id_prestamo, self.rut_usuario, self.isbn_libro, self.tipo_de_prestamo, self.estado_prestamo, self.fecha_prestamo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def listar_prestamos(self):
        sql = "SELECT * FROM Prestamos"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_Prestamo = prestamo
            print(f"id_prestamo: {id_prestamo}, rut_usuario: {rut_usuario}, isbn_libro: {isbn_libro}, Tipo_De_Prestamo: {tipo_de_prestamo}, estado_prestamo: {estado_prestamo}, Fecha_Prestamo: {fecha_Prestamo}")

