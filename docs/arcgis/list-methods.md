# List Methods

List methods can be used to retrieve lists of items to process, such as shapefiles, grids, tables, or fields in a table. Even if GIS objects have multiple files associated (e.g., shapefiles or grid rasters), the geoprocessor allows listing those objects as ESRI recognizes them.

**Wildcard** is a string with characters to help limit the results. An asterisk (`*`) is used for missing characters; use only `*` to return all items. For example, listing all features with the word "tile" anywhere in the name would use a wildcard `*tile*`.

| Function | Parameters |
|----------|------------|
| `arcpy.ListFeatureClasses({Wildcard},{Type})` | Wildcard (optional); Type (optional): "POINT", "LINE", "POLYGON", "LABEL" |
| `arcpy.ListRasters({Wildcard},{Type})` | Wildcard (optional); Type (optional): "GRID", "TIF", "JPG", "GIF", "IMG", etc. |
| `arcpy.ListTables({Wildcard},{Type})` | Wildcard (optional); Type (optional): "dBase", "INFO" |
| `arcpy.ListFields(Table,{Wildcard},{Type})` | Table (required): dbTable, shapefile, grid; Wildcard (optional); Type (optional): Integer, Single, Double, String, Date |

## Examples

### List polygon shapefiles starting with N

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "E:\\myfolder"

# List polygon shapefiles starting with the N character
fcs = arcpy.ListFeatureClasses("N*", "POLYGON")

# Print the list
print(fcs)
```

### Check if a field exists in a shapefile

```python
import arcpy

# Shapefile to check
shapefile = "E:\\myshapefile.shp"

# The field name
fieldtocheck = "NAME"

# Create a list of fields from a shapefile using the wildcard "NAME".
# If the field "NAME" exists, it returns a list containing one item;
# otherwise the list will be empty.
fields = arcpy.ListFields(shapefile, "NAME")

# If the length of the list is zero (empty), the field doesn't exist
if len(fields) == 0:
    print("The field " + fieldtocheck + " doesn't exist")
else:
    print("The field " + fieldtocheck + " exists")
```

### List and print TIF raster paths

```python
import arcpy

# Set the workspace where rasters are
workfolder = "E:\\myfolder"
arcpy.env.workspace = workfolder

# List TIF rasters starting with DEM characters
rasters = arcpy.ListRasters("DEM*", "TIFF")

# Iterate the objects of the list and print the full path
for raster in rasters:
    print(workfolder + "\\" + raster)
```

### Add a filename field to shapefiles

This script adds a text field to the attribute tables of shapefiles and writes the name of each shapefile as the field value.

```python
import arcpy

# Set the workspace where shapefiles are
arcpy.env.workspace = "E:\\myfolder"

# List point shapefiles in the folder
fcs = arcpy.ListFeatureClasses("*", "POINT")

# Iterate through the list
for fc in fcs:
    # Define the name of the new field
    fieldname = "FILENAME"
    # Add a text field with length 20
    arcpy.AddField_management(fc, fieldname, "TEXT", "", "", "20", "", "NON_NULLABLE", "NON_REQUIRED", "")
    # Define the expression:
    # fc is the filename (e.g., myshapefile.shp)
    # Select characters from position 0 up to -4 to cut off ".shp"
    mytxt = '"' + fc[0:-4] + '"'
    # Calculate the field value
    arcpy.CalculateField_management(fc, fieldname, mytxt, "VB", "")
```
