# -*- coding: utf-8 -*-

from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Style.Styles import Estilos_1
from download import Download
from formats import FormatInput
import os
class Signals(QObject):
    countChanged = Signal(int)
    emitId = Signal(QFrame)
    def __init__(self):
        super().__init__()

class FrameDownload(QFrame):
    def __init__(self):
        super().__init__(parent=None)
        self.ydl_opts = {}
        self.signal = Signals()
        self.estilo = Estilos_1().estiloFrame
        self.defaultPath = f'{Path.home()}/Música'
        self.videoSelection = False
        self.resize(945, 185)
        self.codec = 'mp3'
        self.quality = '192'
        self.enumerate = False
        self.download_complete = False
        self.sombra = QGraphicsDropShadowEffect()
        self.sombra.setBlurRadius(12)
        self.sombra.setColor(QColor(0, 0, 0))
        self.sombra.setOffset(2, 2)
        self.setGraphicsEffect(self.sombra)
        self.setStyleSheet(self.estilo)
        self.setMaximumSize(QSize(945, 185))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(196, 110))
        self.frame.setMaximumSize(QSize(196, 110))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.labelImagen = QLabel(self.frame)
        self.labelImagen.setObjectName(u"labelImagen")
        self.labelImagen.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.labelImagen)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTitulo = QLabel(self)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.verticalLayout_2.addWidget(self.labelTitulo)
        self.splitter_4 = QSplitter(self)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter_4)
        self.label.setObjectName(u"label")
        self.splitter_4.addWidget(self.label)
        self.lineEdit = QLineEdit(self.splitter_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.splitter_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.splitter_3 = QSplitter(self)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.labelFormato = QLabel(self.splitter_3)
        self.labelFormato.setObjectName(u"labelFormato")
        self.labelFormato.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.labelFormato)
        self.labelCalidad = QLabel(self.splitter_3)
        self.labelCalidad.setObjectName(u"labelCalidad")
        self.labelCalidad.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.labelCalidad)
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.splitter = QSplitter(self)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.comboBox = QComboBox(self.splitter)
        self.comboBox.setObjectName(u"comboBox")
        self.splitter.addWidget(self.comboBox)
        self.comboBox_2 = QComboBox(self.splitter)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.splitter.addWidget(self.comboBox_2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.labelDuracion = QLabel(self.splitter_2)
        self.labelDuracion.setObjectName(u"labelDuracion")
        self.splitter_2.addWidget(self.labelDuracion)
        self.labelExtractor = QLabel(self.splitter_2)
        self.labelExtractor.setObjectName(u"labelExtractor")
        self.splitter_2.addWidget(self.labelExtractor)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.labelWebPage = QLabel(self)
        self.labelWebPage.setObjectName(u"labelWebPage")
        self.labelWebPage.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse)
        self.verticalLayout_2.addWidget(self.labelWebPage)
        self.splitter_5 = QSplitter(self)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.progressBar = QProgressBar(self.splitter_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAlignment(Qt.AlignCenter)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(0)
        self.splitter_5.addWidget(self.progressBar)
        self.labelKbps = QLabel(self.splitter_5)
        self.labelKbps.setObjectName(u"labelKbps")
        self.labelKbps.setAlignment(Qt.AlignCenter)
        self.splitter_5.addWidget(self.labelKbps)
        self.verticalLayout_2.addWidget(self.splitter_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnOpen = QPushButton(self)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setMinimumSize(QSize(35, 35))
        self.btnOpen.setMaximumSize(QSize(35, 35))
        self.btnOpen.setEnabled(False)
        icon = QIcon()
        icon.addFile(u"img/folder3.png",QSize(), QIcon.Normal, QIcon.Off)
        self.btnOpen.setIcon(icon)
        self.btnOpen.setIconSize(QSize(32, 32))
        self.verticalLayout_3.addWidget(self.btnOpen)
        self.btnEliminar = QPushButton(self)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setMinimumSize(QSize(35, 35))
        self.btnEliminar.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u"img/cancel.png",QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminar.setIcon(icon1)
        self.btnEliminar.setIconSize(QSize(32, 32))
        self.verticalLayout_3.addWidget(self.btnEliminar)
        self.btnDescargar = QPushButton(self)
        self.btnDescargar.setObjectName(u"btnDescargar")
        self.btnDescargar.setMinimumSize(QSize(35, 35))
        self.btnDescargar.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u"img/download.png",QSize(), QIcon.Normal, QIcon.Off)
        self.btnDescargar.setIcon(icon2)
        self.btnDescargar.setIconSize(QSize(32, 32))
        self.verticalLayout_3.addWidget(self.btnDescargar)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.labelImagen.setText("")
        self.labelTitulo.setText("")
        self.label.setText(QCoreApplication.translate("Frame", u"  Titulo de Salida  ", None))
        self.labelFormato.setText(QCoreApplication.translate("Frame", u"Formato", None))
        self.labelCalidad.setText(QCoreApplication.translate("Frame", u"Calidad disponible", None))
        self.labelDuracion.setText("")
        self.labelExtractor.setText("")
        self.labelWebPage.setText("")
        self.labelKbps.setText(QCoreApplication.translate("Frame", u"            Kbps            ", None))
        self.btnOpen.setText("")
        self.btnEliminar.setText("")
        self.btnDescargar.setText("")
        # retranslateUi

        # VARIABLES
        audioFormat = ['aac', 'm4a', 'mp3', 'ogg', 'wav', 'flac']
        videoFormat = ['flv', 'mp4', 'mkv', 'mpg', 'ogv', 'wmv']
        self.resolutions = None
        self.video_extension = ''
        self.comboBox.addItems(audioFormat + videoFormat)
        self.quality_audio = ['Buena', 'Regular']
        self.comboBox_2.addItems(self.quality_audio)

        # SEÑALES
        self.btnOpen.clicked.connect(self.open_download_path)
        self.btnEliminar.clicked.connect(self.panelDelete)
        self.btnDescargar.clicked.connect(self.download)
        self.comboBox.currentTextChanged.connect(self.getValueFormatCombo)
        self.progressBar.valueChanged.connect(self.progressBar.setValue)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(2)
    # METODOS

    def setPath(self, path):
        self.defaultPath = path
    def getPath(self):
        return self.defaultPath
    def open_download_path(self):
        os.system(f'open {os.path.realpath(self.defaultPath)}')
    def set_resolutions(self, resolutions):
        self.resolutions = resolutions
    def get_resolutions(self):
        return  self.resolutions
    def getValueFormatCombo(self, value):
        self.codec = value
        if value == 'aac' or self.codec == 'm4a' or self.codec == 'mp3' or self.codec == 'ogg' or self.codec == 'wav' or self.codec == 'flac':
            if value == 'ogg':
                self.codec = 'vorbis'
            self.videoSelection = False
            self.comboBox_2.currentIndexChanged.connect(self.getValueQualityAudio)
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.quality_audio)

        else:
            self.videoSelection = True
            self.comboBox_2.currentTextChanged.connect(self.getValueQualityVideo)
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.get_resolutions())

    def getValueQualityAudio(self, value):
        if value == 0:
            self.quality = '192'
        elif value == 1:
            self.quality = '128'
    def getValueQualityVideo(self, value):
        resolution = []
        if value == 'Buena' or value == 'Regular':
            resolution.clear()
            return
        elif 'x' in value:
            resolution = value.split('x')
            self.video_extension = f'bestvideo[height<={resolution[1]}][width<={resolution[0]}]+bestaudio/best[height<={resolution[1]}][width<={resolution[0]}]'

    def get_opts(self):
        if self.videoSelection:
            formats = FormatInput(self.codec,
                                  quality=None,
                                  hook=self.my_hook,
                                  format=self.video_extension,
                                  title=self.lineEdit.text(),
                                  path=self.getPath())
            opts = formats.opts_video
            return opts
        else:
            formats = FormatInput(self.codec,
                                  quality=self.quality,
                                  hook=self.my_hook,
                                  format=None,
                                  title=self.lineEdit.text(),
                                  path=self.getPath())
            opts = formats.opts_audio
            return opts

    def panelDelete(self):
        self.signal.emitId.emit(self)

    def download(self):
        self.defaultPath = self.getPath()   #parchesito
        download = Download(self.labelWebPage.text(), self.get_opts())  #Link, opts
        threadCount = QThreadPool.globalInstance().maxThreadCount()
        pool = QThreadPool.globalInstance()
        download.signal.finished.connect(self.finishDownload)
        pool.start(download)

    def finishDownload(self):
        self.download_complete = True
        self.progressBar.setFormat('Terminado')
        self.btnDescargar.setEnabled(False)
        self.btnOpen.setEnabled(True)
        # self.setStyleSheet('background-color: rgba(0, 0, 20, 0.25);')

    def my_hook(self, d):
        if d['status'] == 'downloading':
            v = d['_speed_str']
            p = d['_percent_str']
            p = p.replace('%', '')
            p.strip()
            self.progressBar.valueChanged.emit(float(p))
            self.labelKbps.setText(v)
        if d['status'] == 'finished':
            self.progressBar.setFormat('Convirtiendo...')

