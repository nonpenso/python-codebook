# NumPy

NumPy adds support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them efficiently.

```python
import numpy as np
```

## Arrays

A NumPy array is a grid of values, all of the same type. Arrays can be created from Python lists or generated using built-in functions.

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
```

### Array Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| `ndim` | Number of dimensions | `b.ndim` → `2` |
| `shape` | Tuple of dimension sizes | `b.shape` → `(2, 3)` |
| `size` | Total number of elements | `b.size` → `6` |
| `dtype` | Data type of elements | `b.dtype` → `dtype('int64')` |

### Reshaping and Transforming

```python
a = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3 matrix (returns a new array)
b = a.reshape(2, 3)
print(b)
# [[1 2 3]
#  [4 5 6]]

# Resize modifies the array in place
a.resize(3, 2)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]

# Flatten to 1D
c = b.ravel()
print(c)  # [1 2 3 4 5 6]
```

### Changing Data Type

```python
a = np.array([1.5, 2.7, 3.9])
b = a.astype(int)
print(b)  # [1 2 3]
```

## Array Creation

```python
# Array of zeros
a = np.zeros((3, 4))

# Array of ones
b = np.ones((2, 3))

# Array with a range of values
c = np.arange(0, 10, 2)
print(c)  # [0 2 4 6 8]

# Array of zeros with the same shape as another array
d = np.zeros_like(b)
```

### Random Arrays

```python
# Uniform random values in [0, 1)
r1 = np.random.rand(3, 3)

# Standard normal distribution (mean=0, std=1)
r2 = np.random.randn(3, 3)

# Random integers between low (inclusive) and high (exclusive)
r3 = np.random.randint(0, 10, size=(2, 3))
print(r3)
# e.g. [[7 2 5]
#        [1 9 3]]
```

## Statistical Computation

```python
a = np.array([1, 2, 3, 4, 5, np.nan, 7])

# Mean (ignores NaN with nanmean)
print(np.mean(a))       # nan
print(np.nanmean(a))    # 3.6667

# Standard deviation
print(np.std(a))        # nan
print(np.nanstd(a))     # 1.9720

# Median
print(np.median(a))     # nan
print(np.nanmedian(a))  # 3.5

# Percentile (ignores NaN with nanpercentile)
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.percentile(b, 25))  # 3.25
print(np.percentile(b, 75))  # 7.75
```

| Function | Description |
|----------|-------------|
| `np.mean(a)` | Arithmetic mean |
| `np.nanmean(a)` | Mean ignoring NaN values |
| `np.std(a)` | Standard deviation |
| `np.nanstd(a)` | Standard deviation ignoring NaN |
| `np.median(a)` | Median value |
| `np.percentile(a, q)` | q-th percentile |

## Basic Operations

### Sum and Difference

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a + 10)  # [11 12 13]
```

### Product and Quotient

```python
print(a * b)   # [ 4 10 18]
print(a / b)   # [0.25 0.4  0.5 ]
print(a ** 2)  # [1 4 9]
```

### Cloning an Array

```python
a = np.array([1, 2, 3])

# Assignment does NOT create a copy (both point to same data)
b = a
b[0] = 99
print(a)  # [99  2  3] — a is also modified!

# Use .copy() to create an independent clone
a = np.array([1, 2, 3])
c = a.copy()
c[0] = 99
print(a)  # [1 2 3] — a is unchanged
```

:::{warning} Assignment vs Copy
Using `b = a` does **not** create a new array. Both variables reference the same data in memory. Always use `.copy()` when you need an independent copy.
:::
