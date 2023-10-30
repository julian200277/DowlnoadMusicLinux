import yt_dlp
from PySide6.QtCore import QObject, QRunnable, Signal


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Download(QRunnable):
    def __init__(self, link, opts):
        super().__init__()
        self.opts = opts
        self.link = link
        self.signal = Signals()

    def run(self):
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            ydl.download([self.link])
            self.signal.finished.emit()  # emite cuando ya se haya terminado la señal para que otro hilo inicie
