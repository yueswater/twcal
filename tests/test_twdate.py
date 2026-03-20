import pytest

from twcal.twdate import TWDate


class TestTWDate:
    def test_creation(self):
        d = TWDate(115, 3, 20)
        assert d.year == 115
        assert d.month == 3
        assert d.day == 20

    def test_equality(self):
        assert TWDate(115, 3, 20) == TWDate(115, 3, 20)

    def test_inequality(self):
        assert TWDate(115, 3, 20) != TWDate(114, 3, 20)

    def test_year_zero_raises(self):
        with pytest.raises(ValueError):
            TWDate(0, 1, 1)

    def test_invalid_month_raises(self):
        with pytest.raises(ValueError):
            TWDate(115, 13, 1)

    def test_invalid_day_raises(self):
        with pytest.raises(ValueError):
            TWDate(115, 2, 30)

    def test_before_minguo(self):
        d = TWDate(-1, 1, 1)
        assert d.year == -1

    def test_ordering(self):
        assert TWDate(114, 1, 1) < TWDate(115, 1, 1)
        assert TWDate(115, 1, 1) > TWDate(114, 12, 31)
        assert TWDate(115, 3, 1) <= TWDate(115, 3, 2)


class TestStr:
    def test_str(self):
        assert str(TWDate(115, 3, 20)) == "民國115年3月20日"

    def test_str_before_minguo(self):
        assert str(TWDate(-1, 1, 1)) == "民國前1年1月1日"


class TestFromShortString:
    def test_basic(self):
        assert TWDate.from_short_string("1150320") == TWDate(115, 3, 20)

    def test_single_digit_year(self):
        assert TWDate.from_short_string("10101") == TWDate(1, 1, 1)

    def test_roundtrip(self):
        d = TWDate(115, 3, 2)
        assert TWDate.from_short_string(d.to_short_string()) == d

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            TWDate.from_short_string("1151301")


class TestToString:
    def test_basic(self):
        assert TWDate(115, 3, 20).to_string() == "民國115年3月20日"

    def test_single_digit(self):
        assert TWDate(1, 1, 1).to_string() == "民國1年1月1日"

    def test_before_minguo(self):
        assert TWDate(-1, 1, 1).to_string() == "民國前1年1月1日"

    def test_before_minguo_deep(self):
        assert TWDate(-12, 6, 15).to_string() == "民國前12年6月15日"


class TestToShortString:
    def test_basic(self):
        assert TWDate(115, 3, 20).to_short_string() == "1150320"

    def test_zero_padded(self):
        assert TWDate(115, 3, 2).to_short_string() == "1150302"

    def test_single_digit_year(self):
        assert TWDate(1, 1, 1).to_short_string() == "10101"
