import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

class Window:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window1 = QWidget()
        self.window2 = QWidget()
        self.window1.setStyleSheet("background-color: #2671a5;")
        self.window1.setWindowTitle("Ejercicio_base_datos")
        self.window1.setFixedSize(200, 150)
        self.window2.setStyleSheet("background-color: #2671a5;")
        self.window2.setWindowTitle("Ejercicio_base_datos")
        self.window2.setFixedSize(400, 300)


    def Ingreso_de_datos(self):
        main_layout = QVBoxLayout()
        vertical_layout1 = QVBoxLayout()
        vertical_layout2 = QVBoxLayout()
        vertical_layout3 = QVBoxLayout()
        vertical_layout4 = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        save = QPushButton("Guardar")
        save.setStyleSheet("Color: black; background-color: white;")
        cancel = QPushButton("Cancelar")
        cancel.setStyleSheet("Color: black; background-color: white;")
        cancel.clicked.connect(self.cancelar)
        data = QLabel("Ingreso de datos")
        data.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nombre = QLabel("Nombre:")
        self.nombre_text = QLineEdit()
        self.nombre_text.setStyleSheet("Color: black; background-color: white;")
        price = QLabel("Precio:")
        self.price_text = QLineEdit()
        self.price_text.setStyleSheet("Color: black; background-color: white;")
        description = QLabel("Descripción:")
        self.description_text = QLineEdit()
        self.description_text.setStyleSheet("Color: black; background-color: white;")
        vertical_layout4.addWidget(nombre)
        vertical_layout4.addWidget(self.nombre_text)
        vertical_layout4.addWidget(price)
        vertical_layout4.addWidget(self.price_text)
        vertical_layout4.addWidget(description)
        vertical_layout4.addWidget(self.description_text)
        horizontal_layout1.addLayout(vertical_layout4)
        vertical_layout1.addWidget(data)
        horizontal_layout2.addWidget(save)
        horizontal_layout2.addWidget(cancel)
        vertical_layout2.addLayout(horizontal_layout1)
        vertical_layout3.addLayout(horizontal_layout2)
        main_layout.addLayout(vertical_layout1)
        main_layout.addLayout(vertical_layout2)
        main_layout.addLayout(vertical_layout3)
        self.window2.setLayout(main_layout)       
        self.window2.setLayout(QVBoxLayout())
        self.window2.show()

    def inicio(self):
        main_layout = QVBoxLayout()
        ingreso_Id = QLabel("Ingresa el usuario:")
        self.ingreso_text_Id = QLineEdit()
        self.ingreso_text_Id.setStyleSheet("Color: black; background-color: white;")
        ingreso_passeord = QLabel("Ingresa la contraseña:")
        self.ingreso_text_password = QLineEdit()
        self.ingreso_text_password.setStyleSheet("Color: black; background-color: white;")
        self.ingreso_text_password.setEchoMode(QLineEdit.EchoMode.Password)
        button_ingreso = QPushButton("Ingresar")
        button_ingreso.clicked.connect(self.verificacion)
        button_ingreso.setStyleSheet("Color: black; background-color: white;")
        main_layout.addWidget(ingreso_Id)
        main_layout.addWidget(self.ingreso_text_Id)
        main_layout.addWidget(ingreso_passeord)
        main_layout.addWidget(self.ingreso_text_password)
        main_layout.addWidget(button_ingreso)
        self.window1.setLayout(main_layout)
        self.window1.show()

    def verificacion(self):
        if self.ingreso_text_Id.text() == "admin" and self.ingreso_text_password.text() == "admin":
            self.window1.close()
            self.Ingreso_de_datos()
        else:
            QMessageBox.warning(self.window, "Error", "Usuario o contraseña incorrectos")

    def guardar(self):
        #Va a hacer algo :)
        pass
    
    def cancelar(self):
        self.nombre_text.clear()
        self.price_text.clear()
        self.description_text.clear()
        QMessageBox.information(self.window2, "Ingreso cancelado", "Se ha cancelado el ingreso de datos")