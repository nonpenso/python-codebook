# Geoprocessing

## Geoprocessing Functions

Functions with geometries:

| Function | Description | Syntax |
|----------|-------------|--------|
| **Buffer** | Buffer | `outgeom = ingeom.Buffer('width')` |
| **Centroid** | Centroid of the polygon | `outgeom = ingeom.Centroid()` |
| **Simplify** | Simplification of the geometry | `outgeom = ingeom.Simplify()` |
| **Distance** | Distance between two geometries | `outgeom = ingeom.Distance(ingeom2)` |
| **Intersection** | Provides the overlapped area | `outgeom = ingeom1.Intersection(ingeom2)` |
| **Union** | Union of geometries, separating the overlapped area | `outgeom = ingeom1.Union(ingeom2)` |
| **Difference** | Erases the overlapped area | `outgeom = ingeom1.Difference(ingeom2)` |
| **SymDifference** | Erases the non-overlapped area | `outgeom = ingeom1.SymDifference(ingeom2)` |

## Example

```python
import ogr, osr

driver = ogr.GetDriverByName('ESRI Shapefile')
laearef = osr.SpatialReference()
laearef.ImportFromEPSG(3035)

# Open two layers
ds1 = driver.Open(r'C:\data\layer1.shp', 0)
ds2 = driver.Open(r'C:\data\layer2.shp', 0)
lyr1 = ds1.GetLayer()
lyr2 = ds2.GetLayer()

# Create an empty layer
ds3 = driver.CreateDataSource(r'C:\data\output.shp')
lyr3 = ds3.CreateLayer('output', laearef, geom_type=ogr.wkbPolygon)
layer_defn = lyr3.GetLayerDefn()

# Iterate through features
for n in range(lyr1.GetFeatureCount()):
    feature1 = lyr1.GetFeature(n)
    geom1 = feature1.GetGeometryRef()
    attribute1 = feature1.GetField('Id')

    for i in range(lyr2.GetFeatureCount()):
        feature2 = lyr2.GetFeature(i)
        geom2 = feature2.GetGeometryRef()
        attribute2 = feature2.GetField('Id')

        if geom1.Intersects(geom2):
            intersection = geom2.Intersection(geom1)

            dstfeature = ogr.Feature(layer_defn)
            dstfeature.SetGeometry(intersection)
            lyr3.CreateFeature(dstfeature)
            dstfeature.Destroy()

ds1.Destroy()
ds2.Destroy()
ds3.Destroy()
```
