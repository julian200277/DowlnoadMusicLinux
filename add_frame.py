
import yt_dlp
from PySide6.QtCore import QRunnable, QObject, Signal

# Este archivo no interviene aun en ninguna funcionalidad, pero la intención es que se agregue el contenido
# Al panel principal mediante un hilo separado

class Signals(QObject):
    finished = Signal()
    def __init__(self):
        super().__init__()

class AddFrame(QRunnable):
    def __init__(self, link, progresBar):
        super().__init__()
        self._link = link
        self.signal = Signals()
        self.info_dict = None
        self.progresBar = progresBar
        self.youtube = yt_dlp.YoutubeDL()

    def run(self):
        with yt_dlp.YoutubeDL() as self.ydl:
            # self.youtube.signal.addFrame.connect(self.onCountChanged) No existe la señal en YoutubeDL quise usar mi
            # clase personalizada y usar herencia pero NO me funcionó
            self.info_dict = self.ydl.extract_info(self._link, download=False)
            self.signal.finished.emit()

    def onCountChanged(self, value):
        # self.progresBar.setFormat(f'Procesando enlace... {value}%')
        self.progresBar.setValue(value)