import datetime
from unittest.mock import patch

import pytest

from twcal.convert import to_gregorian, to_minguo, today
from twcal.twdate import TWDate


class TestToMinguo:
    def test_basic(self):
        result = to_minguo(datetime.date(2026, 3, 20))
        assert result == TWDate(115, 3, 20)

    def test_year_one(self):
        result = to_minguo(datetime.date(1912, 1, 1))
        assert result == TWDate(1, 1, 1)

    def test_before_minguo(self):
        result = to_minguo(datetime.date(1911, 1, 1))
        assert result == TWDate(-1, 1, 1)

    def test_before_minguo_1900(self):
        result = to_minguo(datetime.date(1900, 6, 15))
        assert result == TWDate(-12, 6, 15)

    def test_leap_year(self):
        result = to_minguo(datetime.date(2024, 2, 29))
        assert result == TWDate(113, 2, 29)


class TestToGregorian:
    def test_basic(self):
        result = to_gregorian(TWDate(115, 3, 20))
        assert result == datetime.date(2026, 3, 20)

    def test_year_one(self):
        result = to_gregorian(TWDate(1, 1, 1))
        assert result == datetime.date(1912, 1, 1)

    def test_before_minguo(self):
        result = to_gregorian(TWDate(-1, 1, 1))
        assert result == datetime.date(1911, 1, 1)

    def test_before_minguo_1900(self):
        result = to_gregorian(TWDate(-12, 6, 15))
        assert result == datetime.date(1900, 6, 15)

    def test_leap_year(self):
        result = to_gregorian(TWDate(113, 2, 29))
        assert result == datetime.date(2024, 2, 29)

    def test_roundtrip(self):
        original = datetime.date(1905, 3, 10)
        assert to_gregorian(to_minguo(original)) == original


class TestToday:
    def test_today(self):
        fake_today = datetime.date(2026, 3, 20)
        with patch("twcal.convert.datetime") as mock_dt:
            mock_dt.date.today.return_value = fake_today
            mock_dt.date.side_effect = lambda *args: datetime.date(*args)
            result = today()
        assert result == TWDate(115, 3, 20)
