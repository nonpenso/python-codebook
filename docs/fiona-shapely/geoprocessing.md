# Geoprocessing

## Geoprocessing Functions

Functions with geometries:

| Function | Description | Syntax |
|----------|-------------|--------|
| **Area** | Area of polygon | `geom.area` |
| **Bounds** | Geometry extent: minX, minY, maxX, maxY | `geom.bounds` |
| **Length** | Length of geometry | `geom.length` |
| **Centroid** | Centroid of geometry | `geom.centroid` |
| **Buffer** | Buffer | `geom.buffer('width')` |
| **Distance** | Distance between two geometries | `geom1.distance(geom2)` |
| **Intersection** | Provides the overlapped area | `geom1.intersection(geom2)` |
| **Union** | Union of geometries, separating the overlapped area | `geom1.union(geom2)` |
| **Cascading Unions** | Union of a list of geometries, separating the overlapped area | `cascaded_union([geom1, geom2, geom3...])` |
| **Difference** | Erases the overlapped area | `geom1.difference(geom2)` |
| **SymDifference** | Erases the non-overlapped area | `geom1.symmetric_difference(geom2)` |

## Example

```python
import fiona
import shapely.geometry as shp

sch = {'geometry': 'Polygon',
       'properties': {'Area': 'float:13.3'}}

data1_shp = r'C:\Data\data1.shp'
data2_shp = r'C:\Data\data2.shp'
targt_shp = r'C:\Data\target.shp'

with fiona.open(targt_shp, 'w', driver='ESRI Shapefile', schema=sch) as output:

    for feat1 in fiona.open(data1_shp):
        geom1 = shp.shape(feat1['geometry'])

        for feat2 in fiona.open(data2_shp):
            geom2 = shp.shape(feat2['geometry'])

            if geom1.intersects(geom2):
                interc = geom1.intersection(geom2)
                area = interc.area

                output.write({'geometry': shp.mapping(interc),
                              'properties': {'Area': area}})
```
