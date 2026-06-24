# Mapping

The ESRI Python library provides a module to manipulate `.mxd` files with functions to automate managing, exporting, and printing.

To access a map document (.mxd) properties and methods, create a Python object as shown below:

```python
>>> import arcpy
>>> mxd = arcpy.mapping.MapDocument(r"C:\Project\Project.mxd")
```

## Functions

| Function | Description |
|----------|-------------|
| `arcpy.mapping.ListDataFrames(map, [wildcard])` | Returns the list of DataFrame objects within a single map. Also used to return a DataFrame object. |
| `arcpy.mapping.ListLayers(map, [wildcard], [dataframe])` | Returns the list of Layer objects within a single dataframe. Also used to return a Layer object. |
| `arcpy.mapping.ListLayoutElements(map, [element_type], [wildcard])` | Returns elements from a page layout (not map annotations). Types: "DATAFRAME_ELEMENT", "GRAPHIC_ELEMENT", "LEGEND_ELEMENT", "MAPSURROUND_ELEMENT", "PICTURE_ELEMENT", "TEXT_ELEMENT" |
| `arcpy.mapping.InsertLayer(dataframe, reference_layer, insert_layer, [insert_position])` | Inserts a layer at a specific location within a dataframe |

## Object Properties

Any objects (dataframes, layers, elements, etc.) provide access to important properties. You can get or set position, change text, modify rotation, and more. The Python object is created by assigning a variable to an item from the list of objects.

For example, given 2 dataframes (DF1 and DF2), to work on DF2: create the list of dataframes selecting only DF2 with a wildcard. The list has only one item. The object will be the item at position `[0]`.

```python
>>> dataframe_list = arcpy.mapping.ListDataFrames(mxd, "DF2")
>>> dataframe_obj = dataframe_list[0]
```

### DataFrame Properties

| Property | Description |
|----------|-------------|
| name | DataFrame's name as it appears in the table of contents |
| displayUnits | Data frame distance units |
| elementHeight/Width | Height or width of the element in page units |
| elementPositionX/Y | X or Y location of the data frame element's anchor position in page units |
| extent | Map extent using map coordinates (map units) |
| mapUnits | Data frame map units |
| referenceScale | Data frame's reference scale |
| scale | Scale of the active data frame |
| panToExtent | Pans and centers the data frame extent using an extent object |

### Layer Properties

| Property | Description |
|----------|-------------|
| name | Name of a layer as it appears in the ArcMap table of contents |
| isFeatureLayer | True/False if layer is a Feature Class |
| isGroupLayer | True/False if layer is a Group of layers |
| isRasterLayer | True/False if layer is a Raster |
| dataSource | The complete path for the layer's data source |
| definitionQuery | Get or set a layer's definition query |
| brightness/contrast | Get or set brightness and contrast value (between +100% and -100%) |
| visible | Controls the display of a layer |

### GraphicElement Properties

| Property | Description |
|----------|-------------|
| name | Name of the element |
| elementHeight/Width | Height or width in page units |
| elementPositionX/Y | X or Y location of the anchor position in page units |

### TextElement Properties

| Property | Description |
|----------|-------------|
| name | Name of the element |
| elementHeight/Width | Height or width in page units |
| elementPositionX/Y | X or Y location of the anchor position in page units |
| text | The text string associated with the element |

## Usage Example

```python
>>> dataframes_list = arcpy.mapping.ListDataFrames(mxd)
>>> for df in dataframes_list:
...     print(df.name)
...     print(df.extent)
...     print(df.displayUnits)
Layers
2624322.3646503 1340246.53411237 6536340.36465029 5431630.53411241
Meters
>>> dataframe = arcpy.mapping.ListDataFrames(mxd)[0]
>>> list_layers = arcpy.mapping.ListLayers(mxd, "*", dataframe)
>>> for lyr in list_layers:
...     print(lyr.name, lyr.dataSource, lyr.visible)
NUTS, C:\Project\NUTS.shp, True
Rivers, C:\Project\rivers.shp, True
Samples, C:\Project\sample_points.shp, False
```

## Complete Example

This script inserts a new shapefile layer, applies symbology from another layer, changes the title text of the map, and saves a copy of the project.

```python
import arcpy

# Create the map object
mxd = arcpy.mapping.MapDocument(r"C:\Project\Project.mxd")

# Create the dataframe object
dataframe = arcpy.mapping.ListDataFrames(mxd)[0]

# Create the layer objects
ref_layer = arcpy.mapping.ListLayers(mxd, "ref_layer", dataframe)[0]
my_layer = arcpy.mapping.Layer(r"C:\Project\mylayer.shp")

# Change symbology and insert layer
arcpy.ApplySymbologyFromLayer_management(my_layer, ref_layer)
arcpy.mapping.InsertLayer(dataframe, ref_layer, my_layer, "AFTER")

# Change the title text
elems = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "Title")[0]
elems.text = "Map of my layer"

# Save a copy of the project
mxd.saveACopy(r"C:\Project\Project1.mxd")
del mxd
```
