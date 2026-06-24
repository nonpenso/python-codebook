# Raster Operations

There are three different ways to perform raster operations (addition, multiplication, division, etc.) and conditional statements (less than, greater than, equal to, not equal to, etc.) with Python:

1. **Math Function** — Processing a specific function from the ArcToolBox Math toolset (works only with two rasters)
2. **Map Algebra** — Processing the operation with Single Output Map Algebra
3. **Raster Object** — Processing with the `sa` (Spatial Analyst) module

```python
# This script calculates the addition of two rasters in 3 different ways

# Import arcpy module
import arcpy
import arcpy.sa as arcsa
arcpy.CheckOutExtension("spatial")

# Define the two rasters
raster1 = "E:\\Temp\\raster1"
raster2 = "E:\\Temp\\raster2"

### Method 1: Math Function
result_plus = "E:\\Temp\\result_plus"
arcpy.Plus_sa(raster1, raster2, result_plus)

### Method 2: Single Output Map Algebra
result_Alg = "E:\\Temp\\result_Alg"
arcpy.SingleOutputMapAlgebra_sa(
    raster1 + " + " + raster2, result_Alg, raster1 + ";" + raster2
)

### Method 3: Raster Object (Spatial Analyst)
result_Obj = "E:\\Temp\\result"
outRas = arcsa.Raster(raster1) + arcsa.Raster(raster2)
outRas.save(result_Obj)
```

:::{note}
The Raster Object method (Method 3) using `arcpy.sa` is the recommended approach in modern ArcGIS Python scripting, as it provides cleaner syntax and supports chaining multiple operations.
:::
