import mysql.connector

conexion = mysql.connector.connect(
        host = "localhost",
        user = "agregar_user",
        password = "agregar_password",
        database = "agregar_base"
    )


def agregar(nombre, precio, descripcion):
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM agregar_tabla") #cambiar el nombre de la tabla

    resultado = cursor.fetchall() #esta es una verificacion para las pruebas, luego la puedes borrar o solo comentar

    print(resultado) #esto es parte de la verificacion

    cursor.execute(f"INSERT INTO `agregar_base`.`agregar_tabla` (`nombre`, `precio`, `descripcion` ) VALUES ('{nombre}', '{precio}', '{descripcion}');") #cambiar nombre de la base de datos y la tabla

    conexion.commit()

    print(cursor.fetchall())  #esto es parte de la verificacion luego de guardar los datos

    cursor.close()

def ejemplo_obtencion_datos(nombre, precio, descripcion): #aqui la prueba de que los datos estan saliendodesde window.py
    print(nombre, precio, descripcion) 
