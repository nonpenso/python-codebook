# Multiprocessing

The `multiprocessing` module enables parallel execution by spawning multiple processes, each with its own Python interpreter and memory space. This bypasses the Global Interpreter Lock (GIL) and allows true parallelism on multi-core systems.

```python
from multiprocessing import Pool, cpu_count
```

## Basic Concept

Unlike threading, multiprocessing creates separate processes that run independently. This is ideal for CPU-bound tasks where you need to utilise multiple cores.

```python
from multiprocessing import cpu_count

print(f"Available CPU cores: {cpu_count()}")
```

## Using Pool

`Pool` manages a group of worker processes and distributes tasks across them.

```python
from multiprocessing import Pool, cpu_count


def square(n):
    """Return the square of a number."""
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a pool with all available cores
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(square, numbers)

    print(results)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

!!! warning "The `if __name__ == '__main__'` Guard"
    On Windows, multiprocessing requires the `if __name__ == "__main__"` guard to prevent infinite process spawning.

## Pool Methods

| Method | Description |
|--------|-------------|
| `pool.map(func, iterable)` | Apply function to each item, return results in order |
| `pool.starmap(func, iterable)` | Like `map`, but unpacks arguments from tuples |
| `pool.apply(func, args)` | Call function with args in a single worker |
| `pool.apply_async(func, args)` | Non-blocking version of `apply` |
| `pool.map_async(func, iterable)` | Non-blocking version of `map` |

## Example with Multiple Arguments

Use `starmap` when your function takes multiple arguments:

```python
from multiprocessing import Pool


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


if __name__ == "__main__":
    pairs = [(2, 3), (4, 5), (6, 7), (8, 9)]

    with Pool() as pool:
        results = pool.starmap(multiply, pairs)

    print(results)  # [6, 20, 42, 72]
```

## Example with Real Workload

```python
import time
from multiprocessing import Pool, cpu_count


def process_item(item):
    """Simulate a CPU-intensive task."""
    total = 0
    for i in range(10_000_000):
        total += i * item
    return total


if __name__ == "__main__":
    items = list(range(8))

    # Sequential
    start = time.time()
    sequential_results = [process_item(i) for i in items]
    print(f"Sequential: {time.time() - start:.2f}s")

    # Parallel
    start = time.time()
    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(process_item, items)
    print(f"Parallel:   {time.time() - start:.2f}s")
```
