# NetCDF

NetCDF (Network Common Data Form) is a file format designed for storing array-oriented scientific data, particularly climate and weather datasets.

## Reading with netCDF4

The `netCDF4` library is the most common way to work with NetCDF files in Python.

```python
from netCDF4 import Dataset

# Open a NetCDF file
ds = Dataset("data.nc", "r")
```

### Inspecting the File

```python
# View dimensions
print(ds.dimensions)
for dim_name, dim in ds.dimensions.items():
    print(f"{dim_name}: size = {len(dim)}")

# View variables
print(ds.variables)
for var_name, var in ds.variables.items():
    print(f"{var_name}: shape={var.shape}, dtype={var.dtype}")
```

### Accessing Variables

```python
# Get a variable
temp = ds.variables["temperature"]

# Variable properties
print(temp.shape)       # Shape of the array
print(temp.units)       # Units attribute (e.g., "K" or "degrees_C")
print(temp.dtype)       # Data type

# Read data into a NumPy array
temp_data = temp[:]

# Slicing (e.g., first time step, all lat/lon)
first_step = temp[0, :, :]
```

### Time Variables

```python
from netCDF4 import Dataset, num2date

ds = Dataset("data.nc", "r")
time_var = ds.variables["time"]

# Get calendar and units
print(time_var.units)      # e.g., "days since 1900-01-01"
print(time_var.calendar)   # e.g., "standard"

# Convert numeric time to datetime objects
dates = num2date(time_var[:], units=time_var.units, calendar=time_var.calendar)
for d in dates[:5]:
    print(d)
```

### Complete Example

```python
from netCDF4 import Dataset
import numpy as np

ds = Dataset("climate.nc", "r")

# List all variable names
print(list(ds.variables.keys()))

# Read temperature and compute statistics
temp = ds.variables["temperature"][:]
print(f"Mean: {np.nanmean(temp):.2f}")
print(f"Max:  {np.nanmax(temp):.2f}")
print(f"Min:  {np.nanmin(temp):.2f}")

ds.close()
```

:::{note} Always Close the File
Call `ds.close()` when done, or use a context manager if the library version supports it.
:::

## Reading with SciPy

SciPy provides a simpler (but more limited) interface for reading NetCDF files.

```python
from scipy.io import netcdf_file

# Open file (mmap=False loads into memory)
f = netcdf_file("data.nc", "r", mmap=False)

# List variables
print(f.variables.keys())

# Access a variable
temp = f.variables["temperature"]
data = temp.data  # NumPy array

# Dimensions
print(temp.dimensions)  # e.g., ('time', 'lat', 'lon')
print(temp.shape)

f.close()
```

:::{note} SciPy Limitations
`scipy.io.netcdf_file` only supports NetCDF3 format. For NetCDF4/HDF5 files, use the `netCDF4` library instead.
:::
