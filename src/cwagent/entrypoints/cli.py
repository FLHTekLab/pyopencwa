import os
import time
import click
import json
import math
import logging
import requests
import logging.config as logging_config
from cwagent import config, bootstrap
from cwagent.domain import commands
from cwagent.service_layer import unit_of_work
from cwagent.adapters import cwa_open_api

logging_config.dictConfig(config.logging_config)
logger = logging.getLogger(__name__)
timer_logger = logging.getLogger('api_timer')
bus = bootstrap.bootstrap(
    uow=unit_of_work.JsonFileUnitOfWork(),
    start_orm=False,
    cwa_api=cwa_open_api.CWAOpenAPI()
)


def get_local_storage_filename(data_id: str):
    if not os.path.exists('.cwagent'):
        os.mkdir('.cwagent')
    return f'.cwagent/{data_id}.json'


def get_cwa_api_response(api_url: str, params: dict = None):
    """取得 cwa api 回應，並解計算http request 執行時間"""
    start_time = time.time()
    params = params or {}
    logger.debug(f'api path: {api_url}, params: {params}')
    r = requests.get(
        headers={'Authorization': config.get_cwa_auth_key()},
        url=api_url,
        params=params,
        verify=config.get_api_ssl_check_flag()
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_formatted = format(elapsed_time, '5.2f')  # 将秒数格式化为两位小数
    timer_logger.info(f'{elapsed_time_formatted}, {api_url}')
    logger.debug(f'{r.status_code} {r.reason}')
    if r.text.find("{") == 0:
        response = r.json()
        return response
    else:
        raise cwa_open_api.CwaApiError(r.text)


@click.group()
@click.option('--api-spec-json', default='src/cwa-rest-api-dict.json', help='API specification JSON file')
def cwagentcli(api_spec_json):
    """中央氣象署開放資料平臺之資料擷取API"""
    logger.debug(f'api_spec_json: {api_spec_json}')
    pass


class SwaggerAPICLI(click.MultiCommand):
    CWA_REST_API_DICT: dict

    def list_commands(self, ctx):
        logger.debug(f'list_cmd ctx.parent.params["api_spec_json"]: {ctx.parent.params["api_spec_json"]}')
        with open(ctx.parent.params["api_spec_json"], 'r', encoding='utf-8') as f:
            return sorted(json.load(f).keys())

    def get_command(self, ctx, name):
        # logger.debug(f'get_cmd ctx.parent.params["api_spec_json"]: {ctx.parent.params["api_spec_json"]}')
        with open(ctx.parent.params["api_spec_json"], 'r', encoding='utf-8') as f:
            group = json.load(f)[name]

        @click.group(name=name, help=group['title'])
        def group_command():
            pass

        for api_spec in group['apis']:
            # check if timeFrom parameter in api_spec['parameters']
            time_from_parameter = None
            for parameter in api_spec['parameters']:
                if parameter['name'] == 'timeFrom':
                    # set value yyyy-MM-dd
                    time_from_parameter = time.strftime("%Y-%m-%d", time.localtime())
                    break
            if time_from_parameter:
                @click.command(name=api_spec['dataId'], help=api_spec['summary'])
                @click.option('--api-path', default=api_spec['path'], help='API path')
                @click.option('--data-id', default=api_spec['dataId'], help='API data id')
                @click.option('--description', default=api_spec['description'], help='API description')
                @click.option('--time-from', default=time_from_parameter, help='API timeFrom parameter')
                def sub_command(api_path, data_id, description, time_from):
                    click.echo(f'Running {name} {description} {get_local_storage_filename(data_id)}')

                    response = get_cwa_api_response(
                        api_url=f'{config.get_cwa_uri()}{api_path}',
                        params={'timeFrom': time_from}
                    )
                    with open(get_local_storage_filename(data_id), 'w', encoding='utf-8') as fh:
                        json.dump(response, fh, ensure_ascii=False, indent=4)
                    return response

                group_command.add_command(sub_command)
            else:
                @click.command(name=api_spec['dataId'], help=api_spec['summary'])
                @click.option('--api-path', default=api_spec['path'], help='API path')
                @click.option('--data-id', default=api_spec['dataId'], help='API data id')
                @click.option('--description', default=api_spec['description'], help='API description')
                def sub_command(api_path, data_id, description):
                    click.echo(f'Running {name} {description} {get_local_storage_filename(data_id)}')

                    response = get_cwa_api_response(
                        api_url=f'{config.get_cwa_uri()}{api_path}'
                    )
                    with open(get_local_storage_filename(data_id), 'w', encoding='utf-8') as fh:
                        json.dump(response, fh, ensure_ascii=False, indent=4)
                    return response

                group_command.add_command(sub_command)

        return group_command


@cwagentcli.command(cls=SwaggerAPICLI, help='中央氣象署開放資料平臺之資料擷取API')
@click.pass_context
def api(ctx):
    logger.debug(f'ctx.parent.params["api_spec_json"]: {ctx.parent.params["api_spec_json"]}')
    pass


@cwagentcli.command()
def pull_ob():
    """擷取所有氣象站觀測資料"""
    bus.handle(commands.PullAllStationObservations())
    click.echo('pull all station observations done')


def _print_group_apis(api_spec_json_file, group_name):
    with open(api_spec_json_file, 'r', encoding='utf-8') as f:
        group = json.load(f)[group_name]
    for _api in group['apis']:
        click.echo(f"{_api['dataId']} {_api['summary']}")


@cwagentcli.group(help='天氣警特報')
@click.pass_context
def alert(ctx):
    """天氣警特報"""
    pass


@alert.command()
@click.pass_context
def listall(ctx):
    """列出警特報"""
    click.echo("警特報列表")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='alert')


@cwagentcli.group(help='天文')
@click.pass_context
def astronomy(ctx):
    """天文"""
    pass


@astronomy.command()
@click.pass_context
def listall(ctx):
    """列出天文資料"""
    click.echo("天文資料列表")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='astronomy')


@astronomy.command()
@click.pass_context
def list_sunrise(ctx):
    """列出日出日落資料"""
    click.echo("日出日落資料列表")
    local_file = get_local_storage_filename('A-B0062-001')
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        locations = data['records']['locations']['location']
        locations = sorted(locations, key=lambda _location: _location['time'][0]['SunRiseTime'])
        for location in locations:
            click.echo(
                f"{location['CountyName']} "
                f"{location['time'][0]['Date']} "
                f"SunRise {location['time'][0]['SunRiseTime']} "
                f"SunSet {location['time'][0]['SunSetTime']} "
            )


@cwagentcli.group(help='氣候')
@click.pass_context
def climate(ctx):
    """氣候"""
    pass


@climate.command()
@click.pass_context
def listall(ctx):
    """列出氣候資料"""
    click.echo("氣候資料列表")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='climate')


@cwagentcli.group(help='地震海嘯')
@click.pass_context
def earthquake(ctx):
    """地震海嘯"""
    pass


@earthquake.command()
@click.pass_context
def listall(ctx):
    """列出地震海嘯資料"""
    click.echo("地震海嘯資料列表")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='earthquake')


@cwagentcli.group(help='預報')
@click.pass_context
def forecast(ctx):
    """預報"""
    pass


@forecast.command()
@click.argument('lat', type=float)
@click.argument('lon', type=float)
def forecast_by_geo(lat, lon):
    station = find_nearest_station(target_lat=lat, target_lon=lon)
    county_name = station['GeoInfo']['CountyName']
    local_file = get_local_storage_filename('F-C0032-001')
    logger.debug(f'local_file: {local_file}')
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        locations = data['records']['location']
        location = next((location for location in locations if location['locationName'] == county_name), None)
        if location:
            click.echo(f"{location['locationName']} ")
            elements = location['weatherElement']
            for element in elements:
                click.echo(
                    f"{element['elementName']} "
                    f"{list(element['time'][0]['parameter'].values())}"
                    f"{element['time'][0]['startTime']}-{element['time'][0]['endTime']} "
                )
    else:
        raise


@forecast.command()
@click.pass_context
def listall(ctx):
    """列出預報資料"""
    click.echo("預報資料列表")
    # with open(ctx.parent.parent.params["api_spec_json"], 'r', encoding='utf-8') as f:
    #     group = json.load(f)['forecast']
    # # 列出 group['apis'] 中的所有 dataId
    # for _api in group['apis']:
    #     click.echo(f"{_api['dataId']} {_api['summary']}")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='forecast')


@cwagentcli.group(help='數值預報')
@click.pass_context
def health(ctx):
    """數值預報"""
    pass


@health.command()
@click.pass_context
def listall(ctx):
    """列出數值預報資料"""
    click.echo("數值預報資料列表")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='health')


@cwagentcli.group(help='觀測')
@click.pass_context
def observation(ctx):
    """觀測"""
    # ctx.ensure_object(dict)
    # ctx.obj['api_spec_json'] = ctx.parent.params["api_spec_json"]
    pass


@observation.command()
@click.pass_context
def listall(ctx):
    """列出觀測資料"""
    click.echo("觀測資料列表")
    # with open(ctx.parent.parent.params["api_spec_json"], 'r', encoding='utf-8') as f:
    #     group = json.load(f)['observation']
    # # 列出 group['apis'] 中的所有 dataId
    # for _api in group['apis']:
    #     click.echo(f"{_api['dataId']} {_api['summary']}")
    _print_group_apis(api_spec_json_file=ctx.parent.parent.params["api_spec_json"], group_name='observation')


def find_nearest_station(target_lat, target_lon):
    """
    搜尋目標經緯度最近的氣象站。

    Args:
      target_lat: 目標經緯度緯度。
      target_lon: 目標經緯度經度。

    Returns:
      目標經緯度最近的氣象站資訊。
    """
    local_file = get_local_storage_filename('O-A0001-001')
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        stations = sorted(data['records']['Station'],
                          key=lambda _station: (_station['GeoInfo']['Coordinates'][1]['StationLatitude'],
                                                _station['GeoInfo']['Coordinates'][1]['StationLongitude']))

        # 計算每個氣象站與目標經緯度的距離。
        distances = []
        for station in stations:
            station_lat = station['GeoInfo']['Coordinates'][1]['StationLatitude']
            station_lon = station['GeoInfo']['Coordinates'][1]['StationLongitude']
            distance = math.sqrt((station_lat - target_lat) ** 2 + (station_lon - target_lon) ** 2)
            distances.append(distance)

        # 找出距離最小的氣象站。
        min_index = distances.index(min(distances))
        return stations[min_index]


@observation.command()
@click.argument('lat', type=float)
@click.argument('lon', type=float)
def query_by_geo(lat, lon):
    """以經緯度座標資訊查詢天氣資訊"""
    station = find_nearest_station(target_lat=lat, target_lon=lon)
    click.echo(f"{station['ObsTime']['DateTime']} "
               f"{station['GeoInfo']['CountyName']} "
               f"{station['GeoInfo']['TownName']} "
               f"{station['StationName']} "
               f"{station['WeatherElement']['Weather']} "
               f"{station['WeatherElement']['AirTemperature']}C "
               f"{station['WeatherElement']['RelativeHumidity']}% "
               f"降雨 {station['WeatherElement']['Now']['Precipitation']}mm"
               )
    pass


@observation.command()
@click.argument('data_id')
def list_records(data_id):
    """列出觀測資料"""
    click.echo("觀測資料列表")
    local_file = get_local_storage_filename(data_id)
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data_id == 'O-A0001-001':
            # stations = data['records']['Station']
            stations = sorted(data['records']['Station'],
                              key=lambda station: (station['GeoInfo']['CountyCode'], station['GeoInfo']['TownCode']))
            lines = [
                f"{station['ObsTime']['DateTime']}"
                f"{station['GeoInfo']['CountyName']:>5} "
                f"{station['GeoInfo']['CountyCode']:>5} "
                f"{station['GeoInfo']['TownCode']:>10} "
                f"{station['WeatherElement']['Weather']:>5} "
                f"{station['WeatherElement']['AirTemperature']:>5} "
                f"{station['WeatherElement']['RelativeHumidity']:>5} "
                f"{station['StationId']:<7} "
                f"{station['GeoInfo']['TownName']:<10}"
                f"{station['StationName']:<8}"
                for station in stations
            ]
            for line in lines:
                click.echo(line)


if __name__ == '__main__':
    cwagentcli()
