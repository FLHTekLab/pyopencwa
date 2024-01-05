import os
import logging
import json
from typing import List
from cwagent import bootstrap
from cwagent.service_layer import unit_of_work
from cwagent.adapters import cwa_open_api, repository
from cwagent.domain import commands, model

logger = logging.getLogger(__name__)
JSON_FILE = '.teststore.json'


class FakeCWAOpenAPI(cwa_open_api.AbstractCWAOpenAPI):

    def pull_all_stations_observation(self) -> List[model.StationObservation]:
        with open('./tests/unit/O-A0001-001.json') as fh:
            content = json.loads(fh.read())
            if not isinstance(content.get('records').get('Station'), list):
                raise ValueError
        return [model.StationObservation.load(dto) for dto in content.get('records').get('Station')]


class MemoryRepository(repository.AbstractRepository):
    _stations = []  # type: List['model.Station']

    def _get_by_station_id(self, station_id: str) -> model.Station:
        return next((s for s in self._stations if s.station_id == station_id), None)

    def _add(self, station_id: str, station_name: str, geo_info: dict):
        station = model.Station(
            station_id=station_id,
            station_name=station_name,
            geo_info=model.GeoInfo.load(geo_info)
        )
        self._stations.append(station)
        return station


class MemoryUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.stations = MemoryRepository()
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass


def bootstrap_test_app():
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)
    return bootstrap.bootstrap(
        # uow=unit_of_work.JsonFileUnitOfWork(json_file=JSON_FILE),
        uow=MemoryUnitOfWork(),
        start_orm=False,
        cwa_api=FakeCWAOpenAPI()
    )


def test_pull_all_stations_observation():
    bus = bootstrap_test_app()
    bus.handle(commands.PullAllStationsObservation())

    s = bus.uow.stations.get_by_station_id(station_id='C0R890')
    assert s.station_name == '山海'
    assert len(s.observations) == 1
    assert isinstance(s.observations[0], model.TimeObservation)
