# Date & Time

Python handles dates and times through the `time` and `datetime` modules.

## Module time

The `time` module provides functions for working with time values represented as seconds since the epoch (January 1, 1970).

### Time Structure

`time.localtime()` returns a named tuple with 9 attributes:

| Index | Attribute | Description | Values |
| --- | --- | --- | --- |
| 0 | tm_year | 4-digit year | e.g. 2025 |
| 1 | tm_mon | Month | 1–12 |
| 2 | tm_mday | Day | 1–31 |
| 3 | tm_hour | Hour | 0–23 |
| 4 | tm_min | Minute | 0–59 |
| 5 | tm_sec | Second | 0–59 |
| 6 | tm_wday | Day of week | 0–6 (Monday=0) |
| 7 | tm_yday | Day of year | 1–366 |
| 8 | tm_isdst | Daylight saving | -1, 0, 1 |

### Format Directives

| Directive | Meaning |
| --- | --- |
| `%a` / `%A` | Abbreviated / full weekday name |
| `%b` / `%B` | Abbreviated / full month name |
| `%d` | Day of month (01–31) |
| `%H` / `%I` | Hour: 24h (00–23) / 12h (01–12) |
| `%j` | Day of year (001–366) |
| `%m` | Month (01–12) |
| `%M` | Minute (00–59) |
| `%S` | Second (00–59) |
| `%y` / `%Y` | Year without / with century |
| `%Z` | Time zone name |

### Main Functions

| Function | Description |
| --- | --- |
| `time.localtime()` | Current local time as a named tuple |
| `time.time()` | Current time as seconds since epoch (float) |
| `time.strftime(format, t)` | Format a time tuple as a string |
| `time.sleep(secs)` | Pause execution for the given number of seconds |

```python
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2025, tm_mon=3, tm_mday=4, ...)
>>> time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
'Tue, 04 Mar 2025 11:56:30'
```

### Measuring Elapsed Time

```python
import time

print(time.strftime("%H:%M:%S"))
start = time.time()

# Simulate a process
time.sleep(3.7)

elapsed = time.time() - start
hours = int(elapsed // 3600)
minutes = int((elapsed % 3600) // 60)
seconds = int(elapsed % 60)

print(f"Time: {time.strftime('%H:%M:%S')}")
print(f"Processing time: {hours:02d}:{minutes:02d}:{seconds:02d}")
```

## Module datetime

The `datetime` module provides classes for manipulating dates and times.

### Main Classes

| Class | Description |
| --- | --- |
| `datetime.date(year, month, day)` | A date (no time component) |
| `datetime.time(hour, minute, second, microsecond)` | A time (no date component) |
| `datetime.datetime(year, month, day, hour, minute, second)` | Combined date and time |
| `datetime.timedelta(days, seconds, ...)` | A duration between two dates/times |

### Main Methods

| Method | Description |
| --- | --- |
| `datetime.date.today()` | Current local date |
| `datetime.datetime.now()` | Current local date and time |
| `obj.replace(year=..., month=...)` | Return a copy with specified fields replaced |
| `obj.isoformat()` | ISO 8601 string (YYYY-MM-DDTHH:MM:SS) |
| `obj.year`, `.month`, `.day`, `.hour`, etc. | Access individual components |
| `obj.weekday()` | Day of week (Monday=0, Sunday=6) |

### Examples

```python
>>> import datetime
>>> today = datetime.date(2025, 8, 6)
>>> one_day = datetime.timedelta(days=1)
>>> today + one_day
datetime.date(2025, 8, 7)

>>> birth = datetime.datetime(1974, 2, 7, 20, 45, 50)
>>> now = datetime.datetime(2025, 3, 16, 10, 38, 2)
>>> diff = now - birth
>>> diff.days
18665
>>> diff.seconds
49932

>>> years = diff.days // 365
>>> remaining_days = diff.days % 365
>>> hours = diff.seconds // 3600
>>> minutes = (diff.seconds % 3600) // 60
>>> print(f"{years} years, {remaining_days} days, {hours}h {minutes}min")
51 years, 40 days, 13h 52min
```
