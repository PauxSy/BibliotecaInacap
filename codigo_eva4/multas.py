from datetime import datetime
import biblioteca

class Multas:
    def __init__(self, id_devolucion: int, estado_multa: str, monto_deuda: int, dias_retraso: int):
        self.id_devolucion = id_devolucion
        self.estado_multa = estado_multa
        self.monto_deuda = monto_deuda
        self.dias_retraso = dias_retraso

def multar_devolucion_fuera_de_plazo(host, user, password, port, database):
    fecha_actual = datetime.now().date()
    db = biblioteca.Biblioteca(host, user, password, port, database)

    try:
        cursor = db.cursor
        # Seleccionar todas las devoluciones con fecha_devolucion mayor a la fecha actual y sin multa generada
        sql = """
        SELECT id FROM devoluciones
        WHERE fecha_devolucion > %s
        """
        cursor.execute(sql, (fecha_actual,))
        resultados = cursor.fetchall()
        
        print(resultados)
       # if resultados:
            # Generar multas para los resultados encontrados
        #    for row in resultados:
         #       id_devolucion = row[0]
          #      sql_update = """
           ##    SET multa_generada = TRUE
             #   WHERE id = %s
              #  """
               # cursor.execute(sql_update, (id_devolucion,))
        
        # Confirmar los cambios
        db.conn.commit()
    finally:
        db.cerrar_conexion()
