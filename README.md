# Python Codebook

A practical Python code reference for quick lookup and copy/paste, covering language fundamentals, data modules, and geospatial libraries.

## 📖 Documentation

**[https://nonpenso.github.io/python-codebook/](https://nonpenso.github.io/python-codebook/)**

## Contents

- **Python Basics** — variables, types, strings, lists, dictionaries, file I/O, control flow
- **Modules** — NumPy, Pandas, Matplotlib, CSV, NetCDF, datetime, multiprocessing, NetworkX, XML
- **ArcGIS** — arcpy geoprocessing, cursors, mapping, raster operations
- **GRASS** — scripting GRASS GIS from Python
- **GDAL** — raster and vector processing with GDAL/OGR
- **Fiona & Shapely** — vector I/O and geometry operations
- **Google Earth Engine** — GEE Python API for features and images
- **Rasterio** — raster reading, writing, and reprojecting

## Local Preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

## Deployment

The site is automatically built and deployed to GitHub Pages on every push to `main` via GitHub Actions.
