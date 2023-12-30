import click
import json

with open('cwa-rest-api-dict.json', 'r', encoding='utf-8') as f:
    CWA_REST_API_DICT = json.load(f)


@click.group()
def cwagentcli():
    """中央氣象署開放資料平臺之資料擷取API"""
    pass


class SwaggerAPICLI(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(CWA_REST_API_DICT.keys())

    def get_command(self, ctx, name):
        group = CWA_REST_API_DICT[name]

        @click.group(name=name, help=group['title'])
        def group_command():
            pass

        for _api in group['apis']:
            @click.command(name=_api['dataId'], help=_api['summary'])
            def sub_command():
                click.echo(f'Running {name} {_api["dataId"]}')

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
