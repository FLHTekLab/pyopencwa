"""
dataID: O-A0001-001
summary: 自動氣象站-氣象觀測資料
"""
from typing import List
from dataclasses import dataclass
from marshmallow import Schema, fields, post_load

from cwagent import config
from cwagent.domain import events


@dataclass
class Coordinate:
    CoordinateName: str
    CoordinateFormat: str
    StationLatitude: float
    StationLongitude: float

    @classmethod
    def load(cls, data: dict):
        _schema = CoordinateSchema()
        return _schema.load(data)

    def dump(self):
        _schema = CoordinateSchema()
        return _schema.dump(self)


class CoordinateSchema(Schema):
    CoordinateName = fields.Str()
    CoordinateFormat = fields.Str()
    StationLatitude = fields.Float()
    StationLongitude = fields.Float()

    @post_load
    def make_coordinate(self, data, **kwargs):
        return Coordinate(**data)


@dataclass
class GeoInfo:
    Coordinates: list
    StationAltitude: str
    CountyName: str
    TownName: str
    CountyCode: str
    TownCode: str

    def __repr__(self):
        return f'{self.CountyName}, {self.TownName}'

    @classmethod
    def load(cls, data: dict):
        _schema = GeoInfoSchema()
        return _schema.load(data)

    def dump(self):
        _schema = GeoInfoSchema()
        return _schema.dump(self)


class GeoInfoSchema(Schema):
    Coordinates = fields.List(fields.Nested(CoordinateSchema()))
    StationAltitude = fields.Str()
    CountyName = fields.Str()
    TownName = fields.Str()
    CountyCode = fields.Str()
    TownCode = fields.Str()

    @post_load
    def make_geo_info(self, data, **kwargs):
        return GeoInfo(**data)


@dataclass
class GustOccurredAt:
    WindDirection: int
    DateTime: str

    @classmethod
    def load(cls, data: dict):
        _schema = GustOccurredAtSchema()
        return _schema.load(data)

    def dump(self):
        _schema = GustOccurredAtSchema()
        return _schema.dump(self)


class GustOccurredAtSchema(Schema):
    WindDirection = fields.Int()
    DateTime = fields.Str()

    @post_load
    def make_gust_occurred_at(self, data, **kwargs):
        return GustOccurredAt(**data)


@dataclass
class GustInfo:
    PeakGustSpeed: float
    Occurred_at: GustOccurredAt

    @classmethod
    def load(cls, data: dict):
        _schema = GustInfoSchema()
        return _schema.load(data)

    def dump(self):
        _schema = GustInfoSchema()
        return _schema.dump(self)


class GustInfoSchema(Schema):
    PeakGustSpeed = fields.Float()
    Occurred_at = fields.Nested(GustOccurredAtSchema())

    @post_load
    def make_gust_info(self, data, **kwargs):
        return GustInfo(**data)


@dataclass
class DailyInfoOccurredAt:
    DateTime: str

    @classmethod
    def load(cls, data: dict):
        _schema = DailyInfoOccurredAtSchema()
        return _schema.load(data)

    def dump(self):
        _schema = DailyInfoOccurredAtSchema()
        return _schema.dump(self)


class DailyInfoOccurredAtSchema(Schema):
    DateTime = fields.Str()

    @post_load
    def make_daily_info_occurred_at(self, data, **kwargs):
        return DailyInfoOccurredAt(**data)


@dataclass
class TemperatureInfo:
    AirTemperature: float
    Occurred_at: DailyInfoOccurredAt

    @classmethod
    def load(cls, data: dict):
        _schema = TemperatureInfoSchema()
        return _schema.load(data)

    def dump(self):
        _schema = TemperatureInfoSchema()
        return _schema.dump(self)


class TemperatureInfoSchema(Schema):
    AirTemperature = fields.Float()
    Occurred_at = fields.Nested(DailyInfoOccurredAtSchema())

    @post_load
    def make_temperature_info(self, data, **kwargs):
        return TemperatureInfo(**data)


@dataclass
class DailyHigh:
    TemperatureInfo: TemperatureInfo

    @classmethod
    def load(cls, data: dict):
        _schema = DailyHighSchema()
        return _schema.load(data)

    def dump(self):
        _schema = DailyHighSchema()
        return _schema.dump(self)


class DailyHighSchema(Schema):
    TemperatureInfo = fields.Nested(TemperatureInfoSchema())

    @post_load
    def make_daily_high(self, data, **kwargs):
        return DailyHigh(**data)


@dataclass
class DailyLow:
    TemperatureInfo: TemperatureInfo

    @classmethod
    def load(cls, data: dict):
        _schema = DailyLowSchema()
        return _schema.load(data)

    def dump(self):
        _schema = DailyLowSchema()
        return _schema.dump(self)


class DailyLowSchema(Schema):
    TemperatureInfo = fields.Nested(TemperatureInfoSchema())

    @post_load
    def make_daily_low(self, data, **kwargs):
        return DailyLow(**data)


@dataclass
class DailyExtreme:
    DailyHigh: DailyHigh
    DailyLow: DailyLow

    @classmethod
    def load(cls, data: dict):
        _schema = DailyExtremeSchema()
        return _schema.load(data)

    def dump(self):
        _schema = DailyExtremeSchema()
        return _schema.dump(self)


class DailyExtremeSchema(Schema):
    DailyHigh = fields.Nested(DailyHighSchema())
    DailyLow = fields.Nested(DailyLowSchema())

    @post_load
    def make_daily_extreme(self, data, **kwargs):
        return DailyExtreme(**data)


@dataclass
class Now:
    Precipitation: int  # 降雨量

    @classmethod
    def load(cls, data: dict):
        _schema = NowSchema()
        return _schema.load(data)

    def dump(self):
        _schema = NowSchema()
        return _schema.dump(self)


class NowSchema(Schema):
    Precipitation = fields.Int()

    @post_load
    def make_now(self, data, **kwargs):
        return Now(**data)


@dataclass
class WeatherElement:
    Weather: str
    Now: Now
    WindDirection: int
    WindSpeed: float
    AirTemperature: float
    RelativeHumidity: int
    AirPressure: float
    GustInfo: GustInfo
    DailyExtreme: DailyExtreme

    @classmethod
    def load(cls, data: dict):
        _schema = WeatherElementSchema()
        return _schema.load(data)

    def dump(self):
        _schema = WeatherElementSchema()
        return _schema.dump(self)


class WeatherElementSchema(Schema):
    Weather = fields.Str()
    Now = fields.Nested(NowSchema())
    WindDirection = fields.Int()
    WindSpeed = fields.Float()
    AirTemperature = fields.Float()
    RelativeHumidity = fields.Int()
    AirPressure = fields.Float()
    GustInfo = fields.Nested(GustInfoSchema())
    DailyExtreme = fields.Nested(DailyExtremeSchema())

    @post_load
    def make_weather_element(self, data, **kwargs):
        return WeatherElement(**data)


@dataclass
class ObsTime:
    DateTime: str

    @classmethod
    def load(cls, data: dict):
        _schema = ObsTimeSchema()
        return _schema.load(data)

    def dump(self):
        _schema = ObsTimeSchema()
        return _schema.dump(self)


class ObsTimeSchema(Schema):
    DateTime = fields.Str()

    @post_load
    def make_obs_time(self, data, **kwargs):
        return ObsTime(**data)


class StationObservation:

    def __init__(
            self,
            station_name: str,
            station_id: str,
            obs_time: ObsTime,
            geo_info: GeoInfo,
            weather_element: WeatherElement
    ):
        self.station_name = station_name
        self.station_id = station_id
        self.obs_time = obs_time
        self.geo_info = geo_info
        self.weather_element = weather_element
        # self.events = []  # type: List[events.Event]

    def __repr__(self):
        return f'<Station ({self.station_name}, {self.station_id}, {self.geo_info})>'

    @classmethod
    def load(cls, data: dict):
        _schema = StationObservationSchema()
        return _schema.load(data)

    def dump(self):
        _schema = StationObservationSchema()
        return _schema.dump(self)


class StationObservationSchema(Schema):
    station_name = fields.Str(data_key='StationName')
    station_id = fields.Str(data_key='StationId')
    obs_time = fields.Nested(ObsTimeSchema(), data_key='ObsTime')
    geo_info = fields.Nested(GeoInfoSchema(), data_key='GeoInfo')
    weather_element = fields.Nested(WeatherElementSchema(), data_key='WeatherElement')

    @post_load
    def make_station(self, data, **kwargs):
        return StationObservation(**data)


class TimeObservationSchema(Schema):
    obs_time = fields.Nested(ObsTimeSchema(), data_key='ObsTime')
    weather_element = fields.Nested(WeatherElementSchema(), data_key='WeatherElement')

    @post_load
    def make_time_observation(self, data, **kwargs):
        return TimeObservation(**data)


class TimeObservation:
    def __init__(self, obs_time: ObsTime, weather_element: WeatherElement):
        self.obs_time = obs_time
        self.weather_element = weather_element

    @classmethod
    def load(cls, data: dict):
        _schema = TimeObservationSchema()
        return _schema.load(data)

    def dump(self):
        _schema = TimeObservationSchema()
        return _schema.dump(self)


class StationSchema(Schema):
    station_id = fields.Str(data_key='StationId')
    station_name = fields.Str(data_key='StationName')
    geo_info = fields.Nested(GeoInfoSchema(), data_key='GeoInfo')
    observations = fields.List(fields.Nested(TimeObservationSchema()), data_key='Observations', load_default=[])

    @post_load
    def make_station(self, data, **kwargs):
        return Station(**data)


class Station:

    def update_time_observation(self, obs_time: ObsTime, weather_element: WeatherElement):
        time_observation = TimeObservation(obs_time=obs_time, weather_element=weather_element)
        if len(self.observations) >= config.get_max_station_observation_count():
            del self.observations[0]
        self.observations.append(time_observation)

    def __repr__(self):
        return f'<Station ({self.station_id}, {self.station_name}, {self.geo_info}, {len(self.observations)} records)>'

    def __eq__(self, other):
        if not isinstance(other, Station):
            return False
        return self.station_id == other.station_id

    def __hash__(self):
        return hash((self.station_id, self.station_name))

    def __init__(
            self,
            station_id: str,
            station_name: str,
            geo_info: GeoInfo,
            observations: List[TimeObservation]
    ):
        self.station_id = station_id
        self.station_name = station_name
        self.geo_info = geo_info
        self.observations = observations  # type: List[TimeObservation]
        self.events = []  # type: List[events.Event]

    @classmethod
    def load(cls, data: dict):
        _schema = StationSchema()
        return _schema.load(data)

    def dump(self):
        _schema = StationSchema()
        return _schema.dump(self)


_station_observation = {
    "StationName": "鼻頭",
    "StationId": "C0R860",
    "ObsTime": {
        "DateTime": "2023-12-26T22:00:00+08:00"
    },
    "GeoInfo": {
        "Coordinates": [
            {
                "CoordinateName": "TWD67",
                "CoordinateFormat": "decimal degrees",
                "StationLatitude": 22.106108,
                "StationLongitude": 120.88986
            },
            {
                "CoordinateName": "WGS84",
                "CoordinateFormat": "decimal degrees",
                "StationLatitude": 22.1043,
                "StationLongitude": 120.89788
            }
        ],
        "StationAltitude": "31.0",
        "CountyName": "屏東縣",
        "TownName": "滿州鄉",
        "CountyCode": "10013",
        "TownCode": "10013240"
    },
    "WeatherElement": {
        "Weather": "陰",
        "Now": {
            "Precipitation": 0
        },
        "WindDirection": 17,
        "WindSpeed": 9.8,
        "AirTemperature": 22,
        "RelativeHumidity": 64,
        "AirPressure": 1021.1,
        "GustInfo": {
            "PeakGustSpeed": -99,
            "Occurred_at": {
                "WindDirection": -99,
                "DateTime": "-99"
            }
        },
        "DailyExtreme": {
            "DailyHigh": {
                "TemperatureInfo": {
                    "AirTemperature": 22.4,
                    "Occurred_at": {
                        "DateTime": "2023-12-26T20:20:00+08:00"
                    }
                }
            },
            "DailyLow": {
                "TemperatureInfo": {
                    "AirTemperature": 19.8,
                    "Occurred_at": {
                        "DateTime": "2023-12-26T00:10:00+08:00"
                    }
                }
            }
        }
    }
}

if __name__ == '__main__':
    obj = StationObservationSchema().load(_station_observation)
    # obj = DailyExtremeSchema().load(station["WeatherElement"]["DailyExtreme"])
    # print(type(obj))
    assert isinstance(obj, StationObservation)
    assert obj.dump() == _station_observation
