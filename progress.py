# -*- coding: utf-8 -*-


from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Style.Styles import Estilos_1


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(567, 263)
        self.estilo = Estilos_1().estiloProgressBar
        Frame.setStyleSheet(self.estilo)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        # font.setBold(True)
        self.label.setFont(font)

        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(Frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"", None))
    # retranslateUi


class Signals(QObject):
    textChanged = Signal(str)
    valueChanged = Signal(int)
    finish = Signal()

    def __init__(self):
        super().__init__()


class Worker(QThread):
    signal = Signals()

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        pass  # bucle


class ProgressWindow(QFrame):
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.signal = Signals()
