from marshmallow import Schema, fields


class Coordinate(Schema):
    CoordinateName = fields.Str()
    CoordinateFormat = fields.Str()
    StationLatitude = fields.Float()
    StationLongitude = fields.Float()


class GeoInfo(Schema):
    Coordinates = fields.List(fields.Nested(Coordinate()))
    StationAltitude = fields.Str()
    CountyName = fields.Str()
    TownName = fields.Str()
    CountyCode = fields.Str()
    TownCode = fields.Str()


class GustInfoOccurredAt(Schema):
    WindDirection = fields.Int()
    DateTime = fields.Str()


class GustInfo(Schema):
    PeakGustSpeed = fields.Float()
    Occurred_at = fields.Nested(GustInfoOccurredAt())


class DailyInfoOccurredAt(Schema):
    DateTime = fields.Str()


class TemperatureInfo(Schema):
    AirTemperature = fields.Float()
    Occurred_at = fields.Nested(DailyInfoOccurredAt())


class DailyHigh(Schema):
    TemperatureInfo = fields.Nested(TemperatureInfo())


class DailyLow(Schema):
    TemperatureInfo = fields.Nested(TemperatureInfo())


class DailyExtreme(Schema):
    DailyHigh = fields.Nested(DailyHigh())
    DailyLow = fields.Nested(DailyLow())


class Now(Schema):
    Precipitation = fields.Int()


class WeatherElement(Schema):
    Weather = fields.Str()
    Now = fields.Nested(Now())
    WindDirection = fields.Int()
    WindSpeed = fields.Float()
    AirTemperature = fields.Float()
    RelativeHumidity = fields.Int()
    AirPressure = fields.Float()
    GustInfo = fields.Nested(GustInfo())
    DailyExtreme = fields.Nested(DailyExtreme())


class ObsTime(Schema):
    DateTime = fields.Str()


class Station(Schema):
    StationName = fields.Str()
    StationId = fields.Str()
    ObsTime = fields.Nested(ObsTime())
    GeoInfo = fields.Nested(GeoInfo())
    WeatherElement = fields.Nested(WeatherElement())


station = {
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
    # obj = Station().load(station)
    obj = DailyExtreme().load(station["WeatherElement"]["DailyExtreme"])
    print(type(obj))
    # assert obj.dump() == station
