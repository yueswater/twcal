# twcal

<img src="https://img.shields.io/badge/Python-%3E%3D3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

[中文版](README_zh-TW.md)

A simple Python package to convert between the Gregorian calendar and the Taiwanese (Minguo) calendar.

## Installation

```bash
pip install twcal
```

## Usage

### Create a Minguo date

```python
from twcal import TWDate

d = TWDate(115, 3, 20)  # 民國115年3月20日
```

### Convert between Gregorian and Minguo

```python
import datetime
from twcal import to_minguo, to_gregorian

# Gregorian -> Minguo
tw = to_minguo(datetime.date(2026, 3, 20))
# TWDate(year=115, month=3, day=20)

# Minguo -> Gregorian
gd = to_gregorian(tw)
# datetime.date(2026, 3, 20)
```

### Get today's date in Minguo format

```python
from twcal import today

d = today()
print(d)  # 民國115年3月20日
```

### Format as string

```python
d = TWDate(115, 3, 20)

d.to_string()        # '民國115年3月20日'
d.to_short_string()  # '1150320'
str(d)               # '民國115年3月20日'
```

### Parse from short string

```python
d = TWDate.from_short_string("1150320")
# TWDate(year=115, month=3, day=20)
```

### Pre-Minguo dates

```python
import datetime
from twcal import to_minguo

d = to_minguo(datetime.date(1911, 1, 1))
# TWDate(year=-1, month=1, day=1)

print(d)  # 民國前1年1月1日
```

### Comparison

```python
from twcal import TWDate

TWDate(115, 1, 1) > TWDate(114, 12, 31)   # True
TWDate(114, 1, 1) < TWDate(115, 1, 1)     # True
```

### Validation

```python
from twcal import TWDate

TWDate(0, 1, 1)    # ValueError: 民國0年不存在
TWDate(115, 2, 30) # ValueError: day is out of range for month
```

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software for any purpose, including commercial use.
