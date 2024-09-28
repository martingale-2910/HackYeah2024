import click


@click.group()
def main():
    print('Running main CLI')


@main.command()
def dummy():
    print('Running a dummy script')


@main.command()
def server():
    print('Running server')


if __name__ == '__main__':
    main()
