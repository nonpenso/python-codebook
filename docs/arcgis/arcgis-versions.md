# Python ArcGIS 9.3 vs ArcGIS 10.0

ArcGIS 9.3 and 10.0 have different ways to access Geoprocessing Tools through Python. Generally a script needs to:

- Import the ArcGIS module
- Create the geoprocessor object
- Check the licenses

## Comparison between versions

| Feature | ArcGIS 9.3 | ArcGIS 10.0+ |
|---------|-------------|--------------|
| Import module | `import arcgisscripting` | `import arcpy` |
| Create geoprocessor | `gp = arcgisscripting.create(9.3)` | Not needed — `arcpy` is ready to use |
| Check out extensions | `gp.CheckOutExtension("spatial")` | `arcpy.CheckOutExtension("spatial")` |
| Load toolboxes | Required manually | No longer necessary |
| Overwrite output | `gp.OverWriteOutput = 1` | `arcpy.env.overwriteOutput = True` |
| Set workspace | `gp.workspace = "E:\\temp"` | `arcpy.env.workspace = "E:\\temp"` |

!!! note
    Modern ArcGIS (10.x and ArcGIS Pro) uses `import arcpy` directly. The old `arcgisscripting.create()` pattern is obsolete and should not be used in new scripts.

## Migrating from 9.3 to 10.0+

The tool names are the same for both versions — only the imported module changes from `gp` to `arcpy`.

A quick trick to update old scripts (rather than doing a find/replace of all references) is to change the module name:

```python
import arcpy as gp
```

To update a script from 9.3 to 10.0+:

1. Replace `import arcgisscripting` with `import arcpy`
2. Remove the geoprocessor object creation line
3. Remove ToolBox loading statements
4. Replace `gp.` with `arcpy.` (or use the alias trick above)

## Further information

- [What's new for geoprocessing in ArcGIS 10](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/What_s_new_for_geoprocessing_in_ArcGIS_10/00qp0000000q000000/)
- [The ArcPy site package](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#//000v000000v7000000.htm)
- [Geoprocessing with Python: Importing ArcPy](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/Importing_ArcPy/002z00000008000000/)
