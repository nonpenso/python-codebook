# Module Installation

## 1 — Windows Environment

Add the Python paths to the Windows environment variable `Path`:

```
C:\Python27\ArcGIS10.3
C:\Python27\ArcGIS10.3\Scripts
```

## 2 — Install pip

1. Download `get-pip.py` from [https://pip.pypa.io/en/latest/installing](https://pip.pypa.io/en/latest/installing)
2. On the command prompt, run:

```
C:\Python27\ArcGIS10.X\python.exe C:\Downloads\get-pip.py

setx PATH "%PATH%;C:\Python27\ArcGIS10.X\Scripts"
```

## 3 — Install Modules

### Activate Python (ArcGIS Pro only)

```
"c:\Program Files\ArcGIS\Pro\bin\Python\Scripts\proenv.bat"
```

### Set proxy (if needed)

```
SET HTTPS_PROXY=http://login:password@proxy.example.com:8012
SET HTTP_PROXY=http://login:password@proxy.example.com:8012
```

### Install the package

**A. Using pip online**

```
pip install <package>
```

**B. Using a .whl file**

Repository: [https://github.com/cgohlke/geospatial-wheels/releases](https://github.com/cgohlke/geospatial-wheels/releases)

```
pip install C:\Downloads\newpackage.whl
```

**C. Using a zip file (egg)**

1. Download the `.zip` and unzip
2. Install on the command prompt:

```
cd C:\Temp
python setup.py install
```

!!! note
    For ArcGIS Pro, always use the `proenv.bat` activation script before installing packages. This ensures modules are installed in the correct Python environment managed by ArcGIS Pro's Conda environment.
