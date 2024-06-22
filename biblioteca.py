import mysql.connector

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
                print(" ")
                print('¡Conexión exitosa!')
        except mysql.connector.Error as e:
            print(f'Error al conectar a la base de datos: {e}')

    def ejecutar_consulta(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conexion.commit()
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()
        print('Conexión cerrada.')