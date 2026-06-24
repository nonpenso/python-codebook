# Numbers

Number data types store numeric values. Python supports the following numerical types:

- **int** — integers (no size limit in Python 3)
- **float** — floating-point real values
- **complex** — complex numbers (e.g., `3+4j`)

:::{note}
Python 2 had a separate `long` type. In Python 3, `int` handles arbitrarily large integers automatically.
:::

## Type Conversion

| Function | Description |
| --- | --- |
| `int(x)` | Convert x to an integer |
| `float(x)` | Convert x to a floating-point number |
| `complex(x)` | Convert x to a complex number with imaginary part zero |

## Math Functions

These functions require `import math`:

| Function | Description |
| --- | --- |
| `abs(x)` | Absolute value of x |
| `math.exp(x)` | The exponential of x (e^x) |
| `math.log(x)` | Natural logarithm of x (x > 0) |
| `math.log10(x)` | Base-10 logarithm of x (x > 0) |
| `math.sqrt(x)` | Square root of x (x > 0) |
| `math.cos(x)` | Cosine of x (in radians) |
| `math.sin(x)` | Sine of x (in radians) |

## Constants

- `math.pi` — the mathematical constant π
- `math.e` — the mathematical constant e

## Examples

```python
>>> (50 - 5 * 6) / 4
5.0
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> 17 / 4       # True division (returns float in Python 3)
4.25
>>> 17 // 4      # Floor division (returns integer quotient)
4
>>> 17 % 4       # Modulus (remainder)
1
```

:::{warning} Python 2 vs Python 3
In Python 2, `17/4` returned `4` (integer division). In Python 3, `/` always returns a float. Use `//` for integer division.
:::
