# CSV

The `csv` module provides functionality for reading and writing CSV (Comma-Separated Values) files.

```python
import csv
```

:::{warning} Python 3 File Opening
In Python 3, open CSV files with `newline=''` to prevent blank rows on Windows. Use text mode (`"r"` / `"w"`) instead of binary mode (`"rb"` / `"wb"` which was required in Python 2).
:::

## Reading as Dictionary

`csv.DictReader` reads each row into a dictionary where keys are the column headers.

```python
import csv

with open("data.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

### Dialect Parameters

You can customise how the CSV is parsed using dialect parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `delimiter` | `,` | Character that separates fields |
| `doublequote` | `True` | Whether quotechar inside a field is doubled |
| `escapechar` | `None` | Character used to escape the delimiter |
| `lineterminator` | `\r\n` | String used to terminate lines |
| `quotechar` | `"` | Character used to quote fields |
| `quoting` | `QUOTE_MINIMAL` | Controls when quotes are generated |
| `skipinitialspace` | `False` | Whether whitespace after delimiter is ignored |

```python
with open("data.csv", "r", newline='') as f:
    reader = csv.DictReader(f, delimiter=";", quotechar="'")
    for row in reader:
        print(row)
```

## Reading as Strings

You can also read CSV files using basic file methods without the `csv` module:

```python
# Read line by line
with open("data.csv", "r") as f:
    line = f.readline()        # Read one line
    print(line.strip())        # Remove trailing newline

# Read all lines at once
with open("data.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        fields = line.strip().split(",")
        print(fields)
```

## Writing as List

`csv.writer` writes rows as lists.

```python
import csv

header = ["name", "age", "city"]
rows = [
    ["Alice", 30, "London"],
    ["Bob", 25, "Paris"],
    ["Charlie", 35, "Berlin"],
]

with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)   # Write a single row
    writer.writerows(rows)    # Write multiple rows
```

## Writing as Dictionary

`csv.DictWriter` writes rows from dictionaries.

```python
import csv

header = ["name", "age", "city"]
rows = [
    {"name": "Alice", "age": 30, "city": "London"},
    {"name": "Bob", "age": 25, "city": "Paris"},
]

with open("output.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)
```

## Sorting by Column

Read the CSV, sort the data, and write it back:

```python
import csv

# Read data
with open("data.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

# Sort by the "age" column (convert to int for numeric sort)
rows.sort(key=lambda row: int(row["age"]))

# Write sorted data
with open("sorted.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```
