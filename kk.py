def renovar_prestamo(self, id_prestamo_original, nueva_fecha_prestamo):
        # Obtener datos del préstamo original
        sql = "SELECT rut_usuario, isbn_libro FROM Prestamos WHERE id_prestamo = %s"
        self.cursor.execute(sql, (id_prestamo_original,))
        resultado = self.cursor.fetchone()
        if resultado:
            rut_usuario, isbn_libro = resultado

            # Cambiar el estado del préstamo original a 'Inactivo'
            sql_update_prestamo = "UPDATE Prestamos SET estado_prestamo = 'Inactivo' WHERE id_prestamo = %s"
            self.cursor.execute(sql_update_prestamo, (id_prestamo_original,))
            self.conexion.commit()

            # Cambiar el estado de la devolución a 'Devuelto'
            sql_update_devolucion = "UPDATE Devoluciones SET estado_devolucion = 'Devuelto' WHERE id_prestamo = %s"
            self.cursor.execute(sql_update_devolucion, (id_prestamo_original,))
            self.conexion.commit()

            # Registrar un nuevo préstamo con los mismos datos del original
            nuevo_prestamo = Prestamos(rut_usuario, isbn_libro, 'Renovación', 'Activo', nueva_fecha_prestamo, self.conexion, self.cursor)
            nuevo_prestamo.agregar_prestamo()

            # Registrar automáticamente una nueva devolución para el nuevo préstamo
            fecha_devolucion = nueva_fecha_prestamo + timedelta(days=3)
            nueva_devolucion = Devoluciones(nuevo_prestamo.id_prestamo, fecha_devolucion, 'Pendiente', self.conexion, self.cursor)
            nueva_devolucion.registrar_devoluciones()
        else:
            print("Préstamo original no encontrado.")