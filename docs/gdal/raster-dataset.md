# Raster Dataset

## Opening a Raster

Before opening a GDAL raster dataset, it is necessary to register drivers, then create a data object.

```python
from osgeo import gdal

# Register drivers
gdal.AllRegister()

# TIF file
tif = r"C:\Temp\image.tif"

# Data object
dataset = gdal.Open(tif)
```

## Raster Properties

Dataset object properties: columns, rows, and band number.

```python
# Get image size
cols = dataset.RasterXSize
rows = dataset.RasterYSize
bands = dataset.RasterCount

# Get projection
proj = dataset.GetProjection()
```

`GetGeoTransform` is a method on a dataset object to get projection info as a tuple with 6 numbers.

```python
geotr = dataset.GetGeoTransform()  # returns (368000.0, 1000.0, 0.0, 8828000.0, 0.0, -1000.0)
```

| Element | Description |
|---------|-------------|
| `geotr[0]` | Top left X |
| `geotr[1]` | W-E pixel resolution |
| `geotr[2]` | Rotation, 0 if image is "north up" |
| `geotr[3]` | Top left Y |
| `geotr[4]` | Rotation, 0 if image is "north up" |
| `geotr[5]` | N-S pixel resolution |

## Value Properties

Working with pixel values is limited to one TIF band.

```python
band = dataset.GetRasterBand(1)

# Get NoData value
NoData = band.GetNoDataValue()

# Get min and max
vmin = band.GetMinimum()
vmax = band.GetMaximum()

# Get data type
vtype = band.DataType

# Get colour table
coltab = band.GetColorTable()

# Get statistics: min, max, mean, stddev
stats = band.GetStatistics(1, 1)
```

Raster data types:

| Type | Description |
|------|-------------|
| `GDT_Byte` | Eight bit unsigned integer |
| `GDT_UInt16` | Sixteen bit unsigned integer |
| `GDT_Int16` | Sixteen bit signed integer |
| `GDT_UInt32` | Thirty two bit unsigned integer |
| `GDT_Int32` | Thirty two bit signed integer |
| `GDT_Float32` | Thirty two bit floating point |
| `GDT_Float64` | Sixty four bit floating point |

## Raster to Array

```python
# Convert to a 2D array
data = band.ReadAsArray()
```
