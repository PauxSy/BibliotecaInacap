from datetime import datetime, time
#from biblioteca import Biblioteca  # Asegúrate de importar la clase Biblioteca si no está en este archivo

class Multas:
    def __init__(self, id_devolucion, estado_multa, monto_deuda, dias_retraso, biblioteca, valor_diario_multa):
        self.id_devolucion = id_devolucion
        self.estado_multa = estado_multa
        self.monto_deuda = monto_deuda
        self.dias_retraso = dias_retraso
        self.biblioteca = biblioteca
        self.valor_diario_multa = 1000
        
    
    def pago_multa(self, rut_usuario):
        # Obtener el cursor de la biblioteca
        cursor = self.biblioteca.conexion.cursor()
        cursor.execute("""
            SELECT SUM(M.MONTO_DEUDA) AS TOTAL_MULTAS
            FROM USUARIOS U 
            JOIN PRESTAMOS P ON U.RUT_USUARIO = P.RUT_USUARIO 
            JOIN DEVOLUCIONES D ON P.ID_PRESTAMO = D.ID_PRESTAMO 
            JOIN MULTAS M ON D.ID_DEVOLUCION = M.ID_DEVOLUCION 
            WHERE U.RUT_USUARIO = %s AND M.ESTADO_MULTA = 'Pendiente'
                """,(rut_usuario,))
        
        total_multas = cursor.fetchone()[0]
        
        cursor.execute("""
            SELECT NOMBRE, APELLIDO
            FROM USUARIOS WHERE RUT_USUARIO = %s;
                """,(rut_usuario,))
        
        nombre_usuario = cursor.fetchone()

        if total_multas:
            print("Usuario Sr.(a) ",nombre_usuario[0],"",nombre_usuario[1],": El monto total de la deuda es de",f"${total_multas:,.0f}".replace(",", "."))
            pago = input("¿Desea proceder a registrar el pago de la multa? [1. Si / 2. No]\n")
            if pago == "1":
                cursor.execute("""
                    UPDATE MULTAS M
                    JOIN DEVOLUCIONES D ON P.ID_PRESTAMO = D.ID_PRESTAMO 
                    JOIN PRESTAMOS P ON D.ID_PRESTAMO = P.ID_PRESTAMO 
                    JOIN USUARIOS U ON P.RUT_USUARIO = U.RUT_USUARIO
                    SET M.ESTADO_MULTA = 'Pagada'
                    WHERE U.RUT_USUARIO = %s
                               """)
                # Confirmar los cambios en la base de datos
                self.biblioteca.conexion.commit()
            
                print("[Sistema de Préstamos]: El pago de la/s multa/s pendientes ha sido registrado exitosamente.")

            else:
                print("[Sistema de Préstamos]: Se ha cancelado el proceso de pago.")                
        


        else:
            print("Usuario Sr.(a) ",nombre_usuario[0],"",nombre_usuario[1],": No tiene multas pendientes de pago.")
            
        cursor.close()


            
    def comprobar_multas(self, rut_usuario):
        # Obtener el cursor de la biblioteca
        cursor = self.biblioteca.conexion.cursor()
               
        existe_multa = """
                SELECT U.RUT_USUARIO 
                FROM USUARIOS U 
                JOIN PRESTAMOS P ON U.RUT_USUARIO = P.RUT_USUARIO 
                JOIN DEVOLUCIONES D ON P.ID_PRESTAMO = D.ID_PRESTAMO 
                JOIN MULTAS M ON D.ID_DEVOLUCION = M.ID_DEVOLUCION 
                WHERE U.RUT_USUARIO = %s AND M.ESTADO_MULTA = 'pendiente'
                """
        cursor.execute(existe_multa, (rut_usuario,))

        existe_multa_ = cursor.fetchall()  # Usar cursor directamente
        
        cursor.close()

        if existe_multa_:
            print("[Sistema de Prestamos]: El usuario tiene una o más multas pendiente de pago. No es posible efectuar el préstamo.")
            print("Te devolveré al menu principal.")

            return True
            
        else:
            print("[Sistema de Prestamos]: El usuario no tiene multas pendientes de pago. Puede proceder con el préstamo.")
            return False
        


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
