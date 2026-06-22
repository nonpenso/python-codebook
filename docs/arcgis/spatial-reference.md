# Spatial Reference

The `SpatialReference` object has a number of properties that define the map projection. It can be easily retrieved from a layer with `Describe()` and manipulated.

## Getting Spatial Reference

How to get spatial reference name and codes from a layer:

```python
dataset = r"C:\Data\Landbase.shp"

sr_name = arcpy.Describe(dataset).spatialReference.name
sr_code = arcpy.Describe(dataset).spatialReference.factoryCode
sr_wkt = arcpy.Describe(dataset).spatialReference.exportToString()
```

## Setting and Reprojecting

```python
import arcpy

# Layer with unknown reference
mylyr = r"C:\Data\waterbasin"

# Create the spatial reference object in LAEA
sr = arcpy.SpatialReference(3035)

# Define the projection
arcpy.DefineProjection_management(mylyr, sr)

# Reproject to WGS84 creating a new spatial reference
del sr
newsr = arcpy.SpatialReference(4326)
newlyr = r"C:\Data\waterbasin_WGS"

# Vector file
arcpy.Project_management(mylyr, newlyr, newsr, "ETRS_1989_To_WGS_1984")

# Raster file
resampling_type = "CUBIC"
cell_size = 1000
arcpy.ProjectRaster_management(mylyr, newlyr, newsr, resampling_type, cell_size, "ETRS_1989_To_WGS_1984")
```

## Common Spatial References

| Spatial Reference Name | EPSG Code |
|----------------------|-----------|
| ETRS_1989_LAEA | 3035 |
| GCS_WGS_1984 | 4326 |

!!! note
    Use `arcpy.SpatialReference(EPSG_code)` to create a spatial reference object from an EPSG code. This is the simplest and most portable way to define coordinate systems in ArcPy scripts.
