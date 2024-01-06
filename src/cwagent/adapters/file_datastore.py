import os
import json
from typing import List
import logging
from cwagent.domain import model


logger = logging.getLogger(__name__)


class FileDatastore:
    _stations = []  # type: List['model.Station']

    def count(self) -> int:
        return len(self._stations)

    def delete(self, station_id: str):
        n, s = next(((n, s) for n, s in enumerate(self._stations) if s.station_id == station_id), (None, None))
        if s is None:
            m = f'station_id {station_id} not exist'
            logger.warning(m)
            raise ValueError(m)
        else:
            del self._stations[n]
            logger.info(f'delete station {s}')
        self._save()

    def get_by_station_id(self, station_id: str) -> model.Station:
        return next((u for u in self._stations if u.station_id == station_id), None)

    def add(self, s: model.Station):
        if self.get_by_station_id(station_id=s.station_id):
            raise ValueError(f'station_id {s.station_id} already exist')
        self._stations.append(s)
        return s

    def __init__(self, file: str):
        self._file = file
        self._index = 0  # 新增一個 index 來追蹤迭代的進度
        if os.path.exists(file):
            with open(self._file, 'r') as fh:
                content = json.loads(fh.read())
                if not isinstance(content, list):
                    raise ValueError
            self._stations = [model.Station.load(data) for data in content]
        else:
            self._stations = []

    def __iter__(self):
        return iter(self._stations)
    
    def __next__(self):
        if self._index >= len(self._stations):
            raise StopIteration
        else:
            s = self._stations[self._index]
            self._index += 1
            return s


    def commit(self):
        self._save()

    def _save(self):
        with open(self._file, 'w') as fh:
            content = [s.dump() for s in self._stations]
            fh.write(json.dumps(content, indent=2, ensure_ascii=False))


def session_factory(file: str):
    return FileDatastore(file)
