# String Formatting (% Operator)

!!! note "Prefer f-strings"
    The `%` formatting operator is a legacy approach. In modern Python (3.6+), **f-strings** are the preferred method for string formatting. See [Strings](../basics/strings.md) for details on f-strings.

The `%` operator allows you to embed values inside a string using conversion specifications.

## Syntax

```
"format string" % (values)
```

```python
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
# Name: Alice, Age: 30
```

## Conversion Specification Pattern

```
%[flags][width][.precision]code
```

Each `%` placeholder in the string follows this pattern.

## Conversion Codes

| Code | Description | Example |
|------|-------------|---------|
| `%s` | String (or any object via `str()`) | `"%s" % "hello"` → `"hello"` |
| `%d` or `%i` | Integer (decimal) | `"%d" % 42` → `"42"` |
| `%f` | Floating-point (default 6 decimals) | `"%f" % 3.14` → `"3.140000"` |
| `%e` | Floating-point in scientific notation | `"%e" % 0.001` → `"1.000000e-03"` |
| `%c` | Single character (int or str) | `"%c" % 65` → `"A"` |

## Flags

| Flag | Description | Example |
|------|-------------|---------|
| `-` | Left-align within the field width | `"%-10s!"` → `"hello     !"` |
| `+` | Show sign for positive numbers | `"%+d" % 42` → `"+42"` |
| ` ` (space) | Insert space before positive numbers | `"% d" % 42` → `" 42"` |
| `#` | Alternate form (`0x` for hex, `0o` for octal) | `"%#x" % 255` → `"0xff"` |
| `0` | Zero-pad numbers | `"%05d" % 42` → `"00042"` |

## Width

Minimum number of characters in the output. Pads with spaces (or zeros if `0` flag is used).

```python
print("%10s" % "hi")    #         hi  (right-aligned, 10 chars wide)
print("%-10s!" % "hi")  # hi        !  (left-aligned)
print("%10d" % 42)      #         42
```

## Precision

For floats, specifies the number of decimal places. For strings, specifies the maximum length.

```python
print("%.2f" % 3.14159)   # 3.14
print("%.4f" % 3.14159)   # 3.1416
print("%.3s" % "hello")   # hel
```

## Combined Examples

```python
# Right-aligned float with 2 decimal places, 8 chars wide
print("%8.2f" % 3.14159)    #     3.14

# Zero-padded integer, 5 chars wide
print("%05d" % 42)          # 00042

# Multiple values
x, y = 10.5, 20.3
print("Point: (%.1f, %.1f)" % (x, y))  # Point: (10.5, 20.3)

# Dictionary-based formatting
data = {"name": "Alice", "score": 95.5}
print("%(name)s scored %(score).1f%%" % data)  # Alice scored 95.5%
```
