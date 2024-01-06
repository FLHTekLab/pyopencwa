import logging
from typing import List, Dict, Callable, Type  # , TYPE_CHECKING
from cwagent.domain import commands, events, model
from cwagent.adapters import cwa_open_api
from cwagent.service_layer import unit_of_work

logger = logging.getLogger(__name__)


def pull_all_stations_observation(
        cmd: commands.PullAllStationObservations,
        uow: unit_of_work.AbstractUnitOfWork,
        cwa_api: cwa_open_api.AbstractCWAOpenAPI
):
    with uow:
        logger.debug(f'cmd: {cmd}')
        for _sto in cwa_api.pull_all_stations_observation():
            station = uow.stations.get_by_station_id(station_id=_sto.station_id)
            if station is None:  # new station
                logger.info(
                    f'new station:  '
                    f'{_sto.station_id}, '
                    f'{_sto.station_name}, '
                    f'{_sto.geo_info}'
                )
                uow.stations.add(
                    model.Station(
                        station_id=_sto.station_id,
                        station_name=_sto.station_name,
                        geo_info=_sto.geo_info,
                        observations=[]
                    )
                )
                station = uow.stations.get_by_station_id(station_id=_sto.station_id)
            # update station observation
            station.update_time_observation(
                obs_time=_sto.obs_time,
                weather_element=_sto.weather_element
            )

        uow.commit()


EVENT_HANDLERS = {
    # events.UserRegistered: [fetch_user_dev_list],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    # commands.Register: register_user,
    commands.PullAllStationObservations: pull_all_stations_observation,
}  # type: Dict[Type[commands.Command], Callable]
