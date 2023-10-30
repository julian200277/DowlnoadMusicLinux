class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            # self.info(msg)
            print(f'Logger: {msg}')

    def info(self, msg):
        print(f'Info: {msg}')

    def warning(self, msg):
        print(f'Warning: {msg}')

    def error(self, msg):
        print(f'Error: {msg}')
