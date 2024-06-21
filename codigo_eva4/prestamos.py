class Prestamo:
    def __init__(self, ID_Prestamo: int, Rut_Usuario: str, ISBN_Libro: int, Tipo_De_Prestamo: str, Estado_Prestamo: str, Fecha_Prestamo: date):
        self.ID_Prestamo = ID_Prestamo
        self.Rut_Usuario = Rut_Usuario
        self.ISBN_Libro = ISBN_Libro
        self.Tipo_De_Prestamo = Tipo_De_Prestamo
        self.Estado_Prestamo = Estado_Prestamo
        self.Fecha_Prestamo = Fecha_Prestamo