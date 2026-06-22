# Lists

Lists are the most versatile compound data type in Python. A list contains items separated by commas and enclosed within square brackets `[ ]`.

Values are accessed using the slice operator `[ ]` and `[ : ]` with indexes starting at 0.

## Built-in Functions

| Function | Description |
| --- | --- |
| `len(list)` | Total number of items in the list |
| `range(start, stop, step)` | Creates a sequence of numbers (returns an iterator in Python 3) |
| `sorted(list)` | Returns a new sorted list |
| `max(list)` | Returns the item with the maximum value |
| `min(list)` | Returns the item with the minimum value |
| `enumerate(list)` | Returns an iterator of (index, value) tuples |
| `set(list)` | Returns unique values from the list |

## List Methods

| Method | Description |
| --- | --- |
| `list.append(obj)` | Add an item to the end |
| `list.pop(index)` | Remove and return the item at position |
| `list.insert(index, obj)` | Insert object at the given position |
| `list.count(obj)` | Count occurrences of the object |
| `list.index(obj)` | Return the index of the first occurrence |

## Examples

```python
>>> a = ['spam', 'eggs', 100, 1234]
>>> a[3]
1234
>>> a[1:-1]
['eggs', 100]

>>> # Replace items
>>> a[0:2] = [1, 12]
>>> a
[1, 12, 100, 1234]

>>> # Remove items
>>> a[0:2] = []
>>> a
[100, 1234]

>>> # Insert items
>>> a[1:1] = ['bletch', 'xyzzy']
>>> a
[100, 'bletch', 'xyzzy', 1234]

>>> # Remove a specific item
>>> a.pop(a.index('xyzzy'))
'xyzzy'
>>> a
[100, 'bletch', 1234]
```

```python
>>> b = [66.25, 333, -1, 333, 1, 1234.5]
>>> b.append(333)
>>> b
[66.25, 333, -1, 333, 1, 1234.5, 333]
>>> b.sort()
>>> b
[-1, 1, 66.25, 333, 333, 333, 1234.5]
>>> b.count(333)
3
```

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
```

!!! note
    In Python 3, `range()` returns an iterator, not a list. Wrap it with `list()` if you need an actual list.

## Iteration

```python
>>> mylist = [33.2, 4674, "House"]
>>> for x in mylist:
...     print(x)
33.2
4674
House
```

```python
>>> # Iterating two lists in parallel
>>> questions = ["name", "quest", "favorite color"]
>>> answers = ["lancelot", "the holy grail", "blue"]
>>> for q, a in zip(questions, answers):
...     print(q, a)
name lancelot
quest the holy grail
favorite color blue
```

```python
>>> # Enumeration (index + value)
>>> mylist = ["tic", "tac", "toe"]
>>> for i, v in enumerate(mylist):
...     print(i, v)
0 tic
1 tac
2 toe
```

## Filtering with fnmatch

The `fnmatch.filter()` function filters a list using shell-style wildcards:

| Pattern | Meaning |
| --- | --- |
| `*` | Matches everything |
| `?` | Matches any single character |
| `[seq]` | Matches any character in seq (`-` for range, `!` to exclude) |

```python
>>> import fnmatch
>>> lst = ['hor1', 'hor2', 'hor3', 'hor4', 'dff1', 'dff2', 'afr1']
>>> fnmatch.filter(lst, "a*")
['afr1']
>>> fnmatch.filter(lst, "dff?")
['dff1', 'dff2']
>>> fnmatch.filter(lst, "h*[1-3]")
['hor1', 'hor2', 'hor3']
>>> fnmatch.filter(lst, "[hd]*")
['hor1', 'hor2', 'hor3', 'hor4', 'dff1', 'dff2']
>>> fnmatch.filter(lst, "*[!1]")
['hor2', 'hor3', 'hor4', 'dff2']
```
