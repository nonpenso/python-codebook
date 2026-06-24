# Set Variables

In order to use GRASS GIS functionality via Python from outside the GRASS environment, some environment variables must be set.

## MS Windows

```
GISBASE= C:\Program Files (x86)\GRASS GIS 6.4.3
GISRC= C:\Users\<User>\AppData\Roaming\GRASS6\grassrc6
LD_LIBRARY_PATH= C:\Program Files (x86)\GRASS GIS 6.4.3\lib
PATH= C:\Program Files (x86)\GRASS GIS 6.4.3\etc;C:\Program Files (x86)\GRASS GIS 6.4.3\etc\python;C:\Program Files (x86)\GRASS GIS 6.4.3\lib;C:\Program Files (x86)\GRASS GIS 6.4.3\bin;C:\Program Files (x86)\GRASS GIS 6.4.3\extralib;C:\Program Files (x86)\GRASS GIS 6.4.3\msys\bin
GRASS_SH= C:\Program Files (x86)\GRASS GIS 6.4.3\msys\bin\sh.exe
```

The `GISRC` variable sets the GRASS Mapset and Location. It is a generic file (no extension) with the following settings:

```
GISDBASE: E:\Documents\GIS DataBase
LOCATION_NAME: MYLOCATION
MAPSET: MYMAPSET
GRASS_GUI: wxpython
```

:::{note}
Remember to update the Location and Mapset in this file when starting a new project.
:::

## Linux

### Ubuntu

```bash
export GISBASE="/usr/local/grass-6.4.4svn/"
export PATH="$PATH:$GISBASE/bin:$GISBASE/scripts"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$GISBASE/lib"
# For parallel session management, use process ID (PID) as lock file number:
export GIS_LOCK=$$
# Path to GRASS settings file
export GISRC="$HOME/.grassrc6"
export PYTHONPATH="$PYTHONPATH:$GISBASE/etc/python"
```

### CentOS / Red Hat

```bash
export GISBASE="/usr/lib64/grass-6.4.2/"
export PATH="$PATH:$GISBASE/bin:$GISBASE/scripts"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64"
# For parallel session management, use process ID (PID) as lock file number:
export GIS_LOCK=$$
# Path to GRASS settings file
export GISRC="$HOME/.grassrc6"
export PYTHONPATH="$PYTHONPATH:$GISBASE/etc/python"
```
