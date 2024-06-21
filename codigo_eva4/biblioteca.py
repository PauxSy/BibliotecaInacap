import mysql.connector

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