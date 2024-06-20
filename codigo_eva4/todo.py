# import mysql.connector
# from datetime import date, timedelta

# class Libro:
#     def __init__(self, ISBN_Libro: int, Genero: str, Titulo: str, Autor: str, Stock: int, Idioma: str):
#         self.ISBN_Libro = ISBN_Libro
#         self.Genero = Genero
#         self.Titulo = Titulo
#         self.Autor = Autor
#         self.Stock = Stock
#         self.Idioma = Idioma

# class Usuario:
#     def __init__(self, Rut_Usuario: str, Tipo_Usuario: str, Nombre: str, Apellido: str, Email: str, Celular: int):
#         self.Rut_Usuario = Rut_Usuario
#         self.Tipo_Usuario = Tipo_Usuario
#         self.Nombre = Nombre
#         self.Apellido = Apellido
#         self.Email = Email
#         self.Celular = Celular

# class Prestamo:
#     def __init__(self, ID_Prestamo: int, Rut_Usuario: str, ISBN_Libro: int, Tipo_De_Prestamo: str, Estado_Prestamo: str, Fecha_Prestamo: date):
#         self.ID_Prestamo = ID_Prestamo
#         self.Rut_Usuario = Rut_Usuario
#         self.ISBN_Libro = ISBN_Libro
#         self.Tipo_De_Prestamo = Tipo_De_Prestamo
#         self.Estado_Prestamo = Estado_Prestamo
#         self.Fecha_Prestamo = Fecha_Prestamo

# class Devolucion:
#     def __init__(self, ID_Devolucion: int, ID_Prestamo: int, Fecha_Devolucion: date, Estado_Devolucion: str):
#         self.ID_Devolucion = ID_Devolucion
#         self.ID_Prestamo = ID_Prestamo
#         self.Fecha_Devolucion = Fecha_Devolucion
#         self.Estado_Devolucion = Estado_Devolucion

# class Multa:
#     def __init__(self, ID_Multa: int, ID_Devolucion: int, Estado_Multa: str, Monto_Deuda: int, Dias_Retraso: int):
#         self.ID_Multa = ID_Multa
#         self.ID_Devolucion = ID_Devolucion
#         self.Estado_Multa = Estado_Multa
#         self.Monto_Deuda = Monto_Deuda
#         self.Dias_Retraso = Dias_Retraso

# class Biblioteca:
    
#     def __init__(self, host, user, password, port, database):
#         self.conexion = mysql.connector.connect(
#             host = host,
#             user = user,
#             password = password,
#             port = port,
#             database = database
#         )
#         self.cursor = self.conexion.cursor()

#     # Métodos para gestionar libros
#     def agregar_libro(self, libro: Libro):
#         sql = "INSERT INTO LIBROS (ISBN_LIBRO, GENERO, TITULO, AUTOR, STOCK, IDIOMA) VALUES (%s, %s, %s, %s, %s, %s)"
#         valores = (libro.ISBN_Libro, libro.Genero, libro.Titulo, libro.Autor, libro.Stock, libro.Idioma)
#         self.cursor.execute(sql, valores)
#         self.conexion.commit()

#     def eliminar_libro(self, ISBN_Libro: int):
#         sql = "DELETE FROM LIBROS WHERE ISBN_LIBRO = %s"
#         self.cursor.execute(sql, (ISBN_Libro,))
#         self.conexion.commit()

#     def listar_libros_existentes(self):
#         sql = "SELECT * FROM LIBROS"
#         self.cursor.execute(sql)
#         libros = self.cursor.fetchall()
#         print("------|Los libros existentes son|--------")
#         for libro in libros:
#             ISBN_Libro, Genero, Titulo, Autor, Stock, Idioma = libro
#             print(f"ISBN_Libro: {ISBN_Libro}, Genero: {Genero}, Titulo: {Titulo}, Autor: {Autor}, Stock: {Stock}, Idioma: {Idioma}")

#     # Métodos para gestionar usuarios
#     def agregar_usuario(self, usuario: Usuario):
#         sql = "INSERT INTO USUARIOS (RUT_USUARIO, TIPO_USUARIO, NOMBRE, APELLIDO, EMAIL, CELULAR) VALUES (%s, %s, %s, %s, %s, %s)"
#         valores = (usuario.Rut_Usuario, usuario.Tipo_Usuario, usuario.Nombre, usuario.Apellido, usuario.Email, usuario.Celular)
#         self.cursor.execute(sql, valores)
#         self.conexion.commit()

#     def eliminar_usuario(self, Rut_Usuario: str):
#         sql = "DELETE FROM USUARIOS WHERE RUT_USUARIO = %s"
#         self.cursor.execute(sql, (Rut_Usuario,))
#         self.conexion.commit()

#     def listar_usuarios_existentes(self):
#         sql = "SELECT * FROM USUARIOS"
#         self.cursor.execute(sql)
#         usuarios = self.cursor.fetchall()
#         print("------|Los usuarios existentes son|--------")
#         for usuario in usuarios:
#             Rut_Usuario, Tipo_Usuario, Nombre, Apellido, Email, Celular = usuario
#             print(f"Rut_Usuario: {Rut_Usuario}, Tipo_Usuario: {Tipo_Usuario}, Nombre: {Nombre}, Apellido: {Apellido}, Email: {Email}, Celular: {Celular}")

#     # Métodos para gestionar préstamos
#     def agregar_prestamo(self, prestamo: Prestamo):
#         sql = "INSERT INTO PRESTAMOS (ID_PRESTAMO, RUT_USUARIO, ISBN_LIBRO, TIPO_DE_PRESTAMO, ESTADO_PRESTAMO, FECHA_PRESTAMO) VALUES (%s, %s, %s, %s, %s, %s)"
#         valores = (prestamo.ID_Prestamo, prestamo.Rut_Usuario, prestamo.ISBN_Libro, prestamo.Tipo_De_Prestamo, prestamo.Estado_Prestamo, prestamo.Fecha_Prestamo)
#         self.cursor.execute(sql, valores)
#         self.conexion.commit()

#     def listar_prestamos(self):
#         sql = "SELECT * FROM PRESTAMOS"
#         self.cursor.execute(sql)
#         prestamos = self.cursor.fetchall()
#         print("------|Los registros de préstamos existentes son|--------")
#         for prestamo in prestamos:
#             ID_Prestamo, Rut_Usuario, ISBN_Libro, Tipo_De_Prestamo, Estado_Prestamo, Fecha_Prestamo = prestamo
#             print(f"ID_Prestamo: {ID_Prestamo}, Rut_Usuario: {Rut_Usuario}, ISBN_Libro: {ISBN_Libro}, Tipo_De_Prestamo: {Tipo_De_Prestamo}, Estado_Prestamo: {Estado_Prestamo}, Fecha_Prestamo: {Fecha_Prestamo}")

#     def buscar_prestamo_por_id(self, id_prestamo):
#         sql = "SELECT * FROM PRESTAMOS WHERE ID_PRESTAMO = %s"
#         self.cursor.execute(sql, (id_prestamo,))
#         prestamo = self.cursor.fetchone()
#         return prestamo

#     # Métodos para gestionar devoluciones
#     def registrar_devolucion(self, devolucion: Devolucion):
#         sql = "INSERT INTO DEVOLUCIONES (ID_DEVOLUCION, ID_PRESTAMO, FECHA_DEVOLUCION, ESTADO_DEVOLUCION) VALUES (%s, %s, %s, %s)"
#         valores = (devolucion.ID_Devolucion, devolucion.ID_Prestamo, devolucion.Fecha_Devolucion, devolucion.Estado_Devolucion)
#         self.cursor.execute(sql, valores)
#         self.conexion.commit()

#         sql_actualizar_prestamo = "UPDATE PRESTAMOS SET ESTADO_PRESTAMO = 'Devuelto' WHERE ID_PRESTAMO = %s"
#         self.cursor.execute(sql_actualizar_prestamo, (devolucion.ID_Prestamo,))
#         self.conexion.commit()

#     def listar_devoluciones(self):
#         sql = "SELECT * FROM DEVOLUCIONES"
#         self.cursor.execute(sql)
#         devoluciones = self.cursor.fetchall()
#         print("------|Los registros de devoluciones existentes son|--------")
#         for devolucion in devoluciones:
#             ID_Devolucion, ID_Prestamo, Fecha_Devolucion, Estado_Devolucion = devolucion
#             print(f"ID_Devolucion: {ID_Devolucion}, ID_Prestamo: {ID_Prestamo}, Fecha_Devolucion: {Fecha_Devolucion}, Estado_Devolucion: {Estado_Devolucion}")

#     # Métodos adicionales requeridos por el sistema de préstamos
#     def calcular_fecha_devolucion(self, fecha_prestamo: date, tipo_usuario: str) -> date:
#         if tipo_usuario == 'docente':
#             return fecha_prestamo + timedelta(days=20)
#         elif tipo_usuario == 'alumno':
#             return fecha_prestamo + timedelta(days=7)
#         else:
#             return None

#     def solicitar_renovacion(self, id_prestamo: int, tipo_usuario: str) -> bool:
#         prestamo = self.buscar_prestamo_por_id(id_prestamo)
#         if not prestamo:
#             return False
        
#         estado_prestamo = prestamo[4]
#         if estado_prestamo != 'Prestado':
#             return False
        
#         fecha_prestamo = prestamo[5]
#         nueva_fecha_devolucion = self.calcular_fecha_devolucion(fecha_prestamo, tipo_usuario)
#         if not nueva_fecha_devolucion:
#             return False
        
#         sql = "UPDATE PRESTAMOS SET FECHA_PRESTAMO = %s WHERE ID_PRESTAMO = %s"
#         self.cursor.execute(sql, (nueva_fecha_devolucion, id_prestamo))
#         self.conexion.commit()
        
#         return True

#     def generar_multa(self, id_prestamo: int, dias_retraso: int) -> bool:
#         prestamo = self.buscar_prestamo_por_id(id_prestamo)
#         if not prestamo:
#             return False
        
#         estado_prestamo = prestamo[4]
#         if estado_prestamo != 'Prestado':
#             return False
        
#         monto_multa = 100 * dias_retraso  # Suponiendo una multa de $100 por día de retraso
        
#         sql = "INSERT INTO MULTAS (ID_PRESTAMO, ESTADO_MULTA, MONTO_DEUDA, DIAS_RETRASO) VALUES (%s, %s, %s, %s)"
#         valores = (id_prestamo, 'Pendiente', monto_multa, dias_retraso)
#         self.cursor.execute(sql, valores)
#         self.conexion.commit()
        
#         return True

#     def pagar_multa(self, id_multa: int) -> bool:
#         sql = "UPDATE MULTAS SET ESTADO_MULTA = 'Pagada' WHERE ID_MULTA = %s"
#         self.cursor.execute(sql, (id_multa,))
#         self.conexion.commit()
#         return True

# # Ejemplo de uso
# if __name__ == "__main__":
#     biblioteca = Biblioteca('localhost', 'root', 'password', 3306, 'biblioteca')

#     # Agregar un libro
#     nuevo_libro = Libro(123456789, 'Ficción', 'El nombre del viento', 'Patrick Rothfuss', 5, 'Español')
#     biblioteca.agregar_libro(nuevo_libro)

#     # Agregar un usuario
#     nuevo_usuario = Usuario('12345678-9', 'alumno', 'Juan', 'Perez', 'juan.perez@email.com', 987654321)
#     biblioteca.agregar_usuario(nuevo_usuario)

#     # Realizar un préstamo
#     fecha_prestamo = date.today()
#     fecha_devolucion = biblioteca.calcular_fecha_devolucion(fecha_prestamo, nuevo_usuario.Tipo_Usuario)
#     nuevo_prestamo = Prestamo(1, nuevo_usuario.Rut_Usuario, nuevo_libro.ISBN_Libro, 'Normal', 'Prestado', fecha_prestamo)
#     biblioteca.agregar_prestamo(nuevo_prestamo)

#     # Registrar una devolución
#     nueva_devolucion = Devolucion(1, nuevo_prestamo.ID_Prestamo, fecha_devolucion, 'Devuelto')
#     biblioteca.registrar_devolucion(nueva_devolucion)

#     # Listar libros existentes
#     biblioteca.listar_libros_existentes()

#     # Listar usuarios existentes
#     biblioteca.listar_usuarios_existentes()

#     # Listar préstamos existentes
#     biblioteca.listar_prestamos()

#     # Listar devoluciones existentes
#     biblioteca.listar_devoluciones()

#     # Solicitar renovación de un préstamo
#     biblioteca.solicitar_renovacion(nuevo_prestamo.ID_Prestamo, nuevo_usuario.Tipo_Usuario)

#     # Generar una multa por retraso
#     biblioteca.generar_multa(nuevo_prestamo.ID_Prestamo, 5)

#     # Pagar una multa existente
#     biblioteca.pagar_multa(1)

#     # Listar préstamos nuevamente para verificar cambios
#     biblioteca.listar_prestamos()

#     # Listar multas existentes
#     sql_multas = "SELECT * FROM MULTAS"
#     biblioteca.cursor.execute(sql_multas)
#     multas = biblioteca.cursor.fetchall()
#     print("------|Las multas existentes son|--------")
#     for multa in multas:
#         ID_Multa, ID_Prestamo, Estado_Multa, Monto_Deuda, Dias_Retraso = multa
#         print(f"ID_Multa: {ID_Multa}, ID_Prestamo: {ID_Prestamo}, Estado_Multa: {Estado_Multa}, Monto_Deuda: {Monto_Deuda}, Dias_Retraso: {Dias_Retraso}")

#     # Cerrar conexión
#     biblioteca.conexion.close()


import mysql.connector
from datetime import date, timedelta

class Libro:
    def __init__(self, ISBN_Libro: int, Genero: str, Titulo: str, Autor: str, Stock: int, Idioma: str):
        self.ISBN_Libro = ISBN_Libro
        self.Genero = Genero
        self.Titulo = Titulo
        self.Autor = Autor
        self.Stock = Stock
        self.Idioma = Idioma

class Usuario:
    def __init__(self, Rut_Usuario: str, Tipo_Usuario: str, Nombre: str, Apellido: str, Email: str, Celular: int):
        self.Rut_Usuario = Rut_Usuario
        self.Tipo_Usuario = Tipo_Usuario
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Email = Email
        self.Celular = Celular

class Prestamo:
    def __init__(self, ID_Prestamo: int, Rut_Usuario: str, ISBN_Libro: int, Tipo_De_Prestamo: str, Estado_Prestamo: str, Fecha_Prestamo: date):
        self.ID_Prestamo = ID_Prestamo
        self.Rut_Usuario = Rut_Usuario
        self.ISBN_Libro = ISBN_Libro
        self.Tipo_De_Prestamo = Tipo_De_Prestamo
        self.Estado_Prestamo = Estado_Prestamo
        self.Fecha_Prestamo = Fecha_Prestamo

class Devolucion:
    def __init__(self, ID_Devolucion: int, ID_Prestamo: int, Fecha_Devolucion: date, Estado_Devolucion: str):
        self.ID_Devolucion = ID_Devolucion
        self.ID_Prestamo = ID_Prestamo
        self.Fecha_Devolucion = Fecha_Devolucion
        self.Estado_Devolucion = Estado_Devolucion

class Biblioteca:
    
    def __init__(self, host, user, password, port, database):
        self.conexion = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            port = port,
            database = database
        )
        self.cursor = self.conexion.cursor()

    #------------------------------------|LIBRO|----------------------------------------------
    def agregar_libro(self, libro: Libro):
        sql = "INSERT INTO Libros (ISBN_Libro, Genero, Titulo, Autor, Stock, Idioma) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (libro.ISBN_Libro, libro.Genero, libro.Titulo, libro.Autor, libro.Stock, libro.Idioma)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_libro(self, ISBN_Libro: int):
        sql = "DELETE FROM Libros WHERE ISBN_Libro = %s"
        self.cursor.execute(sql, (ISBN_Libro,))
        self.conexion.commit()

    def listar_libros_existentes(self):
        sql = "SELECT * FROM Libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        print("------|Los libros existentes son|--------")
        for libro in libros:
            ISBN_Libro, Genero, Titulo, Autor, Stock, Idioma = libro
            print(f"ISBN_Libro: {ISBN_Libro}, Genero: {Genero}, Titulo: {Titulo}, Autor: {Autor}, Stock: {Stock}, Idioma: {Idioma}")

    #----------------------------------|USUARIO|----------------------------------------------------
    def agregar_usuario(self, usuario: Usuario):
        sql = "INSERT INTO Usuarios (RUT_Usuario, TIPO_Usuario, NOMBRE, APELLIDO, EMAIL, CELULAR) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (usuario.Rut_Usuario, usuario.Tipo_Usuario, usuario.Nombre, usuario.Apellido, usuario.Email, usuario.Celular)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_usuario(self, Rut_Usuario: str):
        sql = "DELETE FROM Usuarios WHERE RUT_Usuario = %s"
        self.cursor.execute(sql, (Rut_Usuario,))
        self.conexion.commit()

    def listar_usuarios_existentes(self):
        sql = "SELECT * FROM Usuarios"
        self.cursor.execute(sql)
        usuarios = self.cursor.fetchall()
        print("------|Los usuarios existentes son|--------")
        for usuario in usuarios:
            Rut_Usuario, Tipo_Usuario, Nombre, Apellido, Email, Celular = usuario
            print(f"Rut_Usuario: {Rut_Usuario}, Tipo_Usuario: {Tipo_Usuario}, Nombre: {Nombre}, Apellido: {Apellido}, Email: {Email}, Celular: {Celular}")

    #----------------------------------|PRESTAMOS|---------------------------------------------------
    def agregar_prestamo(self, prestamo: Prestamo):
        sql = "INSERT INTO Prestamos (ID_PRESTAMO, RUT_USUARIO, ISBN_LIBRO, TIPO_DE_PRESTAMO, ESTADO_PRESTAMO, FECHA_PRESTAMO) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (prestamo.ID_Prestamo, prestamo.Rut_Usuario, prestamo.ISBN_Libro, prestamo.Tipo_De_Prestamo, prestamo.Estado_Prestamo, prestamo.Fecha_Prestamo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def registrar_devolucion(self, devolucion: Devolucion):
        sql = "INSERT INTO Devoluciones (ID_DEVOLUCION, ID_PRESTAMO, FECHA_DEVOLUCION, ESTADO_DEVOLUCION) VALUES (%s, %s, %s, %s)"
        valores = (devolucion.ID_Devolucion, devolucion.ID_Prestamo, devolucion.Fecha_Devolucion, devolucion.Estado_Devolucion)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

        sql_actualizar_prestamo = "UPDATE Prestamos SET ESTADO_PRESTAMO = 'Devuelto' WHERE ID_PRESTAMO = %s"
        self.cursor.execute(sql_actualizar_prestamo, (devolucion.ID_Prestamo,))
        self.conexion.commit()

    def listar_prestamos(self):
        sql = "SELECT * FROM Prestamos"
        self.cursor.execute(sql)
        prestamos = self.cursor.fetchall()
        print("------|Los registros de prestamos existentes son|--------")
        for prestamo in prestamos:
            ID_Prestamo, Rut_Usuario, ISBN_Libro, Tipo_De_Prestamo, Estado_Prestamo, Fecha_Prestamo = prestamo
            print(f"ID_Prestamo: {ID_Prestamo}, Rut_Usuario: {Rut_Usuario}, ISBN_Libro: {ISBN_Libro}, Tipo_De_Prestamo: {Tipo_De_Prestamo}, Estado_Prestamo: {Estado_Prestamo}, Fecha_Prestamo: {Fecha_Prestamo}")

    def listar_devoluciones(self):
        sql = "SELECT * FROM Devoluciones"
        self.cursor.execute(sql)
        devoluciones = self.cursor.fetchall()
        print("------|Los registros de devoluciones existentes son|--------")
        for devolucion in devoluciones:
            ID_Devolucion, ID_Prestamo, Fecha_Devolucion, Estado_Devolucion = devolucion
            print(f"ID_Devolucion: {ID_Devolucion}, ID_Prestamo: {ID_Prestamo}, Fecha_Devolucion: {Fecha_Devolucion}, Estado_Devolucion: {Estado_Devolucion}")

print("Bienvenido al sistema\n")
print("Ingrese los datos de su base de datos\n")

host = input("Ingrese el host: ")
user = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")
port = input("Ingrese el puerto: ")
database = input("Ingrese el nombre de la base de datos: ")
mi_biblioteca = Biblioteca(host, user, password, port, database)

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
            ISBN_Libro = int(input("Ingrese el ISBN del libro: "))
            Genero = input("Ingrese el género: ")
            Titulo = input("Ingrese el título: ")
            Autor = input("Ingrese el autor: ")
            Stock = int(input("Ingrese el stock: "))
            Idioma = input("Ingrese el idioma: ")

            nuevo_libro = Libro(ISBN_Libro, Genero, Titulo, Autor, Stock, Idioma)
            mi_biblioteca.agregar_libro(nuevo_libro)

        if menu_1 == 2:
            ISBN_Libro = int(input("Ingrese el ISBN del libro a eliminar: "))
            mi_biblioteca.eliminar_libro(ISBN_Libro)

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

            nuevo_usuario = Usuario(Rut_Usuario, Tipo_Usuario, Nombre, Apellido, Email, Celular)
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

            nuevo_prestamo = Prestamo(ID_Prestamo, Rut_Usuario, ISBN_Libro, Tipo_De_Prestamo, Estado_Prestamo, Fecha_Prestamo)
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

            nueva_devolucion = Devolucion(ID_Devolucion, ID_Prestamo, Fecha_Devolucion, Estado_Devolucion)
            mi_biblioteca.registrar_devolucion(nueva_devolucion)

        if menu_4 == 2:
            mi_biblioteca.listar_devoluciones()
else:
    print("El valor ingresado no es correcto")
    
    
    
    print("hola Fran")
    print()