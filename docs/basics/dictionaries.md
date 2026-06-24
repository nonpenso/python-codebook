# Dictionaries

A dictionary is a mutable container that stores key-value pairs. Keys must be immutable (strings, numbers, or tuples), while values can be of any type.

```python
my_dict = {"key": "value"}
```

Keys are unique within a dictionary; values may repeat.

## Dictionary Methods

| Method | Description |
| --- | --- |
| `dict.get(key)` | Returns the value for key, or `None` if not found |
| `key in dict` | Returns True if key exists in the dictionary |
| `dict.items()` | Returns a view of (key, value) pairs |
| `dict.keys()` | Returns a view of all keys |
| `dict.values()` | Returns a view of all values |
| `dict.clear()` | Removes all items |
| `dict.setdefault(key, value)` | Returns value if key exists; otherwise inserts key with value |

:::{note}
`dict.has_key(key)` was removed in Python 3. Use `key in dict` instead.
:::

## Examples

```python
>>> d = {"Name": "Zara", "Age": 7, "Class": "First"}
>>> d["Name"]
'Zara'

>>> # Add a new entry
>>> d["School"] = "DPS School"
>>> d
{'Name': 'Zara', 'Age': 7, 'Class': 'First', 'School': 'DPS School'}

>>> # Update an existing entry
>>> d["Age"] = 8

>>> # List keys and values
>>> list(d.keys())
['Name', 'Age', 'Class', 'School']
>>> list(d.values())
['Zara', 8, 'First', 'DPS School']

>>> # Delete an entry
>>> del d["Name"]
```

### Find a Key by Value

```python
>>> d = {'george': 16, 'amber': 19}

>>> # Using a loop
>>> for name, age in d.items():
...     if age == 16:
...         print(name)
george

>>> # Using list comprehension
>>> [k for k, v in d.items() if v == 16]
['george']
```

### Append to a List Inside a Dictionary

```python
# Using setdefault (concise)
d.setdefault(key, []).append(value)

# Equivalent long form
if key in d:
    d[key].append(value)
else:
    d[key] = [value]
```

## Iteration

```python
>>> mydict = {"Hour": 13, "Day": "Monday"}
>>> for key, value in mydict.items():
...     print(key, value)
Hour 13
Day Monday
```

```python
>>> knights = {"gallahad": "the pure", "robin": "the brave"}
>>> for k, v in knights.items():
...     print(k, v)
gallahad the pure
robin the brave
```

:::{warning} Python 2 vs Python 3
Use `dict.items()` instead of `dict.iteritems()` — the latter was removed in Python 3.
:::
