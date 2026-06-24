# Get Info

Starting GRASS in Python:

```python
>>> import grass.script as grass
```

## Environments

| Command | Description |
|---------|-------------|
| `grass.gisenv()` | Get GRASS environment info as a dictionary |

```
'GISDBASE': 'C:/GRASS/GIS DataBase',
'GRASS_GUI': 'wxpython',
'LOCATION_NAME': 'WGS84',
'MAPSET': 'PERMANENT'
```

| Command | Description |
|---------|-------------|
| `grass.setup.init(gisbase, gisdbase, location, mapset)` | Set system variables to run scripts |

```python
>>> gisbase = os.environ['GISBASE']
>>> gisdbase = 'C:/GRASS/GIS DataBase'
>>> location = 'LAEA'
>>> mapset = 'PERMANENT'
>>> import grass.script.setup as gsetup
>>> gsetup.init(gisbase, gisdbase, location, mapset)
```

## Region

| Command | Description |
|---------|-------------|
| `grass.region()` | Dictionary of region definition |

```
'cells': Number of cells
'rows': Rows
'cols': Columns
'nsres': Y pixel resolution
'ewres': X pixel resolution
'w': X min
's': Y min
'e': X max
'n': Y max
```

## List of Layers

| Command | Description | Output |
|---------|-------------|--------|
| `grass.list_strings({'rast','vect'})` | List of elements as strings | `>>> ['myrast@PERMANENT']` |
| `grass.list_grouped({'rast','vect'})` | List grouped by mapsets as a dictionary | `>>> {'PERMANENT': ['myrast']}` |
| `grass.list_grouped({'rast','vect'})['MAPSET']` | List of elements as strings in the mapset | `>>> ['myrast']` |
| `grass.mlist({'rast','vect'})` | List of elements as strings in all mapsets | `>>> ['myrast']` |
