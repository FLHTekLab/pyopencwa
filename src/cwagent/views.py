import logging
from cwagent.service_layer import unit_of_work

# from cwagent.domain import model

logger = logging.getLogger(__name__)


def station_report_by_station_id(station_id: str, uow: unit_of_work.AbstractUnitOfWork) -> dict:
    with uow:
        s = uow.stations.get_by_station_id(station_id=station_id)
        logger.debug(f'station: {s}')
        data = {
            'name': s.station_name,
            'id': s.station_id,
            'geo_info': s.geo_info,
        }
        if s:
            data.update({
                'observations': [
                    {
                        'date': ob.obs_time.DateTime,
                        'Precipitation': ob.weather_element.Now.Precipitation,
                        'Temperature': ob.weather_element.AirTemperature,
                        'RelativeHumidity': ob.weather_element.RelativeHumidity,
                        'WindDirection': ob.weather_element.WindDirection,
                        'WindSpeed': ob.weather_element.WindSpeed,

                    }
                    for ob in s.observations
                ]
            })
        # uow.commit()
    logger.debug(f'data: {data}')
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
        # uow.commit()
    return data
