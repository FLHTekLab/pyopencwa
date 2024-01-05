import abc
import logging
from typing import Set, List
from cwagent.domain import model

logger = logging.getLogger(__name__)


class AbstractRepository(abc.ABC):

    def __init__(self):
        self.seen = set()  # type: Set[model.Station]

    def get_by_station_id(self, station_id: str) -> model.Station:
        s = self._get_by_station_id(station_id=station_id)
        if s:
            self.seen.add(s)
        return s

    def add(self, station_id: str, station_name: str, geo_info: dict) -> model.Station:
        if self.get_by_station_id(station_id=station_id):
            raise ValueError(f'station_id {station_id} already exist')

        s = self._add(station_id=station_id, station_name=station_name, geo_info=geo_info)
        return s

    @abc.abstractmethod
    def _get_by_station_id(self, station_id: str) -> model.Station:
        raise NotImplementedError

    @abc.abstractmethod
    def _add(self, station_id: str, station_name: str, geo_info: dict):
        raise NotImplementedError


class JsonFileRepository(AbstractRepository):

    def _get_by_station_id(self, station_id: str) -> model.Station:
        return self.session.get_by_station_id(station_id=station_id)

    def _add(self, station_id: str, station_name: str, geo_info: dict) -> model.Station:
        return self.session.add(
            station_id=station_id,
            station_name=station_name,
            geo_info_dto=geo_info
        )

    def __init__(self, session):
        super().__init__()
        self.session = session  # type:'file_datastore.FileDatastore'


# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session):
#         super().__init__()
#         self.session = session
