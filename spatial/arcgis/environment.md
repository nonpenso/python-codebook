# Environment Settings

Environment settings are additional parameters that affect a tool's results.

| Function | Description |
|----------|-------------|
| `arcpy.ListEnvironments([wildcard])` | Returns a Python list of geoprocessing environment names. Use `getattr()` to evaluate the environment's values |

```python
import arcpy
from arcpy import env

envlist = arcpy.ListEnvironments()

for environment in envlist:
    envSetting = getattr(env, environment)
    print("%-28s: %s" % (environment, envSetting))
```

## Main Environment Settings

```python
import arcpy

# Workspace
arcpy.env.workspace = "C:/data"
arcpy.env.scratchWorkspace = "C:/temp"
arcpy.env.overwriteOutput = True

# Extent: XMin, YMin, XMax, YMax
arcpy.env.extent = r"C:\Temp\mylayer.shp"
arcpy.env.extent = arcpy.Extent(-107.0, 38.0, -104.0, 40.0)
arcpy.env.extent = "-107.0, 38.0, -104.0, 40.0"

# Raster
arcpy.env.snapRaster = r"C:\Temp\mylayer.tif"
arcpy.env.mask = r"C:\Temp\mylayer.tif"
arcpy.env.cellSize = 100
arcpy.env.cellSize = r"C:\Temp\mylayer.tif"
arcpy.env.compression = "LZW"

# Spatial reference
arcpy.env.outputCoordinateSystem = r"C:\Temp\mylayer.tif"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(3035)
arcpy.env.outputCoordinateSystem = "WGS 1984 UTM Zone 18N.prj"
arcpy.env.geographicTransformations = "Arc_1950_To_WGS_1984_5; PSAD_1956_To_WGS_1984_6"
```

:::{note}
Always set `arcpy.env.overwriteOutput = True` at the beginning of your scripts if you want to allow overwriting existing output files. This prevents errors when re-running scripts during development.
:::
