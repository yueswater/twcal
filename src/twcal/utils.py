import datetime


def validate_minguo_date(year: int, month: int, day: int) -> None:
    if year == 0:
        raise ValueError("民國0年不存在")
    gregorian_year = year + 1911 if year > 0 else year + 1912
    datetime.date(gregorian_year, month, day)
