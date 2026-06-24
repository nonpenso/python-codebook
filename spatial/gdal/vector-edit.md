# Vector Edit

## Editing

```python
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')

shp = r'C:\data\sites.shp'

# Open as 1 to write
dataSource = driver.Open(shp, 1)
layer = dataSource.GetLayer()

# Create new feature
layer_defn = layer.GetLayerDefn()
newfeature = ogr.Feature(layer_defn)

# Set an FID index
newfeature.SetFID(0)

# Set a new geometry
newfeature.SetGeometry(point)  # point/line/polygon

# Add feature to layer
layer.CreateFeature(newfeature)
```

## Create New Geometries

| Operation | Method |
|-----------|--------|
| Add new point | `AddPoint(<x>, <y>, [<z>])` |
| Modify point | `SetPoint(<index>, <x>, <y>, [<z>])` |

```python
# Point
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10, 20)

# Line
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10, 10)
line.AddPoint(20, 20)
line.SetPoint(0, 30, 30)  # (10,10) -> (30,30)

# Polygon
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(0, 0)
ring.AddPoint(100, 0)
ring.AddPoint(100, 100)
ring.AddPoint(0, 100)
ring.CloseRings()

polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(ring)
```

## New Layer

Field types:

| Type | Description |
|------|-------------|
| `ogr.OFTInteger` | Integer numbers |
| `ogr.OFTReal` | Float numbers |
| `ogr.OFTString` | Strings |
| `ogr.OFTDate` | Dates |

This script:

- Creates a point vector file `sample.shp`
- Adds a new field `NEWFIELD`
- Adds a new feature point with coordinates and a value of 9999

```python
import ogr, osr

path = r"E:\Spatial\Shape"

driver = ogr.GetDriverByName("ESRI Shapefile")

# Define spatial reference
laearef = osr.SpatialReference()
laearef.ImportFromEPSG(3035)

# Create the shapefile
datasource = driver.CreateDataSource(path)
layer = datasource.CreateLayer('sample', laearef, geom_type=ogr.wkbPoint)

# Add new field
layer_defn = layer.GetLayerDefn()
field_def = ogr.FieldDefn('NEWFIELD', ogr.OFTInteger)
field_def.SetWidth(4)
field_def.SetPrecision(0)
layer.CreateField(field_def)

# Populate with geometry
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(3254159.2, 4586973.6)

featureIndex = 0  # FID value
feature = ogr.Feature(layer_defn)
feature.SetGeometry(point)
feature.SetFID(featureIndex)
layer.CreateFeature(feature)

feature.SetField('NEWFIELD', 9999)
layer.SetFeature(feature)

datasource.Destroy()
```

## Update Attributes

```python
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(r'C:\data\sites.shp', 1)
layer = dataSource.GetLayer()

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    feature.SetField('NEWFIELD', 12345)
    layer.SetFeature(feature)

dataSource.Destroy()
```

## Copy Features

```python
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')

# Copy from source
dataSource = driver.Open(r'C:\data\layer1.shp', 0)
layerSource = dataSource.GetLayer()
featureSource = layerSource.GetFeature(158)  # get the feature with FID = 158
geom = featureSource.GetGeometryRef()

# Create new feature and paste
dataTarget = driver.Open(r'C:\data\layer2.shp', 1)
layerTarget = dataTarget.GetLayer()
newfeature = ogr.Feature(layerTarget.GetLayerDefn())
newfeature.SetGeometry(geom)
newfeature.SetField('ID', 158)
layerTarget.CreateFeature(newfeature)

dataTarget.Destroy()
dataSource.Destroy()
```
