import logging
from cwagent.service_layer import unit_of_work
from cwagent.domain import model

logger = logging.getLogger(__name__)


def station_report_by_station_id(station_id: str, uow: unit_of_work.AbstractUnitOfWork) -> dict:
    with uow:
        s = uow.stations.get_by_station_id(station_id=station_id)
        data = {}
        if s:
            data.update({
                'station_id': s.station_id,
                'station_name': s.station_name,
                'geo_info': s.geo_info,
                'observations': len(s.observations),
            })
        uow.commit()
    return data


def station_list_view(uow: unit_of_work.AbstractUnitOfWork) -> list:
    with uow:
        data = []
        for s in uow.stations:
            data.append({
                'station_id': s.station_id,
                'station_name': s.station_name,
                'geo_info': s.geo_info,
                'observations': len(s.observations),
            })
        uow.commit()
    return data
