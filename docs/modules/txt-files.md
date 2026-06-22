# Text Files

Python provides built-in functions for reading and writing text files using file objects.

## Creating a File Object

Use the `open()` function to create a file object. Always use a `with` statement to ensure the file is properly closed.

```python
with open("example.txt", "r") as f:
    content = f.read()
```

### Open Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or **overwrites** existing content. |
| `"a"` | Append. Creates file or adds to end of existing content. |
| `"r+"` | Read and write. File must exist. |
| `"x"` | Exclusive creation. Fails if file already exists. |

!!! warning "Write Mode Overwrites"
    Opening a file with `"w"` will erase all existing content. Use `"a"` to append instead.

## File Methods

| Method | Description |
|--------|-------------|
| `f.read()` | Read entire file as a single string |
| `f.read(n)` | Read `n` characters |
| `f.readline()` | Read one line (including `\n`) |
| `f.readlines()` | Read all lines into a list |
| `f.write(s)` | Write string `s` to file |
| `f.writelines(lst)` | Write a list of strings to file |
| `f.close()` | Close the file |
| `f.name` | Name of the file |

### Reading Examples

```python
# Read entire file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("data.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# Read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

### Writing Examples

```python
# Write to a file
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Append to a file
with open("output.txt", "a") as f:
    f.write("Appended line\n")
```

## Escape Codes

| Code | Description |
|------|-------------|
| `\n` | Newline |
| `\t` | Tab |
| `\b` | Backspace |
| `\r` | Carriage return |
| `\\` | Literal backslash |

```python
with open("formatted.txt", "w") as f:
    f.write("Name\tAge\tCity\n")
    f.write("Alice\t30\tLondon\n")
    f.write("Bob\t25\tParis\n")
```

## Practical Examples

### Find and Replace in a File

```python
with open("data.txt", "r") as f:
    content = f.read()

content = content.replace("old_text", "new_text")

with open("data.txt", "w") as f:
    f.write(content)
```

### Create a List of Files in a Directory

```python
import os

files = os.listdir("my_folder")
txt_files = [f for f in files if f.endswith(".txt")]

with open("file_list.txt", "w") as out:
    for filename in txt_files:
        out.write(filename + "\n")
```

## Iterating Over Text Files

### Using a for Loop

The simplest way to iterate line by line:

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Using the fileinput Module

The `fileinput` module allows you to iterate over lines from multiple files:

```python
import fileinput

for line in fileinput.input(files=["file1.txt", "file2.txt"]):
    print(f"{fileinput.filename()} line {fileinput.lineno()}: {line.strip()}")
```

| Function | Description |
|----------|-------------|
| `fileinput.filename()` | Name of the current file being read |
| `fileinput.lineno()` | Cumulative line number across all files |
| `fileinput.filelineno()` | Line number within the current file |
| `fileinput.isfirstline()` | `True` if this is the first line of the current file |
| `fileinput.close()` | Close the sequence |

```python
import fileinput

for line in fileinput.input(files=["data1.txt", "data2.txt"]):
    if fileinput.isfirstline():
        print(f"\n--- Reading: {fileinput.filename()} ---")
    print(line.strip())
```
