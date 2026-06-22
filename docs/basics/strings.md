# Strings

Strings in Python are sequences of characters enclosed in single quotes `' '` or double quotes `" "`.

## String Operators

| Operator | Description |
| --- | --- |
| `+` | Concatenation — joins two strings |
| `*` | Repetition — repeats a string n times |
| `[ : ]` | Slice — extracts a substring by index range |
| `in` | Membership — returns True if a character exists in the string |

## Indexing and Slicing

Indexes start at 0 from the left and -1 from the right:

```
 +---+---+---+---+---+
 | H | e | l | l | o |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1
```

```python
>>> text = "Fortunately"
>>> text[0:4]
'Fort'
>>> text[5:-2]
'nate'
```

## Built-in String Functions

| Function | Description |
| --- | --- |
| `ord('A')` | Get the Unicode code point for a character |
| `chr(65)` | Get the character for a Unicode code point |

## String Methods

| Method | Description |
| --- | --- |
| `str.lower()` | Convert to lowercase |
| `str.upper()` | Convert to uppercase |
| `str.capitalize()` | Capitalize the first letter |
| `str.split("sep")` | Split into a list using separator |
| `str.find("sub", start, end)` | Find substring; returns index or -1 |
| `str.strip()` | Remove leading/trailing whitespace |
| `str.replace("old", "new")` | Replace occurrences of a substring |
| `"sep".join(list)` | Join list items into a string with separator |
| `str.encode("utf-8")` | Encode string to bytes |

```python
>>> var1 = "Hello"
>>> var2 = "world"
>>> print(var1 + " " + var2)
Hello world
>>> "spam eggs".split(" ")
['spam', 'eggs']
```

## String Formatting

Python offers three formatting approaches: `%` operator (legacy), `.format()`, and f-strings (recommended).

### Formatting Types

| Type | Description |
| --- | --- |
| `s` | String |
| `d` | Integer |
| `f` | Floating-point decimal |
| `e` | Scientific notation |
| `c` | Single character (from integer code point) |

### Basic Examples

```python
# % operator (legacy)               # .format()                          # f-string (recommended)
>>> "Name: %s, age: %d" % ('Zara', 45)
>>> "Name: {}, age: {}".format('Zara', 45)
>>> name, age = 'Zara', 45
>>> f"Name: {name}, age: {age}"
'Name: Zara, age: 45'
```

### Width and Fill

```python
>>> f"{'Foo':>5}"       # Right-align in 5 characters
'  Foo'
>>> f"{'Foo':<5}"       # Left-align in 5 characters
'Foo  '
>>> f"{5:03d}"          # Zero-pad to 3 digits
'005'
```

### Precision

```python
>>> f"{0.658712358:.3f}"           # 3 decimal places
'0.659'
>>> f"{'abracadabra':.6}"         # Truncate string to 6 characters
'abraca'
>>> f"{0.658712358:6.2f}"         # Width 6, 2 decimal places
'  0.66'
```

### Dictionary Formatting

```python
>>> person = {"name": "Jane", "age": 25}
>>> f"Hello, {person['name']}! You're {person['age']} years old."
"Hello, Jane! You're 25 years old."
```

### F-strings

F-strings (Python 3.6+) are the most concise way to embed expressions in strings:

```python
>>> name = "Jane"
>>> age = 25
>>> f"Hello, {name}! You're {age} years old."
"Hello, Jane! You're 25 years old."

>>> f"Hello, {name.upper()}! You're {age} years old."
"Hello, JANE! You're 25 years old."

>>> balance = 5425.9292
>>> f"Balance: ${balance:.2f}"
'Balance: $5425.93'
```

## Wildcards with fnmatch

The `fnmatch` module provides Unix shell-style wildcard matching:

| Pattern | Meaning |
| --- | --- |
| `*` | Matches everything |
| `?` | Matches any single character |
| `[seq]` | Matches any character in seq |
| `[!seq]` | Matches any character NOT in seq |

```python
>>> import fnmatch
>>> fnmatch.fnmatch('Lorem ipsum', 'Lorem*')
True
>>> fnmatch.fnmatch('abracadabra12', '[a-b]??[a-b]*[1-2][!3-4]')
True
```
