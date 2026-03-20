"""Conversion functions between Gregorian and Minguo calendar."""

import datetime

from twcal.constants import MINGUO_OFFSET
from twcal.twdate import TWDate


def to_minguo(d: datetime.date) -> TWDate:
    """Convert a Gregorian date to Minguo calendar format (ROC year)."""
    year = d.year - MINGUO_OFFSET
    if year <= 0:
        year -= 1
    return TWDate(year, d.month, d.day)


def to_gregorian(d: TWDate) -> datetime.date:
    """Convert Minguo calendar format (ROC year) to a Gregorian date."""
    year = d.year + MINGUO_OFFSET
    if d.year < 0:
        year += 1
    return datetime.date(year, d.month, d.day)


def today() -> TWDate:
    """Get today's date in Minguo calendar format."""
    return to_minguo(datetime.date.today())
