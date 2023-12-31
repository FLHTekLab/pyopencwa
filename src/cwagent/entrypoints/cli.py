import os
import time
import click
import json
import logging
import requests
import logging.config as logging_config
from cwagent import config

logging_config.dictConfig(config.logging_config)
logger = logging.getLogger(__name__)
timer_logger = logging.getLogger('api_timer')


class CwaApiError(Exception):
    pass


def get_local_storage_filename(data_id: str):
    if not os.path.exists('.cwagent'):
        os.mkdir('.cwagent')
    return f'.cwagent/{data_id}.json'


def get_cwa_api_response(api_url: str):
    """取得 cwa api 回應，並解計算http request 執行時間"""
    start_time = time.time()
    logger.debug(f'api path: {api_url}')
    r = requests.get(
        headers={'Authorization': config.get_cwa_auth_key()},
        url=api_url
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
        raise CwaApiError(r.text)


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
        logger.debug(f'get_cmd ctx.parent.params["api_spec_json"]: {ctx.parent.params["api_spec_json"]}')
        with open(ctx.parent.params["api_spec_json"], 'r', encoding='utf-8') as f:
            group = json.load(f)[name]

        @click.group(name=name, help=group['title'])
        def group_command():
            pass

        for _api in group['apis']:
            @click.command(name=_api['dataId'], help=_api['summary'])
            @click.option('--api-path', default=_api['path'], help='API path')
            @click.option('--data-id', default=_api['dataId'], help='API data id')
            @click.option('--description', default=_api['description'], help='API description')
            def sub_command(api_path, data_id, description):
                click.echo(f'Running {name} {description} {get_local_storage_filename(data_id)}')
                response = get_cwa_api_response(api_url=f'{config.get_cwa_uri()}{api_path}')
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
