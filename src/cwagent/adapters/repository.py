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

    # def add(self, station_id: str, station_name: str, geo_info: dict) -> model.Station:
    #     if self.get_by_station_id(station_id=station_id):
    #         raise ValueError(f'station_id {station_id} already exist')
    #
    #     s = self._add(station_id=station_id, station_name=station_name, geo_info=geo_info)
    #     return s

    def add(self, s: model.Station):
        if self.get_by_station_id(station_id=s.station_id):
            raise ValueError(f'station_id {s.station_id} already exist')
        self._add(s=s)
        self.seen.add(s)

    def delete(self, station_id: str):
        if not self.get_by_station_id(station_id=station_id):
            raise ValueError(f'station_id {station_id} does not exist')
        self._delete(station_id=station_id)

    def count(self) -> int:
        return self._count()

    @abc.abstractmethod
    def _get_by_station_id(self, station_id: str) -> model.Station:
        raise NotImplementedError

    # @abc.abstractmethod
    # def _add(self, station_id: str, station_name: str, geo_info: dict):
    #     raise NotImplementedError
    @abc.abstractmethod
    def _add(self, s: model.Station):
        raise NotImplementedError

    @abc.abstractmethod
    def _delete(self, station_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def _count(self) -> int:
        raise NotImplementedError


class JsonFileRepository(AbstractRepository):

    def _get_by_station_id(self, station_id: str) -> model.Station:
        return self.session.get_by_station_id(station_id=station_id)

    def _add(self, s: model.Station):
        return self.session.add(s=s)

    def _delete(self, station_id: str):
        return self.session.delete(station_id=station_id)

    def _count(self) -> int:
        return self.session.count()

    def __init__(self, session):
        super().__init__()
        self.session = session  # type:'file_datastore.FileDatastore'

# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session):
#         super().__init__()
#         self.session = session
