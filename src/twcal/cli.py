"""CLI interface for twcal."""

import datetime

import click

from twcal import convert as twcal_convert
from twcal.twdate import TWDate


@click.group()
def main():
    """Convert between Gregorian and Taiwanese (Minguo) calendar."""
    pass


@main.command()
def now():
    """Show today's date in Minguo format."""
    click.echo(twcal_convert.today())


@main.command()
@click.argument("date")
@click.option("--to-gregorian", "-g", is_flag=True, help="Convert Minguo to Gregorian.")
def convert(date, to_gregorian):
    """Convert a date between Gregorian and Minguo.

    DATE format: YYYY-MM-DD (Gregorian) or YYY-MM-DD (Minguo with -g flag).
    """
    parts = date.split("-")
    if to_gregorian:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        result = twcal_convert.to_gregorian(TWDate(year, month, day))
        click.echo(result.isoformat())
    else:
        d = datetime.date.fromisoformat(date)
        click.echo(twcal_convert.to_minguo(d))
