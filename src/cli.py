import click
import json

with open('cwa-rest-api-dict.json', 'r') as f:
    CWA_REST_API_DICT = json.load(f)

class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(CWA_REST_API_DICT.keys())

    def get_command(self, ctx, name):
        group = CWA_REST_API_DICT[name]

        @click.group(name=name, help=group['title'])
        def group_command():
            pass

        for api in group['apis']:
            @click.command(name=api['dataId'], help=api['summary'])
            def sub_command():
                click.echo(f'Running {name} {api["dataId"]}')

            group_command.add_command(sub_command)

        return group_command


@click.command(cls=CLI, help='中央氣象署開放資料平臺之資料擷取API')
def cli():
    pass


if __name__ == '__main__':
    cli()
