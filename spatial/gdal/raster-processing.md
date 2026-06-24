# Raster Processing

## Write a Raster

```python
import numpy
from osgeo import gdal
from osgeo import osr

## Numpy array with data
data = numpy.array()

## Variables
rasname = '/home/user/Documents/raster.tif'
cols = 100
rows = 50
Xmin = -10.0
Ymax = 80.0
pixel = 1.0
EPSG = 4326
rastype = gdal.GDT_Float32
nodata = -9999

## Raster creation
driver = gdal.GetDriverByName('GTiff')
outDataset = driver.Create(rasname, cols, rows, 1, rastype)
proj = osr.SpatialReference()
proj.ImportFromEPSG(EPSG)
outDataset.SetProjection(proj.ExportToWkt())
outDataset.SetGeoTransform((Xmin, pixel, 0.0, Ymax, 0.0, -1 * pixel))
outBand = outDataset.GetRasterBand(1)
outBand.SetNoDataValue(nodata)

## Writing
outBand.WriteArray(data)
outDataset = None
```

## Raster Processing by Blocks

This script computes a raster using array programming by blocks.

```python
from osgeo import gdal
import numpy

gdal.AllRegister()

inras = r"C:\Dataset\Input.tif"
outras = r"C:\Dataset\Output.tif"

## GET INPUT INFO
dataset = gdal.Open(inras, gdal.GA_ReadOnly)
geot = dataset.GetGeoTransform()
proj = dataset.GetProjection()
band = dataset.GetRasterBand(1)
cols = dataset.RasterXSize
rows = dataset.RasterYSize
nd = band.GetNoDataValue()

## SET OUTPUT INFO
driver = dataset.GetDriver()
outDataset = driver.Create(outras, cols, rows, 1, gdal.GDT_Float32)
outDataset.SetGeoTransform((geot[0], geot[1], geot[2], geot[3], geot[4], geot[5]))
outDataset.SetProjection(proj)
outBand = outDataset.GetRasterBand(1)
outBand.SetNoDataValue(nd)

# SET BLOCK SIZE
blockSizes = band.GetBlockSize()
xBlockSize = blockSizes[0]
yBlockSize = blockSizes[1]

## ITERATION BY BLOCKS
for i in range(0, rows, yBlockSize):
    if i + yBlockSize < rows:
        numRows = yBlockSize
    else:
        numRows = rows - i
    for j in range(0, cols, xBlockSize):
        if j + xBlockSize < cols:
            numCols = xBlockSize
        else:
            numCols = cols - j

        arr = band.ReadAsArray(j, i, numCols, numRows)
        data = numpy.where(arr == nd, numpy.nan, arr)

        ## Do data computation -> outdata

        outBand.WriteArray(outdata, j, i)

outDataset = None
```
