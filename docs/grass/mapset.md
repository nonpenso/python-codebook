# Work with Mapset

## Create

```python
import grass.script as grass
import os

gisbase = os.environ['GISBASE']
gisdbase = 'C:/GRASS/GIS DataBase'
location = 'LAEA'
mapset = 'MYMAPSET'

import grass.script.setup as gsetup
gsetup.init(gisbase, gisdbase, location, mapset)

grass.run_command('g.mapset', flags='c', mapset='NEWMAPSET', location=location, gisdb=gisdbase)
```

## Change

```python
gsetup.init(gisbase, gisdbase, location, 'NEWMAPSET')
```

## Commands

| Operation | Command |
|-----------|---------|
| Get raster list | `raslist = grass.list_grouped('rast')['PERMANENT']` |
| Copy raster | `grass.run_command('g.copy', rast='Elev@MYMAPSET,Elev')` |
| Rename raster | `grass.run_command('g.rename', rast='oldrast,newrast')` |
| Delete raster | `grass.run_command('g.remove', rast='soils,slope,temp')` |
