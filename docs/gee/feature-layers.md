# Feature Layers

## Layer Info and Table

| Command | Description |
|---------|-------------|
| `fc.size().getInfo()` | Number of features |
| `fc.getInfo().get('features')[n].get('properties')` | Properties (dictionary) of feature n |
| `fc.getInfo().get('features')[n].get('properties').keys()` | List of field names |
| `fc.getInfo().get('features')[n].toDictionary().get('MYFIELD')` | Value of the field |

## Common Functions

| Command | Description |
|---------|-------------|
| `fc.reduceColumns(reducer=ee.Reducer.mean(), selectors=['field'])` | Statistics (mean) of column 'field' |
| `fc1.merge(fc2)` | Merge two layers |
| `fc.map(lambda feature: feature.set('Area_HA', feature.geometry().area().divide(100 * 100)))` | Area in hectares for every feature |
| `fc.map(lambda feature: feature.buffer(300))` | Buffer of 300m on every polygon |
| `fc.reduceToImage(properties=['field'], reducer=ee.Reducer.first())` | Convert feature collection to image |

```python
img = ee.Image('UMD/hansen/global_forest_change_2018_v1_6').select(['lossyear'])
AOI = ee.FeatureCollection('users/user/DVC_for_hab')

def getHist(feature):
    hist = img.reduceRegion(reducer=ee.Reducer.frequencyHistogram(), geometry=feature.geometry())
    return feature.set(hist)

AOI = AOI.map(lambda feature: getHist(feature))
```

## Selecting

| Command | Description |
|---------|-------------|
| `fc.filter(ee.Filter.eq('Field', 'Value'))` | Select by property |
| `fc.filterMetadata('Field', 'Operator', 'Value')` | Select by property. Operators: `'equals'`, `'less_than'`, `'greater_than'`, `'not_equals'`, `'not_less_than'`, `'not_greater_than'`, `'starts_with'`, `'ends_with'`, `'not_starts_with'`, `'not_ends_with'`, `'contains'`, `'not_contains'` |
| `fc1.filterBounds(fc2)` | Select by geometry, features that intersect fc2 |

## Vector to Raster

```python
sheds = ee.FeatureCollection('ft:1IXfrLpTHX4dtdj1LcNXjJADBB-d93rkdJ9acSEWK')

# Version 1
empty = ee.Image().byte().clip(sheds)
sheds_Layer = empty.paint(ee.FeatureCollection(sheds))

# Version 2
sheds_Layer = sheds.reduceToImage(['Area'], ee.Reducer.first())
```
