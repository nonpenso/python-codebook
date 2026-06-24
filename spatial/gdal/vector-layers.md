# Vector Layers

## Opening a Vector File

Open methods:

| Mode | Description |
|------|-------------|
| `0` | Read only |
| `1` | Write |

```python
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')
fn = r'C:\data\sites.shp'
dataSource = driver.Open(fn, 0)
layer = dataSource.GetLayer()
```

## Getting Info

```python
# Name
name = layer.GetName()

# Number of features
numFeatures = layer.GetFeatureCount()

# Extent: Xmin, Xmax, Ymin, Ymax
extent = layer.GetExtent()
print('UL:', extent[0], extent[3])
print('LR:', extent[1], extent[2])

# Spatial reference
sRef = layer.GetSpatialRef()
sRefText = sRef.ExportToWkt()
EPSG = sRef.GetAuthorityCode(None)

# Geometry type
type_num = layer.GetGeomType()
type_name = ogr.GeometryTypeToName(type_num)
```

Geometry types:

| Type Number | Type Name |
|-------------|-----------|
| `0` | Unknown (any) |
| `1` | Point |
| `2` | Line String |
| `3` | Polygon |
| `4` | Multi Point |
| `5` | Multi Line String |
| `6` | Multi Polygon |

## Tables

```python
# Field info
layerDef = layer.GetLayerDefn()
for i in range(layerDef.GetFieldCount()):
    fieldDef = layerDef.GetFieldDefn(i)

    fieldName = fieldDef.GetName()
    fieldTypeCode = fieldDef.GetType()
    fieldType = fieldDef.GetFieldTypeName(fieldTypeCode)
    fieldWidth = fieldDef.GetWidth()
    fieldPrecision = fieldDef.GetPrecision()

# Field values
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    dict_feature = feature.items()
    value = feature.GetField("FIELD")
```

## Geometry

```python
# Feature by FID
feature = layer.GetFeature(0)
geometry = feature.GetGeometryRef()

feat_numb = geometry.GetGeometryCount()
geotype = geometry.GetGeometryName()

# Point
x = geometry.GetX()
y = geometry.GetY()

# Polygon
area = geometry.GetArea()
centroid = geometry.Centroid().GetPoint()

ring = geometry.GetGeometryRef(0)
vertex_num = ring.GetPointCount()
for vertex in range(vertex_num):
    lat, lon, z = ring.GetPoint(vertex)
```

## Filtering

### Attribute Filtering

```python
>>> layer.GetFeatureCount()
42
>>> layer.SetAttributeFilter("cover = 'shrubs'")
>>> layer.GetFeatureCount()
6
>>> layer.SetAttributeFilter(None)
>>> layer.GetFeatureCount()
42
```

### Spatial Filtering

```python
# By extent
layer.SetSpatialFilterRect(Xmin, Ymin, Xmax, Ymax)

# By a polygon
polygon = poly.GetFeature(0)
polyGeom = polygon.GetGeometryRef()
layer.SetSpatialFilter(polyGeom)
```

## Delete Objects

```python
feature.Destroy()
dataSource.Destroy()
```
