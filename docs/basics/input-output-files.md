# Input/Output Files

## Files and Directories

How to write a path string in Python:

```python
path = "C:\\myfolder\\temp"     # escaped backslashes
path = "C:/myfolder/temp"       # forward slashes (cross-platform)
path = r"C:\myfolder\temp"      # raw string (recommended on Windows)
```

A string prefixed with `r` or `R` is a *raw string* — backslashes are treated as literal characters.

## Module os

The `os` module provides functions for file and directory operations.

| Function | Description |
| --- | --- |
| `os.chdir(path)` | Change the current working directory |
| `os.listdir(path)` | List entries in a directory |
| `os.makedirs(path)` | Create a directory (including intermediate ones) |
| `os.remove(file)` | Delete a file |
| `os.rmdir(path)` | Delete an empty directory |
| `os.rename(old, new)` | Rename a file or directory |
| `os.path.exists(path)` | Return True if path exists |
| `os.walk(path, topdown=True)` | Walk a directory tree, yielding `(dirpath, dirnames, filenames)` |

```python
# Delete everything inside a directory (use with caution!)
import os

for root, dirs, files in os.walk(r"E:\myfolder", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
```

```python
# Create a directory if it doesn't exist
import os

mydir = r"D:\temp"
if not os.path.exists(mydir):
    os.makedirs(mydir)
```

```python
# Delete an empty directory
import os

mydir = r"D:\temp"
if os.listdir(mydir) == []:
    os.rmdir(mydir)
```

## Module shutil

The `shutil` module provides high-level file and directory operations.

| Function | Description |
| --- | --- |
| `shutil.move(src, dst)` | Move a file or directory |
| `shutil.copy(src, dst)` | Copy a file (preserving permissions) |
| `shutil.copytree(src, dst)` | Copy an entire directory tree |
| `shutil.rmtree(path)` | Delete a directory tree recursively |

```python
# Move all files from one directory to another
import shutil
import os
import glob

mydir = r"D:\workdir"
tempdir = r"D:\workdir\temp"
if not os.path.exists(tempdir):
    os.makedirs(tempdir)

filelist = glob.glob(os.path.join(mydir, "*"))
for file in filelist:
    shutil.move(file, tempdir)
```

## Module zipfile

The `zipfile` module provides tools to create, read, write, and extract ZIP archives.

| Method | Description |
| --- | --- |
| `ZipFile(path, mode)` | Open or create a ZIP archive (`"w"` write, `"r"` read, `"a"` append) |
| `zf.write(file, arcname, compress_type)` | Add a file to the archive |
| `zf.extractall(path)` | Extract all files to a directory |

```python
import glob
import zipfile

mydir = r"D:\workdir"

with zipfile.ZipFile(os.path.join(mydir, "zippedfiles.zip"), "w") as zipped:
    for f in glob.glob(os.path.join(mydir, "*.pdf")):
        zipped.write(f, os.path.basename(f), compress_type=zipfile.ZIP_DEFLATED)
```

!!! note
    Always use `with` statements to ensure files are properly closed.

## Module glob

The `glob` module finds pathnames matching a shell-style pattern.

| Pattern | Meaning |
| --- | --- |
| `?` | Matches any single character |
| `*` | Matches zero or more characters |
| `[seq]` | Matches any character in seq (`-` for range) |

```python
>>> import glob
>>> glob.glob(r'C:\temp\card?.gif')
['C:\\temp\\card1.gif', 'C:\\temp\\card2.gif']
>>> glob.glob(r'C:\temp\*.gif')
['C:\\temp\\1g.gif', 'C:\\temp\\card1.gif', 'C:\\temp\\card2.gif']
>>> glob.glob(r'C:\temp\[0-9]*')
['C:\\temp\\1g.gif', 'C:\\temp\\2a.txt']
```

## Running a Python File

```python
# From another script (Python 3)
exec(open("C:/Temp/Test.py").read())

# From the command line
$ python C:/Temp/Test.py
```

!!! warning
    `execfile()` was removed in Python 3. Use `exec(open(...).read())` or better yet, import the script as a module.

## Reading Keyboard Input

```python
>>> name = input("Enter your name: ")
Enter your name: Alice
>>> name
'Alice'
```

!!! note
    In Python 3, `input()` always returns a string. Use `int(input(...))` or `float(input(...))` to read numbers. The `raw_input()` function from Python 2 was removed — `input()` in Python 3 behaves like Python 2's `raw_input()`.
