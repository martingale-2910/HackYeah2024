import click

from hackyeah2024.server import run_dash, run_flask, run_selenium


@click.group()
def main():
    print("Running main CLI")


@main.group()
def run_server():
    print("Running server")


@run_server.command()
def dash():
    print("Running Dash")
    run_dash()


@run_server.command()
def flask():
    print("Running Flask")
    run_flask()


@run_server.command()
def selenium():
    print("Running Selenium")
    run_selenium()


if __name__ == "__main__":
    main()
