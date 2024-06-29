from datetime import date, timedelta
import mysql.connector
import time

# Importación de clases
from devoluciones import Devoluciones
from multas import Multas
from prestamos import Prestamos
from usuarios import Usuarios
from libros import Libros

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self, host, user, password, port, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.cursor = self.conexion.cursor()

        # Verificar si la conexión está establecida al inicializar
        try:
            if self.conexion.is_connected():
                print("¡Conexión exitosa!")
        except mysql.connector.Error as e:
            print(f'Error al conectar a la base de datos: {e}')
    
    
    def ejecutar_consulta(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.conexion.commit()
            return result
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            self.conexion.rollback()


    def reporte_tipo_usuario(self, tipo_usuario):
        query = "SELECT * FROM usuarios WHERE tipo_usuario = %s"
        params = (tipo_usuario,)
        result = self.ejecutar_consulta(query, params)
        print(f"Reporte de usuarios tipo {tipo_usuario}:")
        for row in result:
            print(row)

    def reporte_prestamos_dia(self, fecha_prestamo):
        query = "SELECT * FROM prestamos WHERE fecha_prestamo = %s"
        params = (fecha_prestamo,)
        result = self.ejecutar_consulta(query, params)
        print(f"Reporte de préstamos para el día {fecha_prestamo}:")
        for row in result:
            print(row)

    def reporte_devoluciones_dia(self, fecha_devolucion):
        query = "SELECT * FROM devoluciones WHERE fecha_devolucion = %s"
        params = (fecha_devolucion,)
        result = self.ejecutar_consulta(query, params)
        print(f"Reporte de devoluciones para el día {fecha_devolucion}:")
        for row in result:
            print(row)
        

    def cerrar_conexion(self):
        self.conexion.close()
        print('Conexión cerrada.')

    @staticmethod
    def MenuBiblioteca():
        print("Bienvenido al sistema\n")
        print("Ingrese los datos de su base de datos\n")
        host = input("Ingrese el host (localhost): ")
        user = input("Ingrese el usuario (root): ")
        password = input("Ingrese la contraseña (0000): ")
        port = input("Ingrese el puerto (3306): ")
        database = input("Ingrese el nombre de la base de datos (PROYECTOFINAL): ")

        # Conectar a la base de datos
        mi_biblioteca = Biblioteca(host, user, password, port, database)
        multa = Multas(None,None,None,None,mi_biblioteca,valor_diario_multa=1000)
        usuario = Usuarios(None,None,None,None,None,None,mi_biblioteca,mi_biblioteca.cursor)


        while True:
            # Mostrar el menú principal 
            menu = int(input("""
            1. Gestionar Libros
            2. Gestionar Usuarios
            3. Gestionar Préstamos
            4. Gestionar Devoluciones
            5. Gestionar Renovaciones
            6. Generar Reporte
            7. Salir del Sistema
            Ingrese su opción: """))

            if menu == 1:
                while True:
                    # Menú de gestión de libros
                    menu_1 = int(input("""
                    1. Ingresar un Libro
                    2. Eliminar un Libro
                    3. Listar libros existentes
                    4. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_1 == 1:
                        print("Ingrese los datos del libro a guardar:\n")
                        isbn_libro = int(input("Ingrese el ISBN del libro: "))
                        genero = input("Ingrese el género: ")
                        titulo = input("Ingrese el título: ")
                        autor = input("Ingrese el autor: ")
                        stock = int(input("Ingrese el stock: "))
                        idioma = input("Ingrese el idioma: ")
                        nuevo_libro = Libros(isbn_libro, genero, titulo, autor, stock, idioma, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        nuevo_libro.agregar_libro()
                        print("Libro agregado exitosamente.")
                    elif menu_1 == 2:
                        isbn_libro = int(input("Ingrese el ISBN del libro a eliminar: "))
                        libro_a_eliminar = Libros(isbn_libro, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        libro_a_eliminar.eliminar_libro(isbn_libro)
                        print("Libro eliminado exitosamente.")
                    elif menu_1 == 3:
                        libros = Libros(None, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        libros.listar_libros_existentes()
                    elif menu_1 == 4:
                        break
                    else:
                        print("Opción no válida")

            elif menu == 2:
                while True:
                    # Menú de gestión de usuarios
                    menu_2 = int(input("""
                    1. Ingresar un Usuario
                    2. Eliminar un Usuario
                    3. Listar usuarios existentes
                    4. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_2 == 1:
                        print("Ingrese los datos del usuario a guardar:\n")
                        rut_usuario = input("Ingrese el RUT del usuario: ")
                        tipo_usuario = input("Ingrese el tipo de usuario (alumno - docente): ")
                        nombre = input("Ingrese el nombre del usuario: ")
                        apellido = input("Ingrese el apellido del usuario: ")
                        email = input("Ingrese el correo del usuario: ")
                        celular = int(input("Ingrese el número de celular del usuario: "))
                        nuevo_usuario = Usuarios(rut_usuario, tipo_usuario, nombre, apellido, email, celular, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        nuevo_usuario.agregar_usuario()
                        print("Usuario agregado exitosamente.")
                    elif menu_2 == 2:
                        rut_usuario = input("Ingrese el RUT del usuario a eliminar: ")
                        eliminar_usuario = Usuarios(rut_usuario, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        eliminar_usuario.eliminar_usuario(rut_usuario)
                        print("Usuario eliminado exitosamente.")
                    elif menu_2 == 3:
                        usuarios_bsd = Usuarios(None, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        usuarios_bsd.listar_usuarios_existentes()
                    elif menu_2 == 4:
                        break
                    else:
                        print("Opción no válida")

            elif menu == 3:
                while True:
                    # Menú de gestión de préstamos
                    menu_3 = int(input("""
                    1. Ingresar un préstamo
                    2. Listar préstamos existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_3 == 1:
                        print("Ingrese los datos del préstamo a guardar:\n")
                        rut_usuario = input("Ingrese el RUT del usuario: ")
                        if multa.comprobar_multas(rut_usuario):
                            continue
                        isbn_libro = int(input("Ingrese el ISBN del libro: "))
                        nuevo_prestamo = Prestamos(rut_usuario, isbn_libro, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)

                        tipo_de_prestamo = input("Ingrese el tipo de préstamo (Renovacion / Prestamo nuevo): ")
                        estado_prestamo = 'Activo'
                        fecha_prestamo = input("Ingrese la fecha del préstamo (YYYY-MM-DD): ")
                        fecha_prestamo = date.fromisoformat(fecha_prestamo)

                        # Verificar si hay stock suficiente para el libro
                        if not nuevo_prestamo.verificar_stock():
                            print("No hay suficiente stock para el libro solicitado.")
                            continue
                        
                        nuevo_prestamo = Prestamos(rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_prestamo, mi_biblioteca.conexion, mi_biblioteca.cursor)

                        if not nuevo_prestamo.verificar_limite_prestamos():
                            print("Ingreso de Prestamo denegado")
                            print("El usuario ya tiene el máximo permitido de préstamos activos.")
                            continue
                        
                        nuevo_prestamo.agregar_prestamo()

                        fecha_devolucion = Devoluciones.calcular_fecha_devolucion(nuevo_prestamo.rut_usuario, nuevo_prestamo.fecha_prestamo, mi_biblioteca.cursor)

                        estado_devolucion = 'Pendiente'
                        nueva_devolucion = Devoluciones(nuevo_prestamo.id_prestamo, fecha_devolucion, estado_devolucion, mi_biblioteca.conexion, mi_biblioteca.cursor)

                        nueva_devolucion.registrar_devoluciones()

                        print(f"Fecha de devolución estimada: {fecha_devolucion}")
                        print("Préstamo y devolución registrados exitosamente.")

                    elif menu_3 == 2:
                        prestamo = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamo.listar_prestamos()
                    elif menu_3 == 3:
                        break
                    else:
                        print("Opción no válida")

            elif menu == 4:
                while True:
                    # Menú de gestión de devoluciones
                    menu_4 = int(input("""
                    1. Registrar una devolución
                    2. Listar devoluciones existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_4 == 1:
                        print("Ingrese los datos de la devolución a guardar:\n")
                        id_prestamo = int(input("Ingrese el ID del préstamo: "))
                        fecha_devolucion = input("Ingrese la fecha de la devolución (YYYY-MM-DD): ")
                        fecha_devolucion = date.fromisoformat(fecha_devolucion)
                        estado_devolucion = 'Pendiente'  # estado_devolucion: Pendiente - Devuelto
                        nueva_devolucion = Devoluciones(id_prestamo, fecha_devolucion, estado_devolucion, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        nueva_devolucion.registrar_devoluciones()
                        print("Devolución realizada con éxito.")
                    elif menu_4 == 2:
                        devolucion = Devoluciones(None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        devolucion.listar_devoluciones()
                    elif menu_4 == 3:
                        break
                    else:
                        print("Opción no válida")

            elif menu == 5:
                while True:
                    menu_5 = int(input("""
                    1. Renovar un préstamo
                    2. Listar renovaciones existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_5 == 1:
                        id_prestamo_original = int(input("Ingrese el ID del préstamo original: "))
                        nueva_fecha_prestamo = date.today()
                        prestamos = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamos.renovar_prestamo(id_prestamo_original, nueva_fecha_prestamo)
                        print("Préstamo renovado exitosamente.")
                    elif menu_5 == 2:
                        prestamos = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamos.listar_renovaciones()
                    elif menu_5 == 3:
                        break
                    else:
                        print("Opción no válida")

            elif menu == 6:
                while True:
                    menu_6 = int(input("""
                    1. Generar reporte por tipo de usuarios 
                    2. Generar reporte de préstamos por día
                    3. Generar reporte de devoluciones por día
                    4.Volver al menú principal
                    Ingrese su opción: """))
                    if menu_6 == 1:
                        tipo_usuario = input("Ingrese el tipo de usuario para ver el reporte(alumno/docente):")
                        mi_biblioteca.reporte_tipo_usuario(tipo_usuario)
                    if menu_6 == 2:
                        fecha_prestamo = input("Ingrese la fecha para el reporte de préstamos (YYYY-MM-DD): ")
                        mi_biblioteca.reporte_prestamos_dia(fecha_prestamo)
                    if menu_6 == 3:
                        fecha_devolucion = input("Ingrese la fecha para el reporte de devoluciones (YYYY-MM-DD): ")
                        mi_biblioteca.reporte_devoluciones_dia(fecha_devolucion)
                    elif menu_6 == 4:
                        break
            
            elif menu == 7:
                print("Saliendo del sistema...")
                break
            
            else:
                print("Opción no válida")

        mi_biblioteca.cerrar_conexion()
        print("¡Hasta luego!")

# Ejecutar el menú de la biblioteca
Biblioteca.MenuBiblioteca()

