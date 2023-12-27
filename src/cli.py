import click
import json

# 读取 JSON 文件
file_path = 'cwa-opendata-api-spec.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


# 动态创建命令组和子命令
class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        # 返回 JSON 文件的第一级键作为命令组
        return data.keys()

    def get_command(self, ctx, name):
        # 返回子命令
        group_data = data.get(name)
        if not group_data:
            return None

        @click.group(name=name, help=f'Commands for {name}')
        def group():
            pass

        for item in group_data:
            cmd_name = item.get('dataId', 'unknown')
            cmd_help = item.get('summary', 'No description available')

            @group.command(name=cmd_name, help=cmd_help)
            def sub_command():
                click.echo(f'Executing {cmd_name} in {name} group')

        return group


# 创建并执行 CLI
cli = ComplexCLI(help='This tool interacts with a nested JSON API specification.')
if __name__ == '__main__':
    cli()
