import os

import click
import json
import logging
import requests
import logging.config as logging_config
from cwagent import config

logging_config.dictConfig(config.logging_config)
logger = logging.getLogger(__name__)

with open('src/cwa-rest-api-dict.json', 'r', encoding='utf-8') as f:
    CWA_REST_API_DICT = json.load(f)


def get_local_storage_filename(data_id: str):
    if not os.path.exists('.cwagent'):
        os.mkdir('.cwagent')
    return f'.cwagent/{data_id}.json'


@click.group()
def cwagentcli():
    """中央氣象署開放資料平臺之資料擷取API"""
    pass


class CwaApiError(Exception):
    pass


class SwaggerAPICLI(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(CWA_REST_API_DICT.keys())

    # @staticmethod
    # def _check_local_storage():
    #     """檢查是否有 local storage folder .cwagent"""
    #     if not os.path.exists('.cwagent'):
    #         os.mkdir('.cwagent')
    #
    # def _get_local_storage_filename(self, dataId: str):
    #     self._check_local_storage()
    #     return f'.cwagent/{dataId}.json'

    def get_command(self, ctx, name):
        group = CWA_REST_API_DICT[name]

        @click.group(name=name, help=group['title'])
        def group_command():
            pass

        for _api in group['apis']:
            @click.command(name=_api['dataId'], help=_api['summary'])
            def sub_command():
                click.echo(f'Running {name} {_api["dataId"]}')
                logger.debug(f'api path: {config.get_cwa_uri()}{_api["path"]}')
                logger.debug(f'auth_key: {config.get_cwa_auth_key()}')
                r = requests.get(
                    headers={'Authorization': config.get_cwa_auth_key()},
                    url=f'{config.get_cwa_uri()}{_api["path"]}'
                )
                logger.debug(f'{r.status_code} {r.reason}')
                if r.text.find("{") == 0:
                    response = r.json()
                    with open(get_local_storage_filename(_api['dataId']), 'w', encoding='utf-8') as f:
                        json.dump(response, f, ensure_ascii=False, indent=4)
                    return response
                else:
                    raise CwaApiError(r.text)

            group_command.add_command(sub_command)

        return group_command


@cwagentcli.command(cls=SwaggerAPICLI, help='中央氣象署開放資料平臺之資料擷取API')
def api():
    pass


@cwagentcli.group(help='天氣警特報')
def alert():
    """天氣警特報"""
    pass


@alert.command()
def listall():
    """列出警特報"""
    click.echo("警特報列表")


@cwagentcli.group(help='天文')
def astronomy():
    """天文"""
    pass


@astronomy.command()
def listall():
    """列出天文資料"""
    click.echo("天文資料列表")


@cwagentcli.group(help='氣候')
def climate():
    """氣候"""
    pass


@climate.command()
def listall():
    """列出氣候資料"""
    click.echo("氣候資料列表")


@cwagentcli.group(help='地震海嘯')
def earthquake():
    """地震海嘯"""
    pass


@earthquake.command()
def listall():
    """列出地震海嘯資料"""
    click.echo("地震海嘯資料列表")


@cwagentcli.group(help='預報')
def forecast():
    """預報"""
    pass


@forecast.command()
def listall():
    """列出預報資料"""
    click.echo("預報資料列表")


@cwagentcli.group(help='數值預報')
def health():
    """數值預報"""
    pass


@health.command()
def listall():
    """列出數值預報資料"""
    click.echo("數值預報資料列表")


@cwagentcli.group(help='觀測')
def observation():
    """觀測"""
    pass


@observation.command()
def listall():
    """列出觀測資料"""
    click.echo("觀測資料列表")


if __name__ == '__main__':
    cwagentcli()
