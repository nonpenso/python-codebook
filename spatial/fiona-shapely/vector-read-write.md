# Vector Read-Write

## Vector File Info

```python
import fiona

shp = r'C:\Data\polygons.shp'
source = fiona.open(shp, 'r', driver='ESRI Shapefile')

## INFO
projection = source.crs
projection_text = source.crs_wkt
feature_count = len(source)
table_fields = source.schema['properties']

## TABLE VALUES
for feature in source:
    print(feature['properties']['Id'])

## GEOMETRIES
for feature in source:
    geometry = feature['geometry']

source.close()
```

## Vector Write

```python
source_shp = r'C:\Data\data1.shp'
target_shp = r'C:\Data\data2.shp'

with fiona.open(source_shp) as source:
    source_driver = source.driver       # 'ESRI Shapefile'
    source_proj = source.crs            # Projection
    source_schema = source.schema       # Geometry type, table fields

with fiona.open(target_shp, 'w',
                driver=source_driver,
                crs=source_proj,
                schema=source_schema) as target:
    for feature in source:
        target.write({'geometry': feature['geometry'],
                      'properties': {'table_field': 100}})
```
