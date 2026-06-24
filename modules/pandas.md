# Pandas

Pandas is a powerful library for data manipulation and analysis, providing data structures like DataFrame and Series for working with structured data.

```python
import pandas as pd
```

## Import and Export Data

### Read CSV

```python
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
df = pd.read_csv("data.csv", usecols=["name", "age"])
```

### Read Excel

```python
df = pd.read_excel("data.xlsx")
df = pd.read_excel("data.xlsx", sheet_name="Sheet2")
```

### From Dictionary

```python
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "city": ["London", "Paris", "Berlin"],
}
df = pd.DataFrame(data)
```

### Read DBF from Shapefile

```python
import geopandas as gpd

gdf = gpd.read_file("shapefile.shp")
df = pd.DataFrame(gdf.drop(columns="geometry"))
```

### Read from MS Access

```python
import pyodbc

conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\path\to\database.accdb;"
)
conn = pyodbc.connect(conn_str)
df = pd.read_sql("SELECT * FROM table_name", conn)
conn.close()
```

### Export

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

## Common Functions

### DataFrame Information

```python
df.shape       # (rows, columns) tuple
df.columns     # Column names
df.dtypes      # Data types of each column
df.head()      # First 5 rows
df.head(10)    # First 10 rows
df.describe()  # Summary statistics
df.sample(5)   # 5 random rows
```

### Aggregation

```python
df["age"].mean()    # Mean of a column
df["age"].sum()     # Sum
df["age"].median()  # Median
df["age"].max()     # Maximum value
df["age"].min()     # Minimum value
df["city"].unique() # Unique values in a column
```

### Indexing and Values

```python
# Get values as a NumPy array
df["age"].values

# Get values as a Python list
df["age"].tolist()

# Unique values
df["city"].unique()

# Number of unique values
df["city"].nunique()
```

### Rename Columns

```python
df = df.rename(columns={"name": "full_name", "age": "years"})
```

## Delete Rows

```python
# Drop rows by index
df = df.drop([0, 1, 2])

# Drop rows where a condition is met
df = df[df["age"] >= 18]

# Drop rows with missing values
df = df.dropna()
df = df.dropna(subset=["age"])

# Reset index after dropping
df = df.reset_index(drop=True)
```

## Operations

### Assign New Columns

```python
# Create a new column from an expression
df = df.assign(birth_year=2024 - df["age"])

# Multiple columns at once
df = df.assign(
    birth_year=2024 - df["age"],
    name_upper=df["name"].str.upper(),
)
```

## Indexing

### loc — Label-based Indexing

```python
# Select row by label
df.loc[0]

# Select rows and specific columns
df.loc[0:5, ["name", "age"]]

# Select with a condition
df.loc[df["age"] > 30, "name"]
```

### iloc — Position-based Indexing

```python
# Select row by position
df.iloc[0]

# Select rows 0-4, columns 0-2
df.iloc[0:5, 0:3]

# Select specific rows and columns
df.iloc[[0, 2, 4], [1, 3]]
```

## Selecting and Filtering

### Select Columns

```python
# Single column (returns Series)
df["name"]

# Multiple columns (returns DataFrame)
df[["name", "age"]]
```

### Filter Rows

```python
# Single condition
df[df["age"] > 30]

# Multiple conditions (use & for AND, | for OR)
df[(df["age"] > 25) & (df["city"] == "London")]
df[(df["age"] < 20) | (df["age"] > 60)]
```

:::{note} Parentheses Required
When combining conditions with `&` or `|`, each condition must be wrapped in parentheses.
:::

### String Filtering

```python
# Contains a substring
df[df["name"].str.contains("ali", case=False)]

# Starts with / ends with
df[df["name"].str.startswith("A")]
df[df["name"].str.endswith("e")]
```

### isin

```python
cities = ["London", "Paris"]
df[df["city"].isin(cities)]
```

### where

```python
# Keep values where condition is True, replace others with NaN
df["age"].where(df["age"] > 30)
```

### query

```python
# SQL-like filtering syntax
df.query("age > 30 and city == 'London'")
```

## Merge and Join

### Concatenate

```python
# Stack DataFrames vertically
df_all = pd.concat([df1, df2], ignore_index=True)

# Stack horizontally
df_wide = pd.concat([df1, df2], axis=1)
```

### Merge

```python
# Inner join (default)
merged = pd.merge(df1, df2, on="id")

# Left join
merged = pd.merge(df1, df2, on="id", how="left")

# Join on different column names
merged = pd.merge(df1, df2, left_on="user_id", right_on="id")
```

| Parameter | Description |
|-----------|-------------|
| `on` | Column name to join on (must exist in both) |
| `left_on` | Column name in left DataFrame |
| `right_on` | Column name in right DataFrame |
| `how` | Type of join: `inner`, `left`, `right`, `outer` |

## Pivot Table

### Using groupby + value_counts + unstack

```python
# Count occurrences of each category per group
pivot = df.groupby("city")["category"].value_counts().unstack(fill_value=0)
```

### Using pivot_table

```python
pivot = pd.pivot_table(
    df,
    values="sales",
    index="city",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)
```

## Group By

### Basic Aggregation

```python
# Sum by group
df.groupby("city")["sales"].sum()

# Multiple aggregations
df.groupby("city")["sales"].agg(["sum", "mean", "count"])
```

### Apply a Custom Function

```python
# Collect values into a list per group
df.groupby("city")["name"].apply(list)
```

### Binning with pd.cut

```python
# Create age bins
bins = [0, 18, 35, 50, 100]
labels = ["youth", "young_adult", "adult", "senior"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

# Count per bin
df.groupby("age_group", observed=True).size()
```
