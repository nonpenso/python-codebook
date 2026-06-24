# Layer Info

## Describe

The `Describe` function returns a Describe object. The output contains properties such as data type, fields, indexes, and many others. Its properties are dynamic, meaning that depending on what data type is described, different properties will be available.

First, create the object:

```python
import arcpy

layer = r"C:\Temp\layer"
desc = arcpy.Describe(layer)
```

Then access the object properties with different methods:

### File Properties

| Property | Description |
|----------|-------------|
| `desc.path` | The file path |
| `desc.file` | The file name |
| `desc.extension` | The file extension |
| `desc.dataType` | The type of the element |
| `desc.spatialReference.name` | The spatial reference |
| `desc.spatialReference.factorycode` | The code of spatial reference |

### Layer Properties

| Property | Description |
|----------|-------------|
| `desc.shapeType` | Polygon, Polyline, Point, MultiPoint, MultiPatch |
| `desc.datasetType` | FeatureClass, RasterDataset, Table, Toolbox, etc. |
| `desc.Extent.{XMin}{YMin}{XMax}{YMax}{ZMin}{ZMax}{MMin}{MMax}` | The extent object |

### Raster Properties

| Property | Description |
|----------|-------------|
| `desc.height` | The number of rows |
| `desc.width` | The number of columns |
| `desc.meanCellHeight` | The cell size in Y direction |
| `desc.meanCellWidth` | The cell size in X direction |
| `desc.noDataValue` | The NoData value of the raster band |
| `desc.pixelType` | The pixel type: U1 (1 bit), U2 (2 bits), U4 (4 bits), U8 (unsigned 8-bit), S8 (signed 8-bit), U16 (unsigned 16-bit), S16 (signed 16-bit), U32 (unsigned 32-bit), S32 (signed 32-bit), F32 (single precision float), F64 (double precision float) |
| `desc.bandCount` | The number of bands in the raster dataset |
| `desc.format` | The raster format: GRID, ERDAS IMAGINE, TIFF |

## Raster Properties

The `GetRasterProperties` function returns properties of a raster dataset. The Python result always returns a geoprocessing object. To obtain the actual string value, use `result.getOutput(0)`.

```python
arcpy.GetRasterProperties_management(in_raster, "{property_type}")
```

### Property Types

| Property | Description |
|----------|-------------|
| `MAXIMUM` | Returns the largest value of all cells in the input raster |
| `MINIMUM` | Returns the smallest value of all cells in the input raster |
| `MEAN` | The mean value of all cells |
| `STD` | The standard deviation value of all cells |
| `UNIQUEVALUECOUNT` | The number of unique values |
| `ALLNODATA` | Returns 1 (True) or 0 (False) if the raster has only NoData values |
| `VALUETYPE` | The pixel type: 0=1-bit, 1=2-bit, 2=4-bit, 3=8-bit unsigned, 4=8-bit signed, 5=16-bit unsigned, 6=16-bit signed, 7=32-bit unsigned, 8=32-bit signed, 9=32-bit float, 10=64-bit double, 11=8-bit complex, 12=64-bit complex, 13=16-bit complex, 14=32-bit complex |
| `TOP/LEFT/RIGHT/BOTTOM` | Returns the top (YMax), left (XMin), right (XMax), or bottom (YMin) value of the extent |
| `CELLSIZEX/CELLSIZEY` | Returns the cell size in the X/Y direction |
| `ROWCOUNT/COLUMNCOUNT` | Returns the number of rows/columns in the input raster |
| `BANDCOUNT` | Returns the number of bands in the input raster |

```python
>>> elevSTD = arcpy.GetRasterProperties_management("c:/data/elevation", "STD")
>>> elevSTD.getOutput(0)
u'246.54'
```

## Cell Value

The `GetCellValue_management` function retrieves the pixel value at a specific X,Y coordinate and (optionally) band.

```python
arcpy.GetCellValue_management(in_raster, xy_point, {band})
```

```python
>>> pixval = arcpy.GetCellValue_management("C:/data/clc.tif", "4496874 2448865")
>>> cellSize = pixval.getOutput(0)
u'12'
```
