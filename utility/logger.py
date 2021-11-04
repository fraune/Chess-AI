import datetime


class Logger(object):
    _instance = None
    _print_to_console = True
    _print_to_file = False
    _file = None

    def __new__(cls, print_to_console: bool = True, print_to_file: bool = False, file_name: str = None):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(print_to_console, print_to_file, file_name)
        return cls._instance

    def _initialize(self, print_to_console: bool = True, print_to_file: bool = False, file_name: str = None):
        self._print_to_console = print_to_console
        if print_to_file:
            if not file_name:
                now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                file_name = f'{now}.chess'
            self._file = open(f'output/{file_name}', 'a')
            self._print_to_file = print_to_file
            self.log('Logger initialized')

    def log(self, text: str, flush: bool = False):
        now = datetime.datetime.now()
        message = f'[{now}] {text}'
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
