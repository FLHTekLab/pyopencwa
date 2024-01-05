import os
import json
from typing import List
import logging
from cwagent.domain import model


logger = logging.getLogger(__name__)


class FileDatastore:
    _stations = []  # type: List['model.Station']

    def get_by_station_id(self, station_id: str) -> model.Station:
        return next((u for u in self._stations if u.station_id == station_id), None)

    def add(self, station_id: str, station_name: str, geo_info_dto: dict) -> model.Station:
        if self.get_by_station_id(station_id=station_id):
            raise ValueError(f'station_id {station_id} already exist')

        s = model.Station(
            station_id=station_id,
            station_name=station_name,
            geo_info=model.observation.GeoInfo.load(geo_info_dto)
        )
        self._stations.append(s)
        return s

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
            content = [s.dump() for s in self._stations]
            fh.write(json.dumps(content, indent=2, ensure_ascii=False))


def session_factory(file: str):
    return FileDatastore(file)
