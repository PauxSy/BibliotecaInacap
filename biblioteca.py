from datetime import date, timedelta
import os
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
                time.sleep(2)
                Biblioteca.limpiar_pantalla()

        except mysql.connector.Error as e:
            print(f'Error al conectar a la base de datos: {e}')
    
    def limpiar_pantalla():
        if os.name == 'posix':  # Linux y macOS
            _ = os.system('clear')
        else:  # Windows
            _ = os.system('cls')
            
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
        host = input("Host (localhost): ")
        user = input("Usuario (root): ")
        password = input("Contraseña: ")
        port = input("Puerto (3306):")
        database = input("Database (PROYECTOFINAL): ")

        # Conectar a la base de datos
        mi_biblioteca = Biblioteca(host, user, password, port, database)
        multa = Multas(None,None,None,None,mi_biblioteca,valor_diario_multa=1000)
        usuario = Usuarios(None,None,None,None,None,None,mi_biblioteca,mi_biblioteca.cursor)


        while True:
            # Mostrar el menú principal 
            menu = int(input("""
            [ Sistema Biblioteca Inacap ]
            
            1. Gestionar Libros
            2. Gestionar Usuarios
            3. Gestionar Préstamos
            4. Gestionar Devoluciones
            5. Gestionar Renovaciones
            6. Gestionar multas
            7. Generar Reporte
            8. Salir del Sistema
            
            Ingrese su opción: """))

            if menu == 1:
                Biblioteca.limpiar_pantalla()
                while True:
                    # Menú de gestión de libros
                    menu_1 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Libros - 

                    1. Ingresar un Libro
                    2. Eliminar un Libro
                    3. Listar libros existentes
                    4. Volver al menú principal
                    
                    Ingrese su opción: """))
                    if menu_1 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Ingresar Libro]")
                        print(" ")
                        print("Ingrese los datos del libro a guardar:\n")
                        isbn_libro = int(input("Ingrese el ISBN del libro: "))
                        genero = input("Ingrese el género: ")
                        titulo = input("Ingrese el título: ")
                        autor = input("Ingrese el autor: ")
                        stock = int(input("Ingrese el stock: "))
                        idioma = input("Ingrese el idioma: ")
                        nuevo_libro = Libros(isbn_libro, genero, titulo, autor, stock, idioma, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        nuevo_libro.agregar_libro()
                        print(" ")
                        print("Libro agregado exitosamente.")
                    elif menu_1 == 2:
                        Biblioteca.limpiar_pantalla()
                        print("[Eliminar Libro]")
                        print(" ")
                        isbn_libro = int(input("Ingrese el ISBN del libro a eliminar: "))
                        libro_a_eliminar = Libros(isbn_libro, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        libro_a_eliminar.eliminar_libro(isbn_libro)
                        print(" ")
                        print("Libro eliminado exitosamente.")
                    elif menu_1 == 3:
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Libros Existentes]")
                        print(" ")
                        libros = Libros(None, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        libros.listar_libros_existentes()
                    elif menu_1 == 4:
                        Biblioteca.limpiar_pantalla()
                        break
                    else:
                        print("Opción no válida")

            elif menu == 2:
                Biblioteca.limpiar_pantalla()
                while True:
                    # Menú de gestión de usuarios
                    menu_2 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Usuarios - 
                        
                    1. Ingresar un Usuario
                    2. Eliminar un Usuario
                    3. Listar usuarios existentes
                    4. Buscar por rut 
                    5. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_2 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Ingresar Usuario]")
                        print(" ")
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
                        Biblioteca.limpiar_pantalla()
                        print("[Eliminar Usuario]")
                        print(" ")
                        rut_usuario = input("Ingrese el RUT del usuario a eliminar: ")
                        eliminar_usuario = Usuarios(rut_usuario, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        eliminar_usuario.eliminar_usuario(rut_usuario)
                        print("Usuario eliminado exitosamente.")
                    elif menu_2 == 3:
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Usuarios existentes]")
                        print(" ")
                        usuarios_bsd = Usuarios(None, None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        usuarios_bsd.listar_usuarios_existentes()
                    elif menu_2 == 4:
                        Biblioteca.limpiar_pantalla()
                        break
                    else:
                        print("Opción no válida")

            elif menu == 3:
                Biblioteca.limpiar_pantalla()
                while True:
                    # Menú de gestión de préstamos
                    menu_3 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                       - Gestión de Préstamos - 
                        
                    1. Ingresar un préstamo
                    2. Listar préstamos existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_3 == 1:
                        Biblioteca.limpiar_pantalla()                      
                        print("[Ingresar Préstamo]")
                        print(" ")
                        print("Ingrese los datos del préstamo a guardar:\n")
                        rut_usuario = input("Ingrese el RUT del usuario: ")
                        #multa.generar_multa()
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
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Préstamos existentes]")
                        print(" ")
                        prestamo = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamo.listar_prestamos()
                    elif menu_3 == 3:
                        Biblioteca.limpiar_pantalla()
                        break
                    else:
                        print("Opción no válida")

            elif menu == 4:
                Biblioteca.limpiar_pantalla()
                while True:
                    # Menú de gestión de devoluciones
                    menu_4 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Devoluciones - 
                        
                    1. Registrar una devolución
                    2. Listar devoluciones existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_4 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Registrar Devolucion]")
                        print(" ")
                        print("Ingrese los datos de la devolución a guardar:\n")
                        id_prestamo = int(input("Ingrese el ID del préstamo: "))
                        fecha_devolucion = input("Ingrese la fecha de la devolución (YYYY-MM-DD): ")
                        fecha_devolucion = date.fromisoformat(fecha_devolucion)
                        estado_devolucion = 'Pendiente'  # estado_devolucion: Pendiente - Devuelto
                        nueva_devolucion = Devoluciones(id_prestamo, fecha_devolucion, estado_devolucion, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        nueva_devolucion.registrar_devoluciones()
                        print("Devolución realizada con éxito.")
                    elif menu_4 == 2:
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Devoluciones Existentes]")
                        print(" ")
                        devolucion = Devoluciones(None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        devolucion.listar_devoluciones()
                    elif menu_4 == 3:
                        Biblioteca.limpiar_pantalla()
                        break
                    else:
                        print("Opción no válida")

            elif menu == 5:
                Biblioteca.limpiar_pantalla()
                while True:
                    menu_5 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Renovaciones - 
                    1. Renovar un préstamo
                    2. Listar renovaciones existentes
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    if menu_5 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Renovar Préstamo]")
                        print(" ")
                        id_prestamo_original = int(input("Ingrese el ID del préstamo original: "))
                        multa.generar_multa()
                        if multa.comprobar_multas_re(id_prestamo_original):
                            continue
                        nueva_fecha_prestamo = date.today()
                        prestamos = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamos.renovar_prestamo(id_prestamo_original, nueva_fecha_prestamo)
                        print("Préstamo renovado exitosamente.")
                    elif menu_5 == 2:
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Renovaciones Existentes]")
                        print(" ")
                        prestamos = Prestamos(None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                        prestamos.listar_renovaciones()
                    elif menu_5 == 3:
                        Biblioteca.limpiar_pantalla()
                        break
                    else:
                        print("Opción no válida")

            elif menu == 6:
                while True:
                    multa.generar_multa()
                    menu_6 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Multas - 
                                       
                    1. Registrar Pago de Multas 
                    2. Listar Registro de Multas
                    3. Volver al menú principal
                    Ingrese su opción: """))
                    
                    if menu_6 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Registrar Pago de Multas]")
                        print(" ")
                        rut_usuario = input("Ingrese el Rut del usuario: ")
                        multa.pago_multa(rut_usuario)
                        
                    elif menu_6 == 2:
                        Biblioteca.limpiar_pantalla()
                        print("[Listar Multas]")
                        print(" ")
                        multa.listar_multas()
                        
                    elif menu_6 == 3:
                        Biblioteca.limpiar_pantalla()
                        break
                    
                    print("|----------------------------------------------------------------------------------------------------------------------------|")

                    
                    
            elif menu == 7:
                while True:
                    Biblioteca.limpiar_pantalla()
                    menu_7 = int(input("""
                    [ Sistema Biblioteca Inacap ]
                        - Gestión de Reportes - 
                                       
                    1. Generar reporte por tipo de usuarios 
                    2. Generar reporte de préstamos por día
                    3. Generar reporte de devoluciones por día
                    4.Volver al menú principal
                    Ingrese su opción: """))
                    if menu_7 == 1:
                        Biblioteca.limpiar_pantalla()
                        print("[Generar Reporte por tipo de Usuarios]")
                        print(" ")
                        tipo_usuario = input("Ingrese el tipo de usuario para ver el reporte(alumno/docente):")
                        mi_biblioteca.reporte_tipo_usuario(tipo_usuario)
                    if menu_7 == 2:
                        Biblioteca.limpiar_pantalla()
                        print("[Generar Reporte de Préstamos por día]")
                        print(" ")
                        fecha_prestamo = input("Ingrese la fecha para el reporte de préstamos (YYYY-MM-DD): ")
                        mi_biblioteca.reporte_prestamos_dia(fecha_prestamo)
                    if menu_7 == 3:
                        Biblioteca.limpiar_pantalla()
                        print("[Generar reporte Devoluciones por día]")
                        print(" ")
                        fecha_devolucion = input("Ingrese la fecha para el reporte de devoluciones (YYYY-MM-DD): ")
                        mi_biblioteca.reporte_devoluciones_dia(fecha_devolucion)
                    elif menu_7 == 4:
                        break
                    

                    
                        
                    
                    
            
            elif menu == 8:
                print("Saliendo del sistema...")
                time.sleep(2)
                break
            
            else:
                print("Opción no válida")

        mi_biblioteca.cerrar_conexion()
        print("¡Hasta luego!")

# Ejecutar el menú de la biblioteca
Biblioteca.MenuBiblioteca()

