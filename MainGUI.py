#!/usr/bin/env python3
# coding: utf-8

import yt_dlp

import urllib
from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from dict import DictLinks
from frame_download import FrameDownload
from Style.Styles import Estilos_1
from progress import ProgressWindow
import urllib.request



class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(950, 750)
        self.estilo = Estilos_1().estiloPrincipal
        self.defaultPath = f'{Path.home()}/Música'
        self.setStyleSheet(self.estilo)
        self.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.txtURL = QTextEdit(self.splitter)
        self.txtURL.setObjectName(u"txtURL")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtURL.sizePolicy().hasHeightForWidth())
        self.txtURL.setSizePolicy(sizePolicy)
        self.txtURL.setMinimumSize(QSize(0, 28))
        self.txtURL.setMaximumSize(QSize(16777215, 28))
        self.splitter.addWidget(self.txtURL)
        self.btnAgregar = QPushButton(self.splitter, 'Agregar')
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setMinimumSize(QSize(28, 28))
        self.btnAgregar.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u"img/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAgregar.setIcon(icon)
        self.btnAgregar.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.btnAgregar)
        # self.btnAjustes = QPushButton(self.splitter)
        # self.btnAjustes.setObjectName(u"btnAjustes")
        # self.btnAjustes.setMinimumSize(QSize(28, 28))
        # self.btnAjustes.setMaximumSize(QSize(28, 28))
        # icon1 = QIcon()
        # icon1.addFile(u"img/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.btnAjustes.setIcon(icon1)
        # self.btnAjustes.setIconSize(QSize(24, 24))
        # self.splitter.addWidget(self.btnAjustes)

        self.verticalLayout.addWidget(self.splitter)

        self.labelPath = QLabel(self.centralwidget)
        self.labelPath.setObjectName(u"labelPath")


        self.verticalLayout.addWidget(self.labelPath)

        #aqui
        self.splitter = QSplitter(self)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 10, 711, 35))
        self.splitter.setOrientation(Qt.Horizontal)
        self.labelEnumerar = QLabel(self.splitter)
        self.labelEnumerar.setObjectName(u"labelEnumerar")
        self.splitter.addWidget(self.labelEnumerar)
        self.btnEnumerar = QPushButton(self.splitter)
        self.btnEnumerar.setObjectName(u"btnEnumerar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEnumerar.sizePolicy().hasHeightForWidth())
        self.btnEnumerar.setSizePolicy(sizePolicy)
        self.btnEnumerar.setMinimumSize(QSize(28, 28))
        self.btnEnumerar.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u"img/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEnumerar.setIcon(icon)
        self.btnEnumerar.setIconSize(QSize(24, 24))
        self.btnEnumerar.setEnabled(False)
        self.splitter.addWidget(self.btnEnumerar)
        self.labelSpacer = QLabel(self.splitter)
        self.labelSpacer.setObjectName(u"labelSpacer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelSpacer.sizePolicy().hasHeightForWidth())
        self.labelSpacer.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.labelSpacer)
        self.verticalLayout.addWidget(self.splitter)
        #aqui

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 855, 172))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRuta = QPushButton(self.centralwidget)
        self.btnRuta.setObjectName(u"btnRuta")
        self.btnRuta.setMinimumSize(QSize(28, 28))
        self.btnRuta.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u"img/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRuta.setIcon(icon2)
        self.btnRuta.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnRuta)

        self.cbxFormato = QComboBox(self.centralwidget)
        self.cbxFormato.setObjectName(u"cbxFormato")
        self.cbxFormato.setEnabled(False)
        self.horizontalLayout.addWidget(self.cbxFormato)

        self.counter = QLabel(self.centralwidget)
        self.counter.setObjectName(u"counter")
        self.counter.setStyleSheet('background-color: black; color: red')
        self.horizontalLayout.addWidget(self.counter)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(28, 28))
        self.btnDelete.setMaximumSize(QSize(28, 28))
        self.btnDelete.setSizeIncrement(QSize(35, 0))
        icon3 = QIcon()
        icon3.addFile(u"img/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setIconSize(QSize(24, 24))
        self.btnDelete.setEnabled(False)
        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setMinimumSize(QSize(28, 28))
        self.btnDownload.setMaximumSize(QSize(28, 28))
        icon4 = QIcon()
        icon4.addFile(u"img/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDownload.setIcon(icon4)
        self.btnDownload.setIconSize(QSize(24, 24))
        self.btnDownload.setEnabled(False)

        self.horizontalLayout.addWidget(self.btnDownload)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 875, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.progress = ProgressWindow()
        self.verticalLayout.addWidget(self.progress)
        self.progress.hide()
        self.general_formats = ['aac', 'm4a', 'mp3', 'ogg', 'wav', 'flac', 'flv', 'mp4', 'mkv', 'mpg', 'ogv', 'wmv']
        self.cbxFormato.addItems(self.general_formats)
        self.cbxFormato.setCurrentIndex(2)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music and Video", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.btnAgregar.setText("")
        self.btnAgregar.setToolTip("Agregar enlace")
        # self.btnAjustes.setText("")
        # self.btnAjustes.setToolTip("Ajustes")
        self.labelPath.setText(self.defaultPath)
        self.btnRuta.setText("")
        self.btnDelete.setText("")
        self.btnDelete.setToolTip("Eliminar Todo")
        self.btnDownload.setText("")
        self.btnDownload.setToolTip("Descargar todo")
        self.labelEnumerar.setText(QCoreApplication.translate("Frame", u"Enumerar todos los elementos", None))
        self.btnEnumerar.setText("")
        self.labelSpacer.setText("")


        # retranslateUi
                        #VARIABLES
        self.webpage_url = ''
        self.cantFrames = 0
        #self.frame = None
        self.codec = ''
        self.videoSelection = False
        self.lista_resoluciones = None
        self.video_extension = ''
                        # SIGNALS

        self.btnRuta.clicked.connect(self.open_path)
        self.btnAgregar.clicked.connect(self.pre_process_playlist)
        self.btnDownload.clicked.connect(self.downloadAll)
        self.btnDelete.clicked.connect(self.deleteAll)
        self.btnEnumerar.clicked.connect(self.panel_enumerate)
        QApplication.clipboard().dataChanged.connect(self.clipboardChanged)
        self.cbxFormato.currentIndexChanged.connect(self.format_for_all)

    def format_for_all(self, value):
        for i in range(self.verticalLayout_2.count()):
            self.verticalLayout_2.itemAt(i).widget().comboBox.setCurrentIndex(value)

    def open_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.defaultPath = str(QFileDialog.getExistingDirectory(self, "Seleccionar Ruta", "/Home", options=options))
        print(f"default path {self.defaultPath}")
        self.labelPath.setText(f'{self.defaultPath}')

    def clipboardChanged(self):
        text = QApplication.clipboard().text()
        if self.txtURL.toPlainText() == '':
            self.txtURL.insertPlainText(text)
        else:
            self.txtURL.setText('')
            self.txtURL.insertPlainText(text)

    def get_frame(self):
        frame = FrameDownload()
        frame.signal.emitId.connect(self.individual_delete)
        self.set_frame_path(frame)
        return frame


    def set_frame_path(self, frame):
        frame.setPath(self.defaultPath)

    def pre_process_playlist(self):
        self.progress.setStyleSheet(self.progress.ui.estilo)
        self.progress.ui.label.setText("Procesando entrada, espere...")
        self.progress.show()
        path = self.txtURL.toPlainText()
        thread_count = QThreadPool.globalInstance().maxThreadCount()
        pool = QThreadPool().globalInstance()
        self.diccionario = DictLinks(path, self.progress)
        self.diccionario.signal.finished.connect(self.add_frames)
        #self.diccionario.signal.dic.connect(self.add_frames)
        pool.start(self.diccionario)

    def add_frames(self):       #Es hasta que termina la extraccion del diccionario
        self.btnDelete.setEnabled(True)
        self.btnDownload.setEnabled(True)
        self.btnEnumerar.setEnabled(True)
        self.cbxFormato.setEnabled(True)
        self.dic = self.diccionario.get_dict()
        resolution = set()
        audio_values_discarded = ['audio only', '80x45', '160x90', '48x27', '120x90', '60x45']
        null_elements = 1
        if self.dic is not None:
            if self.dic.get('_type', 'video') == 'playlist':
                for valor in self.dic['entries']:
                    if valor is None:
                        self.counter.setStyleSheet('background-color: black; color: red')
                        self.counter.setText(f'{null_elements} Elementos ya no están disponibles')
                        null_elements += 1
                        continue
                    else:
                        for value in valor['formats']:
                            if value['resolution'] in audio_values_discarded:
                                continue
                            resolution.add(value["resolution"])

                        self.lista_resoluciones = list(resolution)
                        frame = self.get_frame()
                        frame.set_resolutions(resolution)
                        self.set_video_data_playlist(frame, valor)
                        self.verticalLayout_2.addWidget(frame)

            else:
                for value in self.dic.get('formats'):
                    if value['resolution'] in audio_values_discarded:
                        continue
                    resolution.add(value["resolution"])

                self.progress.ui.label.setText("Procesando entrada, espere...")
                self.progress.ui.progressBar.setValue(100)
                frame = self.get_frame()
                self.lista_resoluciones = list(resolution) #aqui no le muevo
                frame.set_resolutions(resolution)
                self.set_video_data(frame)
                self.verticalLayout_2.addWidget(frame)
            self.progress.hide()
            self.progress.ui.progressBar.reset()
        else:
            self.progress.setStyleSheet('background-color: black; color: red')
            # self.progress.ui.label.setStyleSheet('color: black;')
            self.progress.ui.label.setText(f'Error URL no válida')
            #os.system(f'yt-dlp {self.txtURL.toPlainText()} --cookies {"udemy-cookies.txt"}')

    def set_video_data_playlist(self, frame, value):
        duration = value.get('duration', None)
        video_title = value.get('title', None)
        image = value.get('thumbnails', None)
        extractor = value.get('extractor_key', None)
        self.webpage_url = value.get('webpage_url', None)
        if extractor == 'Youtube':
            url = image[25]['url']
        else:
            url = image[0]['url']
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        frame.labelImagen.setPixmap(pixmap)
        frame.labelImagen.setScaledContents(True)
        frame.labelTitulo.setText(video_title)
        frame.labelDuracion.setText(f'{duration/60:.2f} minutos')
        frame.labelExtractor.setText(extractor)
        frame.labelWebPage.setText(self.webpage_url)
        frame.lineEdit.setText(video_title)

    def set_video_data(self, frame):
        try:
            duration = self.dic.get("duration", None)
            video_title = self.dic.get('title', None)
            image = self.dic.get('thumbnails', None)
            extractor = self.dic.get('extractor_key', None)
            self.webpage_url = self.dic.get('webpage_url', None)
            if extractor == 'Youtube':
                url = image[25]['url']
            else:
                url = image[0]['url']
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            frame.labelImagen.setPixmap(pixmap)
            frame.labelImagen.setScaledContents(True)
            frame.labelTitulo.setText(video_title)
            frame.labelDuracion.setText(f'{duration/60:.2f} minutos')
            frame.labelExtractor.setText(extractor)
            frame.labelWebPage.setText(self.webpage_url)
            frame.lineEdit.setText(video_title)
        except:
            self.progress.setStyleSheet('background-color: black; color: red')
            # self.progress.ui.label.setStyleSheet('color: black;')
            self.progress.ui.label.setText(f'Error URL no válida')

    def panel_enumerate(self):
        for i in range(self.verticalLayout_2.count()):
            text = self.verticalLayout_2.itemAt(i).widget().labelTitulo.text()
            self.verticalLayout_2.itemAt(i).widget().lineEdit.setText(str(i+1) + ' ' + text)
            self.verticalLayout_2.itemAt(i).widget().enumerate = True

    def downloadAll(self):
        for i in range(self.verticalLayout_2.count()):
            if self.verticalLayout_2.itemAt(i).widget().download_complete:
                continue
            self.verticalLayout_2.itemAt(i).widget().download()
            self.verticalLayout_2.itemAt(i).widget().btnDescargar.setEnabled(False)

    def individual_delete(self, frame):
        frame.deleteLater()

    def deleteAll(self):
        self.counter.setStyleSheet(self.estilo)
        self.counter.setText("")
        for i in range(self.verticalLayout_2.count()):
            self.verticalLayout_2.itemAt(i).widget().panelDelete()
        self.btnDownload.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnEnumerar.setEnabled(False)

if __name__ == '__main__':
    app = QApplication()
    ventana = Ui_MainWindow()
    ventana.show()
    sys.exit(app.exec())
