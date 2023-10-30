from logger import MyLogger
class FormatInput:
    def __init__(self, codec, quality=None, hook=None, format=None, title=None, path=None):
        #AUDIO
        self.codec = codec
        self.quality = quality
        self.hook = hook
        self.path = path
        self.format = format
        self.title = title

        self.opts_audio = {
            'ignoreerrors': True,
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': self.codec,
            'preferredquality': self.quality,
        }], 'progress_hooks': [self.hook],
            'logger': MyLogger(),
            'outtmpl': self.path + '/'+self.title,
            'ffmpeg_location': 'ffmpeg-6.0',     # ffmpeg-5.0 are .exe for windows, ffmpeg-6.0 are for Linux


        }

        self.opts_video = {
            'ignoreerrors': True,
            'format': self.format,
            'outtmpl': self.path + '/'+self.title,
            'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': self.codec,  # one of avi, -flv, -mkv, -mp4, -ogv, -wmv, webm      No 3gp support
        }], 'progress_hooks': [self.hook],
            'logger': MyLogger(),
            'ffmpeg_location': 'ffmpeg-6.0',
        }