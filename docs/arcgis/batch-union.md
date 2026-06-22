# Batch Union Features

These scripts allow batch unioning of shapefiles in a target folder into a new shapefile. The features must be the same data type (points, lines, or polygons).

## Union Tool

This script uses the `Union` tool, which needs the following parameters:

- A list of feature classes with their complete path separated by `#;`. Example: `"C:\\Myfolder\\shape1.shp #;C:\\Myfolder\\shape2.shp #;C:\\Myfolder\\shape3.shp"`
- The name of the output feature

```python
import arcpy

# Set the workspace where shapefiles are
workfolder = "E:\\myfolder"
arcpy.env.workspace = workfolder

# List all features in the folder
features = arcpy.ListFeatureClasses()

# Remove the first shapefile from list with pop([position])
firstfc = features.pop(0)

# Create the string to define the input parameter
infeatures = workfolder + "\\" + firstfc

# Iterate the features in the list
for feature in features:
    # Add the separating characters, the path, and the feature name
    infeatures += " #;" + workfolder + "\\" + feature

# Define the output feature
outfeature = workfolder + "\\union.shp"

# Process the union of features
arcpy.Union_analysis(infeatures, outfeature)
```

## Update Tool

The Union tool adds fields from every input feature to the output attribute table. To get an output with the same fields as the input features, use the `Update` tool instead — but it works only with a pair of features at a time.

It is necessary to create temporary files as intermediate results of every update. Processing *n* features will produce *n-2* intermediate files plus the final result.

```python
import arcpy

# Set the workspace where shapefiles are
workfolder = "D:\\Temp"
arcpy.env.workspace = workfolder

# List all features in the folder
features = arcpy.ListFeatureClasses()

# Remove the first and second shapefile from the list
firstfc = workfolder + "\\" + features.pop(0)
secondfc = workfolder + "\\" + features.pop(0)

# Define the output name of the first update
firstupdate = workfolder + "\\update0.shp"

# Process the first update
arcpy.Update_analysis(firstfc, secondfc, firstupdate)

# Iterate the other features in the list and enumerate them from 0
for position, feature in enumerate(features):
    # Process all features except the last one
    if position < (len(features) - 1):
        # Define one input name from the list of features
        infc = workfolder + "\\" + feature
        # Define the other input name according to its position
        inupdate = workfolder + "\\update" + str(position) + ".shp"
        # Define the output name (adding 1 to be the input for next cycle)
        outupdate = workfolder + "\\update" + str(position + 1) + ".shp"
        arcpy.Update_analysis(infc, inupdate, outupdate)
    # Process the last iteration
    if position == (len(features) - 1):
        infc = workfolder + "\\" + feature
        inupdate = workfolder + "\\update" + str(position) + ".shp"
        # Define the final output feature name
        outupdate = workfolder + "\\final_update.shp"
        arcpy.Update_analysis(infc, inupdate, outupdate)
```
