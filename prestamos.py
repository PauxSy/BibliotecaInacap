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

    #fran
    def agregar_prestamo(self):
        sql = "INSERT INTO Prestamos (id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_prestamo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.id_prestamo, self.rut_usuario, self.isbn_libro, self.tipo_de_prestamo, self.estado_prestamo, self.fecha_prestamo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    
    # ---------<< FUNCIONES DE RENOVACION ARIEEEL >>>----falta entenderlo y implementarlo con el menubiblioteca--
    # def agregar_prestamo(self, rut_usuario: str, isbn_libro: int, tipo_de_prestamo: str):
    #         # Obtener el cursor de la biblioteca
    #         cursor = self.biblioteca.conexion.cursor()

    #         # Obtener el tipo de usuario
    #         sql = '''SELECT TIPO_USUARIO FROM USUARIOS WHERE RUT_USUARIO = %s'''
    #         cursor.execute(sql, (rut_usuario,))
    #         tipo_usuario = cursor.fetchone()

    #         if not tipo_usuario:
    #             print("Usuario no encontrado")
    #             return

    #         tipo_usuario = tipo_usuario[0]

    #         # consulta para contar los prestamos y renovaciones 
    #         sql = '''SELECT COUNT(*), 
    #                         MAX(RENOVACIONES) 
    #                  FROM PRESTAMOS 
    #                  WHERE RUT_USUARIO = %s AND ISBN_LIBRO = %s AND DEVUELTO = 0'''
    #         cursor.execute(sql, (rut_usuario, isbn_libro))
    #         nro_prestamos, nro_renovaciones = cursor.fetchone()

    #         # Contar el número total de préstamos activos del usuario
    #         sql = '''SELECT COUNT(*) FROM PRESTAMOS WHERE RUT_USUARIO = %s AND DEVUELTO = 0'''
    #         cursor.execute(sql, (rut_usuario,))
    #         total_prestamos = cursor.fetchone()[0]

    #         def procesar_prestamo(nro_prestamos, nro_renovaciones, limite_prestamos, limite_renovaciones):
    #             if nro_prestamos > 0:
    #                 if nro_renovaciones >= limite_renovaciones:
    #                     print(f"El usuario solo puede renovar un libro hasta {limite_renovaciones} veces consecutivas")
    #                     return
    #                 # Renovar el préstamo existente
    #                 sql = '''UPDATE PRESTAMOS SET RENOVACIONES = RENOVACIONES + 1, FECHA_DEVOLUCION = DATE_ADD(FECHA_DEVOLUCION, INTERVAL 3 DAY) 
    #                          WHERE RUT_USUARIO = %s AND ISBN_LIBRO = %s AND DEVUELTO = 0'''
    #                 cursor.execute(sql, (rut_usuario, isbn_libro))
    #                 print("Préstamo renovado con éxito")
    #             else:
    #                 if total_prestamos >= limite_prestamos:
    #                     print(f"El usuario solo puede tener hasta {limite_prestamos} préstamo(s) activo(s) a la vez")
    #                     return
    #                 # Agregar un nuevo préstamo
    #                 sql = '''INSERT INTO PRESTAMOS (RUT_USUARIO, ISBN_LIBRO, TIPO_DE_PRESTAMO, FECHA_PRESTAMO, FECHA_DEVOLUCION, RENOVACIONES, DEVUELTO)
    #                          VALUES (%s, %s, %s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 0, 0)'''
    #                 cursor.execute(sql, (rut_usuario, isbn_libro, tipo_de_prestamo))
    #                 print("Préstamo agregado con éxito")

    #         if tipo_usuario == "Estudiante":
    #             procesar_prestamo(nro_prestamos, nro_renovaciones, 1, 1)
    #         elif tipo_usuario == "Docente":
    #             procesar_prestamo(nro_prestamos, nro_renovaciones, total_prestamos + 1, 3)
    #         else:
    #             print("Tipo de usuario no reconocido")
    #             return

    #         # Confirmar la transacción
    #         self.biblioteca.conexion.commit()
    #         cursor.close()

    def listar_prestamos(self):
        sql = "SELECT * FROM Prestamos"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_Prestamo = prestamo
            print(f"id_prestamo: {id_prestamo}, rut_usuario: {rut_usuario}, isbn_libro: {isbn_libro}, Tipo_De_Prestamo: {tipo_de_prestamo}, estado_prestamo: {estado_prestamo}, Fecha_Prestamo: {fecha_Prestamo}")

    def max_libros(self):
        None