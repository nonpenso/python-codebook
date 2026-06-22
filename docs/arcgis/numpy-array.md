# NumPy Array

## Raster to/from Array

Raster files can be easily converted to NumPy arrays and back with two ESRI ArcPy functions:

### RasterToNumPyArray

`RasterToNumPyArray(in_raster, {lower_left_corner}, {ncols}, {nrows}, {nodata_to_value})`

| Parameter | Description |
|-----------|-------------|
| in_raster | Input raster |
| lower_left_corner | The lower left corner within the input raster from which to extract the processing block. The x- and y-values are in map units |
| ncols/nrows | The number of columns/rows from the lower_left_corner to convert. Default is the number of columns in the input raster |
| nodata_to_value | The value to assign to NoData cells in the resulting NumPy array. If not specified, the NoData value associated with the raster is used |

### NumPyArrayToRaster

`NumPyArrayToRaster(in_array, {lower_left_corner}, {x_cell_size}, {y_cell_size}, {value_to_nodata})`

| Parameter | Description |
|-----------|-------------|
| in_array | Input array |
| lower_left_corner | The lower left corner of the output raster. X and Y values are in map units; default is 0.0 |
| x/y_cell_size | The cell size in the x/y direction in map units; default is 1.0 |
| value_to_nodata | The value in the NumPy array to assign as NoData in the output raster. If not specified, no NoData values will be set |

More info:

- [RasterToNumPyArray](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/RasterToNumPyArray/000v0000012z000000/)
- [NumPyArrayToRaster](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/NumPyArrayToRaster/000v00000130000000/)

## Array Operation

This script computes the median value of three rasters converted to arrays. To handle large rasters, a tiling method is used with 100-pixel blocks.

Steps:

1. Import the raster spatial info
2. Create an empty raster
3. Iterate through the tiles
4. Convert rasters to arrays
5. Create a 3D array
6. Compute the median
7. Add each tile to the empty raster

```python
import arcpy
import numpy

rast1 = r"C:\temp\ras1.tif"
rast2 = r"C:\temp\ras2.tif"
rast3 = r"C:\temp\ras3.tif"

# Import raster info
desc = arcpy.Describe(rast1)
ext = desc.Extent
xmin = ext.XMin
ymin = ext.YMin
rows = desc.height
cols = desc.width
width = desc.meanCellWidth
height = desc.meanCellHeight
sp_ref = desc.spatialReference
nodata = desc.noDataValue

# Tile size
xBSize = 100
yBSize = 100

# Create empty raster
result = arcpy.CreateRasterDataset_management(
    r"C:\temp", "result.tif", width, "32_BIT_SIGNED", sp_ref, 1
)

# Iterate through tiles
for i in range(0, rows, yBSize):
    if i + yBSize < rows:
        numRows = yBSize
    else:
        numRows = rows - i
    for j in range(0, cols, xBSize):
        if j + xBSize < cols:
            numCols = xBSize
        else:
            numCols = cols - j
        xtile = xmin + (j * width)
        ytile = ymin + (i * height)
        lowleft = arcpy.Point(xtile, ytile)

        # Convert rasters to arrays
        array1 = arcpy.RasterToNumPyArray(rast1, lowleft, numCols, numRows, numpy.nan)
        array2 = arcpy.RasterToNumPyArray(rast2, lowleft, numCols, numRows, numpy.nan)
        array3 = arcpy.RasterToNumPyArray(rast3, lowleft, numCols, numRows, numpy.nan)

        # Create 3D array
        union = numpy.dstack((array1, array2, array3))
        # Compute the median along the 3rd axis
        med = numpy.median(union, axis=2)

        # Convert array to raster and add to the empty raster
        res = arcpy.NumPyArrayToRaster(med, lowleft, width, height, nodata)
        arcpy.Mosaic_management(res, result)

del array1, array2, array3, union, med, res
```
