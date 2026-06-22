# Variables and Operators

## Variables

Variables are reserved memory locations used to store values. The `=` sign assigns values to variables.

```python
counter = 100        # integer
miles = 1000.0       # floating point
name = "John"        # string
```

Python has the following standard data types:

- Numbers
- String
- List
- Tuple
- Dictionary

## Operators

### Arithmetic Operators

| Operator | Description | Example (a=7, b=3) |
| --- | --- | --- |
| `+` | Addition | `a + b` → 10 |
| `-` | Subtraction | `a - b` → 4 |
| `*` | Multiplication | `a * b` → 21 |
| `/` | Division | `a / b` → 2.333... |
| `%` | Modulus (remainder) | `a % b` → 1 |
| `**` | Exponent | `a ** b` → 343 |
| `//` | Floor division | `7.0 // 3` → 2.0 |

### Comparison Operators

| Operator | Description | Example (a=7, b=3) |
| --- | --- | --- |
| `==` | Equal to | `a == b` → False |
| `!=` | Not equal to | `a != b` → True |
| `>` | Greater than | `a > b` → True |
| `<` | Less than | `a < b` → False |
| `>=` | Greater than or equal to | `a >= b` → True |
| `<=` | Less than or equal to | `a <= b` → False |

!!! note
    The `<>` operator from Python 2 has been removed. Use `!=` instead.

### Assignment Operators

| Operator | Description | Example |
| --- | --- | --- |
| `=` | Assign | `c = a + b` |
| `+=` | Add and assign | `c += a` is equivalent to `c = c + a` |
| `-=` | Subtract and assign | `c -= a` is equivalent to `c = c - a` |
| `*=` | Multiply and assign | `c *= a` is equivalent to `c = c * a` |
| `/=` | Divide and assign | `c /= a` is equivalent to `c = c / a` |
| `%=` | Modulus and assign | `c %= a` is equivalent to `c = c % a` |
| `**=` | Exponent and assign | `c **= a` is equivalent to `c = c ** a` |
| `//=` | Floor divide and assign | `c //= a` is equivalent to `c = c // a` |

### Logical Operators

| Operator | Description | Example |
| --- | --- | --- |
| `and` | True if both operands are true | `(a and b)` is True |
| `or` | True if at least one operand is true | `(a or b)` is True |
| `not` | Reverses the logical state | `not (a and b)` is False |
