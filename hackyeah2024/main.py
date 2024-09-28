import click

from hackyeah2024.server import run_server


@click.group()
def main():
    print("Running main CLI")


@main.command()
def dummy():
    print("Running a dummy script")


@main.command()
def server():
    print("Running server")
    run_server()


if __name__ == "__main__":
    main()
