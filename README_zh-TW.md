# twdate

<img src="https://img.shields.io/badge/Python-%3E%3D3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

[English](README.md)

一個簡單的 Python 套件，用於格里曆（西曆）與臺灣民國曆之間的轉換。

## 安裝

```bash
pip install twdate
```

## 使用教學

### 建立民國日期

```python
from twcal import TWDate

d = TWDate(115, 3, 20)  # 民國115年3月20日
```

### 格里曆與民國曆互轉

```python
import datetime
from twcal import to_minguo, to_gregorian

# 格里曆 -> 民國
tw = to_minguo(datetime.date(2026, 3, 20))
# TWDate(year=115, month=3, day=20)

# 民國 -> 格里曆
gd = to_gregorian(tw)
# datetime.date(2026, 3, 20)
```

### 取得今天的民國日期

```python
from twcal import today

d = today()
print(d)  # 民國115年3月20日
```

### 格式化字串

```python
d = TWDate(115, 3, 20)

d.to_string()        # '民國115年3月20日'
d.to_short_string()  # '1150320'
str(d)               # '民國115年3月20日'
```

### 從短字串解析

```python
d = TWDate.from_short_string("1150320")
# TWDate(year=115, month=3, day=20)
```

### 民國前日期

```python
import datetime
from twcal import to_minguo

d = to_minguo(datetime.date(1911, 1, 1))
# TWDate(year=-1, month=1, day=1)

print(d)  # 民國前1年1月1日
```

### 比較

```python
from twcal import TWDate

TWDate(115, 1, 1) > TWDate(114, 12, 31)   # True
TWDate(114, 1, 1) < TWDate(115, 1, 1)     # True
```

### 驗證

```python
from twcal import TWDate

TWDate(0, 1, 1)    # ValueError: 民國0年不存在
TWDate(115, 2, 30) # ValueError: day is out of range for month
```

## 授權

本專案採用 [MIT 授權條款](LICENSE)。你可以自由地使用、修改及散布本軟體，包含商業用途。
