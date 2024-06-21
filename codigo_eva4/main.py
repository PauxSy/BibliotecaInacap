import biblioteca, usuarios, prestamos, devoluciones, multas
from libros import Libros
from datetime import datetime, date
import mysql.connector

print("Bienvenido al sistema\n")
print("Ingrese los datos de su base de datos\n")

host = input("Ingrese el host: ")
user = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")
port = input("Ingrese el puerto: ")
database = input("Ingrese el nombre de la base de datos: ")

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database
)
mi_biblioteca = biblioteca.Biblioteca(host, user, password,port,database)

#multas.multar_devolucion_fuera_de_plazo(host,user,password,port,database)

menu = int(input("""
1. Gestionar Libros
2. Gestionar Usuarios
3. Gestionar Prestamos
4. Gestionar Devoluciones
Ingrese su opción: """))

if menu == 1 or menu == 2 or menu == 3 or menu == 4:
    if menu == 1:
        menu_1 = int(input("""
        1. Ingresar un Libro
        2. Eliminar un Libro
        3. Listar libros existentes
        Ingrese su opción: """))

        if menu_1 == 1:
            print("Ingrese los datos del libro a guardar:\n")
            isbn_libro = int(input("Ingrese el ISBN del libro: "))
            genero = input("Ingrese el género: ")
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            stock = int(input("Ingrese el stock: "))
            idioma = input("Ingrese el idioma: ")

            
        if menu_1 == 2:
            isbn_libro = int(input("Ingrese el ISBN del libro a eliminar: "))
            libros.eliminar_libro(isbn_libro)

        if menu_1 == 3:
            mi_biblioteca.listar_libros_existentes()

    if menu == 2:
        menu_2 = int(input("""
        1. Ingresar un Usuario
        2. Eliminar un Usuario
        3. Listar usuarios existentes
        Ingrese su opción: """))

        if menu_2 == 1:
            print("Ingrese los datos del usuario a guardar:\n")
            Rut_Usuario = input("Ingrese el RUT del usuario: ")
            Tipo_Usuario = input("Ingrese el tipo de usuario: ")
            Nombre = input("Ingrese el nombre del usuario: ")
            Apellido = input("Ingrese el apellido del usuario: ")
            Email = input("Ingrese el correo del usuario: ")
            Celular = int(input("Ingrese el número de celular del usuario: "))

            nuevo_usuario = usuarios(Rut_Usuario, Tipo_Usuario, Nombre, Apellido, Email, Celular)
            mi_biblioteca.agregar_usuario(nuevo_usuario)

        if menu_2 == 2:
            Rut_Usuario = input("Ingrese el RUT del usuario a eliminar: ")
            mi_biblioteca.eliminar_usuario(Rut_Usuario)

        if menu_2 == 3:
            mi_biblioteca.listar_usuarios_existentes()

    if menu == 3:
        menu_3 = int(input("""
        1. Ingresar un préstamo
        2. Listar préstamos existentes
        Ingrese su opción: """))

        if menu_3 == 1:
            print("Ingrese los datos del préstamo a guardar:\n")
            ID_Prestamo = int(input("Ingrese el ID del préstamo: "))
            Rut_Usuario = input("Ingrese el RUT del usuario: ")
            ISBN_Libro = int(input("Ingrese el ISBN del libro: "))
            Tipo_De_Prestamo = input("Ingrese el tipo de préstamo: ")
            Estado_Prestamo = input("Ingrese el estado del préstamo: ")
            Fecha_Prestamo = input("Ingrese la fecha del préstamo (YYYY-MM-DD): ")
            Fecha_Prestamo = date.fromisoformat(Fecha_Prestamo)

            nuevo_prestamo = prestamos(ID_Prestamo, Rut_Usuario, ISBN_Libro, Tipo_De_Prestamo, Estado_Prestamo, Fecha_Prestamo)
            mi_biblioteca.agregar_prestamo(nuevo_prestamo)

        if menu_3 == 2:
            mi_biblioteca.listar_prestamos()

    if menu == 4:
        menu_4 = int(input("""
        1. Registrar una devolución
        2. Listar devoluciones existentes
        Ingrese su opción: """))

        if menu_4 == 1:
            print("Ingrese los datos de la devolución a guardar:\n")
            ID_Devolucion = int(input("Ingrese el ID de la devolución: "))
            ID_Prestamo = int(input("Ingrese el ID del préstamo: "))
            Fecha_Devolucion = input("Ingrese la fecha de la devolución (YYYY-MM-DD): ")
            Fecha_Devolucion = date.fromisoformat(Fecha_Devolucion)
            Estado_Devolucion = input("Ingrese el estado de la devolución: ")

            nueva_devolucion = devoluciones(ID_Devolucion, ID_Prestamo, Fecha_Devolucion, Estado_Devolucion)
            mi_biblioteca.registrar_devolucion(nueva_devolucion)

        if menu_4 == 2:
            mi_biblioteca.listar_devoluciones()
else:
    print("El valor ingresado no es correcto")
    
    
    