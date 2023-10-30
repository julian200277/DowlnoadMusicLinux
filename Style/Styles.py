from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class Estilos_1():
    def __init__(self):
        # self.sombra = QGraphicsDropShadowEffect()
        # self.sombra.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra.setOffset(5)
        # self.sombra.setBlurRadius(7)
        #
        # self.sombra2 = QGraphicsDropShadowEffect()
        # self.sombra2.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra2.setOffset(5)
        # self.sombra2.setBlurRadius(7)
        #
        # self.sombra3 = QGraphicsDropShadowEffect()
        # self.sombra3.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra3.setOffset(5)
        # self.sombra3.setBlurRadius(7)
        self.estiloPrincipal = """
            QMainWindow{
                background-image: url(img/fondo2.jpg);
                background-color: rgba(0, 0, 2, 0.7);
             }
             QPushButton{
                background-color: rgba(0, 0, 2, 0.3);
                border-radius: 5px;
                padding: 3px;
                border-bottom: 2px solid rgba(27, 27, 27, 255 * 0.7);
                border-right: 2px solid rgba(27, 27, 27, 255 * 0.7);
                
             }
             QPushButton:hover{
                background-color: rgba(245, 123, 2, 0.65);
                color: #000;

             }
             QPushButton:pressed{
                background-color: rgba(255, 123, 46, 255 * 0.65);
                padding-top: 0px;
                border-top: 2px solid rgba(27, 27, 27, 255 * 0.7);
                border-left: 2px solid rgba(27, 27, 27, 255 * 0.7);
                border-bottom: 0px;
                border-right: 0px;
            }
            QTextEdit{
                color: white;
            }

            QWidget{
                background-color: rgba(200, 200, 200, 0.1);
                border-radius: 7px;
                color: white;
            }
            QComboBox{
                padding: 7px;
            }
            
        """
        self.estiloFrame = """
            QFrame{
                
                border-radius: 7px;
                color: white;
            }
        
            QComboBox{
                padding: 4px;
            }
        """
        self.estiloProgressBar = """
            QLabel{
                color: white;
            }
            
            QProgressBar{
                border: 2px solid grey;border-radius:8px;padding:1px;
            }
            
        """

        # SOMBRA BOTONES
        # self.sombra4 = QGraphicsDropShadowEffect()
        # self.sombra4.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra4.setOffset(5)
        # self.sombra4.setBlurRadius(7)
        #
        # self.sombra5 = QGraphicsDropShadowEffect()
        # self.sombra5.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra5.setOffset(5)
        # self.sombra5.setBlurRadius(7)
        #
        # self.sombra6 = QGraphicsDropShadowEffect()
        # self.sombra6.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra6.setOffset(5)
        # self.sombra6.setBlurRadius(7)
        #
        # self.sombra7 = QGraphicsDropShadowEffect()
        # self.sombra7.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra7.setOffset(5)
        # self.sombra7.setBlurRadius(7)
        #
        # self.sombra8 = QGraphicsDropShadowEffect()
        # self.sombra8.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra8.setOffset(5)
        # self.sombra8.setBlurRadius(7)
        #
        # self.sombra9 = QGraphicsDropShadowEffect()
        # self.sombra9.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra9.setOffset(5)
        # self.sombra9.setBlurRadius(7)
        #
        # self.sombra10 = QGraphicsDropShadowEffect()
        # self.sombra10.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra10.setOffset(5)
        # self.sombra10.setBlurRadius(7)
        #
        # self.sombra11 = QGraphicsDropShadowEffect()
        # self.sombra11.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra11.setOffset(5)
        # self.sombra11.setBlurRadius(7)
        #
        # self.sombra12 = QGraphicsDropShadowEffect()
        # self.sombra12.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra12.setOffset(5)
        # self.sombra12.setBlurRadius(7)
        #
        # self.sombra13 = QGraphicsDropShadowEffect()
        # self.sombra13.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra13.setOffset(5)
        # self.sombra13.setBlurRadius(7)
        #
        # self.sombra14 = QGraphicsDropShadowEffect()
        # self.sombra14.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra14.setOffset(5)
        # self.sombra14.setBlurRadius(7)
        #
        # self.sombra15 = QGraphicsDropShadowEffect()
        # self.sombra15.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra15.setOffset(5)
        # self.sombra15.setBlurRadius(7)
        #
        # self.sombra16 = QGraphicsDropShadowEffect()
        # self.sombra16.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra16.setOffset(5)
        # self.sombra16.setBlurRadius(7)
        #
        # self.sombra17 = QGraphicsDropShadowEffect()
        # self.sombra17.setColor(QColor(0, 0, 0, 255 * 0.7))
        # self.sombra17.setOffset(5)
        # self.sombra17.setBlurRadius(7)
