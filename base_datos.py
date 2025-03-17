import mysql.connector

class BaseDatos:
    def __init__(self, user, password):

        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = user,
            password = password,
            database = 'ejercicio_bases')
        
    def agregar(self, nombre, precio, descripcion):
        cursor = self.conexion.cursor()
        cursor.execute(f"INSERT INTO `ejercicio_bases`.`producto` (`Nombre`, `Precio`, `Descripcion` ) VALUES ('{nombre}', '{precio}', '{descripcion}');") #cambiar nombre de la base de datos y la tabla
        self.conexion.commit()
        cursor.close()

def ejemplo_obtencion_datos(nombre, precio, descripcion): #aqui la prueba de que los datos estan saliendodesde window.py
    print(nombre, precio, descripcion) 


#
