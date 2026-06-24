# Module Installation

How to install Python packages in different scenarios.

## 1. Set Proxy

If you are behind a corporate proxy, configure it before installing packages:

**Windows (CMD):**

```bash
SET HTTPS_PROXY=http://username:password@proxy.example.com:8080
SET HTTP_PROXY=http://username:password@proxy.example.com:8080
```

**Windows (PowerShell):**

```powershell
$env:HTTPS_PROXY = "http://username:password@proxy.example.com:8080"
$env:HTTP_PROXY = "http://username:password@proxy.example.com:8080"
```

**Linux / macOS:**

```bash
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
export HTTP_PROXY=http://username:password@proxy.example.com:8080
```

**Permanent pip configuration** (create or edit `pip.ini` on Windows or `pip.conf` on Linux):

```ini
[global]
proxy = http://username:password@proxy.example.com:8080
```

Location:
- Windows: `%APPDATA%\pip\pip.ini`
- Linux: `~/.config/pip/pip.conf`

## 2. Activate Python

Before installing, make sure the correct Python environment is active.

**System Python:**

```bash
python --version
```

**Virtual environment (venv):**

```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/macOS)
source .venv/bin/activate
```

**Conda environment:**

```bash
conda activate myenv
```

## 3. Installation Methods

### 3a. Via pip (online)

The standard method for installing packages from [PyPI](https://pypi.org/):

```bash
pip install numpy
pip install numpy==1.26.4        # specific version
pip install numpy>=1.25,<2.0     # version range
pip install -r requirements.txt  # from a file
```

Useful options:

```bash
pip install --upgrade numpy      # upgrade to latest
pip install --user numpy         # install for current user only
pip list                         # list installed packages
pip show numpy                   # show package info
```

### 3b. Using pip + git

Install directly from a Git repository:

```bash
# From the main branch
pip install git+https://github.com/user/repo.git

# From a specific branch
pip install git+https://github.com/user/repo.git@branch-name

# From a specific tag/release
pip install git+https://github.com/user/repo.git@v1.2.3
```

### 3c. Cloning a git repository

For packages not on PyPI, or when you need to modify the source:

```bash
git clone https://github.com/user/repo.git
cd repo
pip install .
```

For development mode (changes to the source are immediately available):

```bash
pip install -e .
```

### 3d. Using wheel files (.whl)

Pre-built binary packages, useful when pip cannot compile from source. A good repository for Windows wheels:

- [https://github.com/cgohlke/geospatial-wheels/releases](https://github.com/cgohlke/geospatial-wheels/releases)

```bash
pip install C:\Downloads\GDAL-3.8.4-cp312-cp312-win_amd64.whl
```

:::{note}
Wheel filenames encode compatibility info: `{package}-{version}-{python}-{abi}-{platform}.whl`. Make sure the Python version (`cp312` = Python 3.12) and platform (`win_amd64`) match your environment.
:::

### 3e. Using zip/tar files

For packages distributed as source archives:

```bash
# Download and extract the archive, then:
cd package-folder
pip install .
```

Or directly without extracting:

```bash
pip install package-1.0.tar.gz
pip install package-1.0.zip
```

Legacy method (still works but pip is preferred):

```bash
cd package-folder
python setup.py install
```

## Verify Installation

```python
>>> import numpy
>>> numpy.__version__
'1.26.4'
>>> numpy.__file__
'C:\\Python312\\Lib\\site-packages\\numpy\\__init__.py'
```
