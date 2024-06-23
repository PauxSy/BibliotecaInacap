import biblioteca
from devoluciones import Devoluciones
from multas import Multas
from prestamos import Prestamos
from usuarios import Usuarios
from libros import Libros
from datetime import date
import mysql.connector

def MenuBiblioteca():
    print("Bienvenido al sistema\n")
    print("Ingrese los datos de su base de datos\n")

    host = input("Ingrese el host (localhost): ")
    user = input("Ingrese el usuario (root): ")
    password = input("Ingrese la contraseña (0000): ")
    port = input("Ingrese el puerto (3306): ")
    database = input("Ingrese el nombre de la base de datos(PROYECTOFINAL): ")

    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )
    mi_biblioteca = biblioteca.Biblioteca(host, user, password, port, database)

    while True:
        # Mostrar el menú principal
        menu = int(input("""
        1. Gestionar Libros
        2. Gestionar Usuarios
        3. Gestionar Prestamos
        4. Gestionar Devoluciones
        5. Gestionar Renovaciones
        6. Generar  Reporte
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
                    tipo_usuario = input("Ingrese el tipo de usuario: ")
                    nombre = input("Ingrese el nombre del usuario: ")
                    apellido = input("Ingrese el apellido del usuario: ")
                    email = input("Ingrese el correo del usuario: ")
                    celular = int(input("Ingrese el número de celular del usuario: "))

                    nuevo_usuario = Usuarios(rut_usuario, tipo_usuario, nombre, apellido, email, celular, mi_biblioteca.conexion, mi_biblioteca.cursor)
                    nuevo_usuario.agregar_usuario()
                    print("Usuario agregado exitosamente.")

                elif menu_2 == 2:
                    rut_usuario = input("Ingrese el RUT del usuario a eliminar: ")
                    eliminar_usuario = Usuarios(rut_usuario,None, None, None, None, None, mi_biblioteca.conexion, mi_biblioteca.cursor)
                    eliminar_usuario.eliminar_usuario(rut_usuario)
                    print("Usuario eliminado exitosamente.")

                elif menu_2 == 3:
                    usuarios_bsd = Usuarios(None,None,None,None,None,None, mi_biblioteca.conexion, mi_biblioteca.cursor)
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
                    id_prestamo = int(input("Ingrese el ID del préstamo: "))
                    rut_usuario = input("Ingrese el RUT del usuario: ")
                    isbn_libro = int(input("Ingrese el ISBN del libro: "))
                    tipo_de_prestamo = input("Ingrese el tipo de préstamo (Renovación / Prestamo nuevo): ")
                    estado_prestamo = input("Ingrese el estado del préstamo (Vigeten / No Vigente): ")
                    fecha_prestamo = input("Ingrese la fecha del préstamo (YYYY-MM-DD): ")
                    fecha_prestamo = date.fromisoformat(fecha_prestamo)

                    nuevo_prestamo = Prestamos(id_prestamo, rut_usuario, isbn_libro, tipo_de_prestamo, estado_prestamo, fecha_prestamo,mi_biblioteca.conexion, mi_biblioteca.cursor)
                    nuevo_prestamo.agregar_prestamo()
                    print("Prestamo agregado exitosamente.")

                elif menu_3 == 2:
                    prestamo=Prestamos(None,None,None,None,None,None,mi_biblioteca.conexion, mi_biblioteca.cursor)
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
                    id_devolucion = int(input("Ingrese el ID de la devolución: "))
                    id_prestamo = int(input("Ingrese el ID del préstamo: "))
                    fecha_devolucion = input("Ingrese la fecha de la devolución (YYYY-MM-DD): ")
                    fecha_devolucion = date.fromisoformat(fecha_devolucion)
                    estado_devolucion = input("Ingrese el estado de la devolución(Pendiente - Devuelto): ")

                    nueva_devolucion = Devoluciones(id_devolucion, id_prestamo, fecha_devolucion, estado_devolucion,mi_biblioteca.conexion, mi_biblioteca.cursor)
                    nueva_devolucion.registrar_devoluciones()
                    print("Devolución agregado exitosamente.")

                elif menu_4 == 2:
                    devolucion=Devoluciones(None,None,None,None,mi_biblioteca.conexion, mi_biblioteca.cursor)
                    devolucion.listar_devoluciones()

                elif menu_4 == 3:
                    break

                else:
                    print("Opción no válida")
        elif menu == 5:
            pass

        elif menu == 6:
            pass

        elif menu == 7:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida")

    conexion.close()
    print("¡Hasta luego!")


MenuBiblioteca()

# hooiii
        