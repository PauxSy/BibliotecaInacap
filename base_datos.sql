CREATE DATABASE PROYECTOFINAL;
USE PROYECTOFINAL;


CREATE TABLE USUARIOS(
RUT_USUARIO VARCHAR(10),
TIPO_USUARIO VARCHAR(8),
NOMBRE VARCHAR(32),
APELLIDO VARCHAR (50),
EMAIL VARCHAR(35),
CELULAR INT
);


CREATE TABLE PRESTAMOS(
ID_PRESTAMO INT,
RUT_USUARIO VARCHAR(10),
ISBN_LIBRO INT,
TIPO_DE_PRESTAMO VARCHAR(20),
ESTADO_PRESTAMO VARCHAR(10),
FECHA_PRESTAMO DATE
);


CREATE TABLE LIBROS(
ISBN_LIBRO INT,
GENERO VARCHAR(15),
TITULO VARCHAR (45),
AUTOR VARCHAR (35),
STOCK INT,
IDIOMA VARCHAR(15)
);


CREATE TABLE MULTAS(
ID_MULTA INT,
ID_DEVOLUCION INT,
ESTADO_MULTA VARCHAR(15),
MONTO_DEUDA INT,
DIAS_RETRASO INT
);


CREATE TABLE DEVOLUCIONES(
ID_DEVOLUCION INT,
ID_PRESTAMO INT,
FECHA_DEVOLUCION DATE,
ESTADO_DEVOLUCION VARCHAR(10)
);

ALTER TABLE USUARIOS
ADD CONSTRAINT PK_USUARIOS_RUT_USUARIO
PRIMARY KEY (RUT_USUARIO);

ALTER TABLE PRESTAMOS
ADD CONSTRAINT PK_PRESTAMOS_ID_PRESTAMO
PRIMARY KEY (ID_PRESTAMO);

ALTER TABLE LIBROS
ADD CONSTRAINT PK_LIBROS_ISBN_LIBRO
PRIMARY KEY (ISBN_LIBRO);

ALTER TABLE MULTAS
ADD CONSTRAINT PK_MULTAS_ID_MULTA
PRIMARY KEY (ID_MULTA);

ALTER TABLE DEVOLUCIONES
ADD CONSTRAINT PK_DEVOLUCIONES_ID_DEVOLUCION
PRIMARY KEY (ID_DEVOLUCION);

ALTER TABLE PRESTAMOS
ADD CONSTRAINT FK_PRESTAMOS_RUT_USUARIO
FOREIGN KEY (RUT_USUARIO)
REFERENCES USUARIOS (RUT_USUARIO);

--
ALTER TABLE PRESTAMOS
ADD CONSTRAINT FK_PRESTAMOS_ISBN_LIBRO
FOREIGN KEY (ISBN_LIBRO)
REFERENCES LIBROS (ISBN_LIBRO);

ALTER TABLE MULTAS 
ADD CONSTRAINT FK_MULTAS_ID_DEVOLUCION
FOREIGN KEY (ID_DEVOLUCION)
REFERENCES DEVOLUCIONES (ID_DEVOLUCION);

ALTER TABLE DEVOLUCIONES
ADD CONSTRAINT FK_DEVULUCIONES_ID_PRESTAMO
FOREIGN KEY (ID_PRESTAMO)
REFERENCES PRESTAMOS (ID_PRESTAMO);


