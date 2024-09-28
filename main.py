import click

from server import run_dash, run_flask

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

if __name__ == "__main__":
    main()
