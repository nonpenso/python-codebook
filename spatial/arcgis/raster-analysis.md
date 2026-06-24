# Raster Analysis

## Histogram

This script reads a raster in blocks, collects pixel values (excluding NoData), and creates a histogram using matplotlib.

```python
import arcpy
import numpy
import matplotlib.pyplot as plt

ras = r'C:\image.tif'

desc = arcpy.Describe(ras)
ext = desc.Extent
xmin = ext.XMin
ymin = ext.YMin
rows = desc.height
cols = desc.width
width = desc.meanCellWidth
height = desc.meanCellHeight
sp_ref = desc.spatialReference
NoData = desc.noDataValue

block = 1000

xBSize = block
yBSize = block
values = []
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
        array = arcpy.RasterToNumPyArray(ras, lowleft, numCols, numRows)
        array = array[numpy.where(array != NoData)]
        values = values + list(array)

fig, ax = plt.subplots(figsize=(10, 10))

b = list(numpy.arange(-1, 1, 0.1))  # Set bin classes
n, bins, patches = ax.hist(values, color='lime', bins=b)

ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Set number of X tick labels
ax.set_xlim(-1, 1)
ax.set_ylim(0, 100)

# Add labels above bars
for i in range(0, len(n)):
    x_pos = bins[i] + ((bins[i + 1] - bins[i]) / 2)
    y_pos = n[i] + (n[i] * 0.1)
    label = str(int(n[i]))
    ax.text(x_pos, y_pos, label, horizontalalignment='center', fontsize=9)

plt.show()
```

:::{note}
The block-based approach is essential for large rasters that don't fit entirely into memory. Adjust the `block` variable (default 1000 pixels) based on your available RAM and raster size.
:::
