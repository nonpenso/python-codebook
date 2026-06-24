# Reprojecting

## Reprojecting a GeoTIFF

```python
import rasterio
from rasterio.warp import reproject, Resampling

# Input GeoTIFF
# WGS84 = EPSG 4326
# Extent: left=-31.5, bottom=26.5, right=35.0, top=71.0
# Pixel size: 0.5 degree

in_tiff = r'C:\temp\IN.tif'
dataset = rasterio.open(in_tiff)
profile = dataset.meta.copy()

# Output GeoTIFF
# LAEA = EPSG 3035
# Extent: left=900000.0, bottom=900000.0, right=7400000.0, top=5500000.0
# Pixel size: 25000 m

out_tiff = r'C:\temp\OUT.tif'
dst_crs = 'EPSG:3035'
dst_pix_size = 25000.0
dst_bounds = (900000.0, 900000.0, 7400000.0, 5500000.0)  # left, bottom, right, top
dst_width = int((dst_bounds[2] - dst_bounds[0]) / dst_pix_size)
dst_height = int((dst_bounds[3] - dst_bounds[1]) / dst_pix_size)
dst_trans = rasterio.Affine(dst_pix_size, 0.0, dst_bounds[0],
                            0.0, -dst_pix_size, dst_bounds[3])

profile.update({
    'crs': dst_crs,
    'transform': dst_trans,
    'width': dst_width,
    'height': dst_height
})

with rasterio.open(out_tiff, 'w', **profile) as outset:
    reproject(
        source=rasterio.band(dataset, 1),
        destination=rasterio.band(outset, 1),
        src_transform=dataset.transform,
        src_crs=dataset.crs,
        dst_transform=dst_trans,
        dst_crs=dst_crs,
        resampling=Resampling.nearest
    )
```
