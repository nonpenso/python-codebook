# Working with Tables

## Field Properties

List field properties of a shapefile:

```python
fields = arcpy.ListFields("c:/shape.shp")
for field in fields:
    print(field.name, field.type, field.scale, field.precision, field.length)
```

## Add Fields

This function adds a field to a feature layer, shapefile, or raster file.

```python
arcpy.AddField_management(<layer>, <field name>, <field type>, <precision>, <field scale>, <field length>)
```

| Field Type | Description |
|-----------|-------------|
| TEXT | Names or other textual qualities |
| FLOAT | Numeric values with fractional values within a specific range |
| DOUBLE | Numeric values with fractional values within a specific range |
| SHORT | Numeric values without fractional values within a specific range; coded values |
| LONG | Numeric values without fractional values within a specific range |
| DATE | Date and/or time |

## Table Editing

Cursors are used to access and iterate over the attribute tables of a feature class.

| Cursor | Purpose |
|--------|---------|
| `arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})` | Reading rows |
| `arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})` | Updating or deleting rows |
| `arcpy.da.InsertCursor(in_table, field_names)` | Inserting rows |

### Search

```python
with arcpy.da.SearchCursor(layer, ['fieldA', 'fieldB']) as cursor:
    for row in cursor:
        print(row[0], row[1])
```

### Update and Delete

```python
with arcpy.da.UpdateCursor(layer, ["roadtype", "distance"]) as cursor:
    for row in cursor:
        row[1] = row[0] * 100
        cursor.updateRow(row)

with arcpy.da.UpdateCursor(layer, ["roadtype"]) as cursor:
    for row in cursor:
        if row[0] == 4:
            cursor.deleteRow()
```

### Insert

```python
cursor = arcpy.da.InsertCursor(layer, ["roadID", "Length"])
cursor.insertRow([0, 100])
```

## Geometries

| Token | Description |
|-------|-------------|
| `SHAPE@` | A geometry object for the feature |
| `SHAPE@XY` | A tuple of the feature's centroid x,y coordinates |
| `SHAPE@X` | A double of the feature's x-coordinate |
| `SHAPE@AREA` | A double of the feature's area |
| `SHAPE@LENGTH` | A double of the feature's length |
| `SHAPE@TRUECENTROID` | A tuple of the feature's true centroid x,y coordinates |

```python
with arcpy.da.SearchCursor(infc, ['SHAPE@XY']) as cursor:
    for row in cursor:
        x, y = row[0]

with arcpy.da.SearchCursor(infc, ['SHAPE@AREA']) as cursor:
    for row in cursor:
        area = row[0]

with arcpy.da.SearchCursor(infc, ['SHAPE@']) as cursor:
    for row in cursor:
        area = row[0].area
```

### Count of Vertices

```python
shp = r'\temp\shield.shp'
features = [feature[0] for feature in arcpy.da.SearchCursor(shp, "SHAPE@")]
count_vertices = sum([f.pointCount - f.partCount for f in features])

## Alternative (slower)
polys = []
with arcpy.da.SearchCursor(shp, ["SHAPE@"]) as cursor:
    for row in cursor:
        polys.append(row[0].pointCount)
print(sum(polys))
```

## Selection with SQL Queries

Some functions need an SQL expression to query table attributes, such as `Select_analysis` (Shape Analysis), `SelectLayerByAttribute` (Data Management), or `Extract by Attributes` (Spatial Analyst).

The clause of a query must be a string with the SQL expression.

### Single Clause

```python
in_features = "cities.shp"
out_feature_class = "cities_Class4.shp"
clause = '"CLASS" = 4'
arcpy.Select_analysis(in_features, out_feature_class, clause)
```

### In a Loop

```python
in_features = "cities.shp"
for clas in ['3', '4']:
    clause = "{} = '{}'".format("FIELD", clas)
    selection = arcpy.SelectLayerByAttribute_management(in_features, "NEW_SELECTION", clause)
    arcpy.CopyFeatures_management(selection, 'cities_Class%s.shp' % (clas))
```

If the clause needs to change according to a variable, the string must be concatenated. Examples of SQL strings:

```python
clause = '"CLASS" = %s' % 4               # -> '"CLASS" = 4'
clause = '"CLASS" = {}'.format(4)          # -> '"CLASS" = 4'

clause = '"NUTS" = \'%s\'' % "AT111"      # -> '"NUTS" = 'AT111''
clause = '"NUTS" = \'{}\''.format('AT111') # -> '"NUTS" = 'AT111''

clause = '"COSN5" LIKE \'%s\'' % "3.1.3%" # -> '"COSN5" LIKE '3.1.3%''
clause = '"COSN5" LIKE \'{}\''.format('3.1.3%')

clause = '"%s" = 10' % "T20"              # -> '"T20" = 10'
clause = '"{}" = 10'.format('T20')        # -> '"T20" = 10'
```

## Raster Table

```python
ras_file = "majorrds.tif"
data = {row[0]: row[1] for row in arcpy.da.SearchCursor(ras_file, ['Value', 'Count'])}
```
