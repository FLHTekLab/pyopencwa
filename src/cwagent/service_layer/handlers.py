import logging
from typing import List, Dict, Callable, Type  # , TYPE_CHECKING
from cwagent.domain import commands, events, model
from cwagent.adapters import cwa_open_api
from cwagent.service_layer import unit_of_work

logger = logging.getLogger(__name__)


def pull_all_stations_observation(
        cmd: commands.PullAllStationsObservation,
        uow: unit_of_work.AbstractUnitOfWork,
        cwa_api: cwa_open_api.AbstractCWAOpenAPI
):
    with uow:
        logger.debug(f'cmd: {cmd}')
        for station_observation in cwa_api.pull_all_stations_observation():
            station = uow.stations.get_by_station_id(station_id=station_observation.station_id)
            if station is None:  # new station
                logger.info(f'new station:  {station_observation.station_id}, {station_observation.station_name}, '
                            f'{station_observation.geo_info}')

                station = uow.stations.add(
                    station_id=station_observation.station_id,
                    station_name=station_observation.station_name,
                    geo_info=station_observation.geo_info.dump()
                )
            # update station observation
            station.update_time_observation(
                obs_time=station_observation.obs_time,
                weather_element=station_observation.weather_element
            )

        uow.commit()


EVENT_HANDLERS = {
    # events.UserRegistered: [fetch_user_dev_list],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    # commands.Register: register_user,
    commands.PullAllStationsObservation: pull_all_stations_observation,
}  # type: Dict[Type[commands.Command], Callable]
