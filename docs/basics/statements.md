# Statements

Statements are the building blocks of Python programs: control flow, function definitions, imports, and exception handling.

## print

The `print()` function outputs values to the console.

```python
>>> s = "Hello world"
>>> print(s)
Hello world
```

:::{note}
In Python 3, `print` is a function and requires parentheses: `print("text")`. The Python 2 syntax `print "text"` no longer works.
:::

## for

The `for` statement iterates over the elements of a sequence.

```python
x = [1, 2, 3, 4, 5, 6]
for numb in x:
    print(numb + 1)
```

## if / elif / else

Conditional execution based on boolean expressions.

```python
x = [1, 2, 3, 4, 5, 6]
for numb in x:
    if numb < 3:
        print("lower")
    elif numb == 3:
        print("equal")
    else:
        print("higher")
```

:::{warning}
The `else` clause does **not** take a condition. If you need another condition, use `elif`.
:::

## while

Repeated execution as long as a condition is true.

```python
count = 0
while count < 9:
    print(f"The count is: {count}")
    count += 1
```

## def / return

Define a reusable function with `def`. Use `return` to send a value back to the caller.

```python
def divide(x, y):
    if y != 0:
        return x / y
    return 0
```

:::{note}
Use `!=` instead of `<>` for "not equal" — the `<>` operator was removed in Python 3. Also note that `def` and `if` must be lowercase.
:::

## try / except / else

Handle exceptions gracefully with `try`/`except`.

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"Result is {result}")
```

## del

Delete a variable, list item, or slice.

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[:]
>>> a
[]
>>> del a
>>> a
NameError: name 'a' is not defined
```

## import

Import modules to extend Python's functionality.

```python
import os
import time
from pathlib import Path
import numpy as np
```

## eval

`eval()` evaluates a string as a Python expression and returns the result.

```python
>>> x = eval("5")
>>> x
5
>>> eval("2 + 3")
5
```

:::{warning}
Avoid using `eval()` with untrusted input — it can execute arbitrary code.
:::

## exec

`exec()` executes a string containing Python statements.

```python
>>> exec('x = 5')
>>> x
5
```

:::{warning}
Like `eval()`, avoid `exec()` with untrusted input. In most cases there are better alternatives (dictionaries, lists, or dedicated data structures).
:::
