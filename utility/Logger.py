from datetime import datetime

from config import PRINT_TO_CONSOLE, PRINT_TO_FILE, LOG_FILE_NAME


class Logger(object):
    _instance = None  # static

    _print_to_console = True
    _print_to_file = False
    _file = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(PRINT_TO_CONSOLE, PRINT_TO_FILE, LOG_FILE_NAME)
        return cls._instance

    def _initialize(self, print_to_console: bool = True, print_to_file: bool = False, file_name: str = None):
        self._print_to_console = print_to_console
        if print_to_file:
            if not file_name:
                now = datetime.now().strftime('%Y%m%d%H%M%S')
                file_name = f'{now}-chess-game.txt'
            self._file = open(f'output/{file_name}', 'a')
            self._print_to_file = print_to_file
            self.log('Logger initialized')

    def log(self, data, flush: bool = False):
        now = datetime.now()
        message = f'[{now}] {data}'
        if self._print_to_console:
            print(message)
        if self._print_to_file:
            self._file.write(f'{message}\n')
            if flush:
                self._file.flush()

    def flush(self):
        if self._print_to_file:
            self._file.flush()

    def close(self):
        if self._print_to_file:
            self._print_to_file = False
            self._file.close()
