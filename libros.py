class Libros:
    def __init__(self, isbn_libro: int, genero: str, titulo: str, autor: str, stock: int, idioma: str, conexion, cursor):
        self.isbn_libro = isbn_libro
        self.genero = genero
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.idioma = idioma
        self.conexion = conexion
        self.cursor = cursor

    def agregar_libro(self):
        sql = "INSERT INTO libros (isbn_libro, genero, titulo, autor, stock, idioma) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.isbn_libro, self.genero, self.titulo, self.autor, self.stock, self.idioma)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_libro(self, isbn_libro: int):
        sql = "DELETE FROM Libros WHERE ISBN_Libro = %s"
        self.cursor.execute(sql, (isbn_libro,))
        self.conexion.commit()

    def listar_libros_existentes(self):
        sql = "SELECT * FROM Libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        print("------|Los libros existentes son|--------")
        for libro in libros:
            isbn_libro, genero, titulo, autor, stock, idioma = libro
            print(f"ISBN_Libro: {isbn_libro}, Genero: {genero}, Titulo: {titulo}, Autor: {autor}, Stock: {stock}, Idioma: {idioma}")

            