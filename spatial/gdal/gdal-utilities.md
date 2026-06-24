# GDAL Utilities

With GDAL Python libraries, several utilities are available. The complete list is at:
[https://gdal.org/programs/](https://gdal.org/programs/)

Python can call them as command-line tools using the `subprocess` module. To run a utility, it is necessary to provide the full path to the executable. The `shell` option allows you to capture the output string from the command.

```python
>>> import subprocess
>>> cmd = r"C:\Python27\Lib\site-packages\osgeo\gdalinfo.exe raster.tif"
>>> shell = subprocess.check_output(cmd, shell=True)
>>> print(shell)
```

## CMD Examples

### Gdalwarp

Website: [https://gdal.org/programs/gdalwarp.html](https://gdal.org/programs/gdalwarp.html)

```
C:\Python27\ArcGIS10.3\Lib\site-packages\osgeo\gdalwarp.exe
-t_srs "+proj=laea +lat_0=52 +lon_0=10 +x_0=4321000 +y_0=3210000 +ellps=GRS80 +units=m +datum=ETRS89 +no_defs"
-r "bilinear"
-te 2639000 1424000 7377000 5965000
-tr 1000 1000
-wo "CUTLINE_ALL_TOUCHED=TRUE"
C:\temp\inras.tif
C:\temp\outras.tif
```
