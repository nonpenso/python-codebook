# Read Layer

Rasterio reads and writes geospatial raster data.

Module documentation is available at:
[https://rasterio.readthedocs.io/en/stable/](https://rasterio.readthedocs.io/en/stable/)

## Open a Raster Layer

```python
import rasterio

with rasterio.open(r'C:\temp\example.tif', 'r') as dataset:
    ## INFO
    name = dataset.name
    metadata = dataset.profile
    bands = dataset.indexes
    extent = dataset.bounds        # left, bottom, right, top
    proj = dataset.crs
    geosp = dataset.transform      # pixel size X, X rotation, top left X, Y rotation, pixel size -Y, top left Y
    rows = dataset.height
    cols = dataset.width
    noData = dataset.nodata

    mask = dataset.read_masks(1)   # 0 = NoData, 255 = Valid data

    ## DATA -> ARRAY
    arr = dataset.read(1)
```

## Operation with Raster Layers

```python
import rasterio
import numpy

in_tiff = r'C:\temp\IN.tif'
out_tiff = r'C:\temp\OUT.tif'

with rasterio.open(in_tiff, 'r') as dataset:
    profile = dataset.meta.copy()  # copy all parameters of source image

    arr_in = dataset.read(1, masked=True)  # read as masked array
    arr_out = numpy.ma.where(arr_in > 60, 100, arr_in)  # compute using masked array method

    with rasterio.open(out_tiff, 'w', **profile) as outset:
        outset.write(arr_out, 1)
```
