import json


class SummaryWriter(object):
    _instance = None
    _file = None
    _dicts_written = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SummaryWriter, cls).__new__(cls)
            # cls._instance._initialize(file_name)
        return cls._instance

    def initialize(self, file_name: str):
        self._file = open(f'../../output/{file_name}', 'w')
        self._file.write('[')

    def write_summary(self, summary: dict, flush: bool = True):
        if self._dicts_written > 0:
            self._file.write(', ')
        json_text = json.dumps(summary)
        self._file.write(json_text)
        if flush:
            self._file.flush()
        self._dicts_written += 1

    def flush(self):
        self._file.flush()

    def close(self):
        self._file.write(']')
        self._file.flush()
        self._file.close()
