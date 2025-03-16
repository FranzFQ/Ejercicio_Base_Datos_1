from window import Window
import sys

def main():
    ventana = Window()
    app = ventana.app
    ventana.inicio()
    sys.exit(app.exec())
    
main()   