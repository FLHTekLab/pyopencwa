import os
import json
from typing import List
import logging
from cwagent.domain import model


logger = logging.getLogger(__name__)


class FileDatastore:
    _stations = []  # type: List['model.Station']

    def __init__(self, file: str):
        self._file = file
        if os.path.exists(file):
            with open(self._file, 'r') as fh:
                content = json.loads(fh.read())
                if not isinstance(content, list):
                    raise ValueError
            self._stations = [model.Station.load(data) for data in content]
        else:
            self._stations = []

    def commit(self):
        self._save()

    def _save(self):
        with open(self._file, 'w') as fh:
            content = [model.Station.dump(u) for u in self._stations]
            fh.write(json.dumps(content, indent=2, ensure_ascii=False))


def session_factory(file: str):
    return FileDatastore(file)
