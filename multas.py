from datetime import datetime
#from biblioteca import Biblioteca  # Asegúrate de importar la clase Biblioteca si no está en este archivo

class Multas:
    def __init__(self, id_devolucion, estado_multa, monto_deuda, dias_retraso, biblioteca, valor_diario_multa):
        self.id_devolucion = id_devolucion
        self.estado_multa = estado_multa
        self.monto_deuda = monto_deuda
        self.dias_retraso = dias_retraso
        self.biblioteca = biblioteca
        self.valor_diario_multa = 1000

    def generar_multa(self):
        fecha_actual = datetime.now().date()
        
        # Obtener el cursor de la biblioteca
        cursor = self.biblioteca.conexion.cursor()
        
        try:
            # Consulta para seleccionar devoluciones atrasadas
            devo_atrasadas = """SELECT ID_DEVOLUCION, FECHA_DEVOLUCION FROM DEVOLUCIONES 
                                WHERE FECHA_DEVOLUCION < %s AND ESTADO_DEVOLUCION = "PENDIENTE" 
                             """
            cursor.execute(devo_atrasadas, (fecha_actual,))
        
            resultados = cursor.fetchall()  # Usar cursor directamente
            
            id_dev_atrasadas = []
            fecha_dev_atrasadas = []
            dias_a = []

            for i, tupla in enumerate(resultados):
                id_devolucion = tupla[0]
                fecha_devolucion = tupla[1]
                # Convertir fecha_devolucion a datetime.date si es necesario
                if isinstance(fecha_devolucion, datetime):
                    fecha_devolucion = fecha_devolucion.date()
                
                # Calcular días de retraso
                dias_atraso = (fecha_actual - fecha_devolucion).days
                               
                id_dev_atrasadas.append(id_devolucion)
                fecha_dev_atrasadas.append(fecha_devolucion)
                dias_a.append(dias_atraso)
            
                
                print("IDs de devolución atrasadas:", id_dev_atrasadas)
                print("Fechas de devolución atrasadas:", fecha_dev_atrasadas)
                print("Días de retraso:", dias_a)
                
                                 
                
            for i in range(len(id_dev_atrasadas)):
                valor_multa = dias_a[i] * self.valor_diario_multa
                cursor.execute("SELECT COUNT(*) FROM MULTAS WHERE ID_DEVOLUCION = %s", (id_dev_atrasadas[i],))
                existe_multa = cursor.fetchone()[0]  
                if existe_multa:
                    actualizar_multa = """UPDATE MULTAS 
                                          SET ESTADO_MULTA = 'Pendiente', 
                                              MONTO_DEUDA = %s, 
                                              DIAS_RETRASO = %s 
                                          WHERE ID_DEVOLUCION = %s"""
                                          
                    cursor.execute(actualizar_multa, (valor_multa, dias_a[i],id_dev_atrasadas[i]))
                    print("ID_devolucion_atrasada",id_dev_atrasadas[i])
        
                else:
                    registrar_multa = """INSERT INTO MULTAS (ID_DEVOLUCION, ESTADO_MULTA, MONTO_DEUDA, DIAS_RETRASO)
                                     VALUES (%s, %s, %s, %s)"""

                    cursor.execute(registrar_multa, (id_dev_atrasadas[i],'Pendiente', valor_multa, dias_a[i]))
                    
       
        # Confirmar los cambios

            # Confirmar los cambios en la base de datos
            self.biblioteca.conexion.commit()
            
        except Exception as e:
            print(f"Error al generar multas: {e}")
            # Si hay un error, hacer rollback de la transacción
            self.biblioteca.conexion.rollback()

        finally:
            # Cerrar el cursor y la conexión
            self.biblioteca.cursor.close()
from datetime import datetime
#from biblioteca import Biblioteca  # Asegúrate de importar la clase Biblioteca si no está en este archivo

class Multas:
    def __init__(self, id_devolucion, estado_multa, monto_deuda, dias_retraso, biblioteca, valor_diario_multa):
        self.id_devolucion = id_devolucion
        self.estado_multa = estado_multa
        self.monto_deuda = monto_deuda
        self.dias_retraso = dias_retraso
        self.biblioteca = biblioteca
        self.valor_diario_multa = 1000

    def generar_multa(self):
        fecha_actual = datetime.now().date()
        
        # Obtener el cursor de la biblioteca
        cursor = self.biblioteca.conexion.cursor()
        
        try:
            # Consulta para seleccionar devoluciones atrasadas
            devo_atrasadas = """SELECT ID_DEVOLUCION, FECHA_DEVOLUCION FROM DEVOLUCIONES 
                                WHERE FECHA_DEVOLUCION < %s AND ESTADO_DEVOLUCION = "PENDIENTE" 
                             """
            cursor.execute(devo_atrasadas, (fecha_actual,))
        
            resultados = cursor.fetchall()  # Usar cursor directamente
            
            id_dev_atrasadas = []
            fecha_dev_atrasadas = []
            dias_a = []

            for i, tupla in enumerate(resultados):
                id_devolucion = tupla[0]
                fecha_devolucion = tupla[1]
                # Convertir fecha_devolucion a datetime.date si es necesario
                if isinstance(fecha_devolucion, datetime):
                    fecha_devolucion = fecha_devolucion.date()
                
                # Calcular días de retraso
                dias_atraso = (fecha_actual - fecha_devolucion).days
                               
                id_dev_atrasadas.append(id_devolucion)
                fecha_dev_atrasadas.append(fecha_devolucion)
                dias_a.append(dias_atraso)
            
                
                print("IDs de devolución atrasadas:", id_dev_atrasadas)
                print("Fechas de devolución atrasadas:", fecha_dev_atrasadas)
                print("Días de retraso:", dias_a)
                
                                 
                
            for i in range(len(id_dev_atrasadas)):
                valor_multa = dias_a[i] * self.valor_diario_multa
                cursor.execute("SELECT COUNT(*) FROM MULTAS WHERE ID_DEVOLUCION = %s", (id_dev_atrasadas[i],))
                existe_multa = cursor.fetchone()[0]  
                if existe_multa:
                    actualizar_multa = """UPDATE MULTAS 
                                          SET ESTADO_MULTA = 'Pendiente', 
                                              MONTO_DEUDA = %s, 
                                              DIAS_RETRASO = %s 
                                          WHERE ID_DEVOLUCION = %s"""
                                          
                    cursor.execute(actualizar_multa, (valor_multa, dias_a[i],id_dev_atrasadas[i]))
                    print("ID_devolucion_atrasada",id_dev_atrasadas[i])
        
                else:
                    registrar_multa = """INSERT INTO MULTAS (ID_DEVOLUCION, ESTADO_MULTA, MONTO_DEUDA, DIAS_RETRASO)
                                     VALUES (%s, %s, %s, %s)"""

                    cursor.execute(registrar_multa, (id_dev_atrasadas[i],'Pendiente', valor_multa, dias_a[i]))
                    
       
        # Confirmar los cambios

            # Confirmar los cambios en la base de datos
            self.biblioteca.conexion.commit()
            
        except Exception as e:
            print(f"Error al generar multas: {e}")
            # Si hay un error, hacer rollback de la transacción
            self.biblioteca.conexion.rollback()

        finally:
            # Cerrar el cursor y la conexión
            self.biblioteca.cursor.close()
