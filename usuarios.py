class Usuarios:
    def __init__(self, rut_usuario: str, tipo_usuario: str, nombre: str, apellido: str, email: str, celular: int,conexion, cursor):
        self.rut_usuario = rut_usuario
        self.tipo_usuario = tipo_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.conexion = conexion
        self.cursor = cursor
        
        
    def agregar_usuario(self):
        sql = "INSERT INTO Usuarios (rut_usuario, tipo_usuario, nombre, apellido, email, celular) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.rut_usuario, self.tipo_usuario, self.nombre, self.apellido, self.email, self.celular)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_usuario(self, rut_usuario: str):
        sql = "DELETE FROM Usuarios WHERE rut_usuario = %s"
        self.cursor.execute(sql, (rut_usuario,))
        self.conexion.commit()

    def listar_usuarios_existentes(self):
        sql = "SELECT * FROM Usuarios"
        self.cursor.execute(sql)
        usuarios = self.cursor.fetchall()
        print("------|Los usuarios existentes son|--------")
        for usuario in usuarios:
            rut_usuario, tipo_usuario, nombre, apellido, email, celular = usuario
            print(f"rut_usuario: {rut_usuario}, tipo_usuario: {tipo_usuario}, nombre: {nombre}, apellido: {apellido}, email: {email}, celular: {celular}")

    def info_personal(self, rut_usuario):
        sql = "SELECT * FROM USUARIOS WHERE RUT_USUARIO = %s"
        self.cursor.execute(sql, (rut_usuario,))
        info_usuario = self.cursor.fetchone()
        print("------------[Información de Usuario]-------------")
        print("Rut:          ",info_usuario[0])
        print("Tipo Usuario: ",info_usuario[1])
        print("Nombre:       ",info_usuario[2])
        print("Apellido:     ",info_usuario[3])
        print("Email:        ",info_usuario[4])
        print("Celular:      ",info_usuario[5])
        print("---------------------------------------------------")
        

    def hist_prestamos_usuario(self, rut_usuario):
        # Consulta SQL para obtener el historial de préstamos del usuario
        sql = """
        SELECT P.ISBN_LIBRO, L.TITULO, P.ESTADO_PRESTAMO, P.FECHA_PRESTAMO, D.FECHA_DEVOLUCION
        FROM PRESTAMOS P
        JOIN DEVOLUCIONES D ON P.ID_PRESTAMO = D.ID_PRESTAMO
        JOIN LIBROS L ON P.ISBN_LIBRO = L.ISBN_LIBRO
        WHERE P.RUT_USUARIO = %s
        ORDER BY D.FECHA_DEVOLUCION DESC
        LIMIT 5;
        """
        self.cursor.execute(sql, (rut_usuario,))
        historial_prestamos = self.cursor.fetchall()

        # Consulta para obtener el nombre y apellido del usuario
        sql2 = "SELECT NOMBRE, APELLIDO FROM USUARIOS WHERE RUT_USUARIO = %s"
        self.cursor.execute(sql2, (rut_usuario,))
        name = self.cursor.fetchone()

        # Imprimir el historial de préstamos en el formato solicitado
        print("------------[ Historial de Préstamos ]-------------")
        print("Rut: ", rut_usuario)
        print("Nombre: ", name[0], "", name[1])
        for prestamo in historial_prestamos:
            isbn, titulo, estado_prestamo, fecha_prestamo, fecha_devolucion = prestamo
            print("-----------------------------------------------------")
            print("ISBN: ", isbn)
            print("Título: ", titulo)
            print("Estado Préstamo: ", estado_prestamo)
            print("Fecha Préstamo: ", fecha_prestamo)
            print("Fecha de Devolución: ", fecha_devolucion)
        print("-----------------------------------------------------")


    def hist_deuda_usuarios(self,rut_usuario):
        sql = "SELECT NOMBRE, APELLIDO FROM USUARIOS WHERE RUT_USUARIO = %s"
        self.cursor.execute(sql, (rut_usuario,))
        name = self.cursor.fetchone()
        
        sql2 = '''SELECT P.ID_PRESTAMO, L.TITULO,D.FECHA_DEVOLUCION, M.MONTO_DEUDA , M.ESTADO_MULTA
                  FROM MULTAS M
                  JOIN DEVOLUCIONES D ON M.ID_DEVOLUCION = D.ID_DEVOLUCION
                  JOIN PRESTAMOS P ON D.ID_PRESTAMO = P.ID_PRESTAMO
                  JOIN LIBROS L ON P.ISBN_LIBRO = L.ISBN_LIBRO
                  WHERE P.RUT_USUARIO = %s
                  GROUP BY M.ESTADO_MULTA, P.ID_PRESTAMO, L.TITULO, D.FECHA_DEVOLUCION, M.MONTO_DEUDA;
                  '''
        self.cursor.execute(sql2, (rut_usuario,))
        historial = self.cursor.fetchall()
        print("------------[ Historial de Multas ]-------------")
        print("Rut: ",rut_usuario)
        print("Nombre: ",name[0],"",name[1])
        for i in range(0,len(historial),1):
            print("-----------------------------------------------------")
            x = historial[i]
            print("Id_Prestamo: ",x[0])
            print("Titulo: ",x[1])
            print("Fecha Devolución: ",x[2])
            print("Monto Deuda: ",x[3])
            print("Estado Multa: ",x[4])
            
        print("-----------------------------------------------------")



        