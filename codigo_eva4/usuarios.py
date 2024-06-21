class Usuarios:
    def __init__(self, rut_usuario: str, tipo_usuario: str, nombre: str, apellido: str, email: str, celular: int):
        self.rut_usuario = rut_usuario
        self.tipo_usuario = tipo_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        
        
    def agregar_usuario(self, usuario):
        sql = "INSERT INTO Usuarios (rut_usuario, tipo_usuario, nombre, apellido, email, celular) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (usuario.rut_usuario, usuario.tipo_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.celular)
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