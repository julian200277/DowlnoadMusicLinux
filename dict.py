import yt_dlp
from PySide6.QtCore import QRunnable, Signal, QObject


class Signals(QObject):
    finished = Signal()
    dic = Signal(dict)

    def __init__(self):
        super().__init__()


class DictLinks(QRunnable):
    def __init__(self, link, panel_progress):
        super().__init__()
        self._link = link
        self.signal = Signals()
        self.info_dict = None
        self.PanelProgress = panel_progress
        """panel_progress  no tiene funcionalidad aún pero es para mostrar los valores de carga 
         del diciconario, por algunas razones no puedo conseguir los datos en tiempo real"""

    def run(self):
        with yt_dlp.YoutubeDL() as self.ydl:
            self.ydl.signal.prueba.connect(self.get_dictionary) # No hay funcionalidad aún en esta conexion
            self.info_dict = self.ydl.extract_info(self._link, download=False)
            self.signal.finished.emit()

    def get_dict(self):
        return self.info_dict

    def get_dictionary(self, value):
        self.signal.dic.emit(value)
