# Working with Geometries

Information about geometries is stored in the "Shape" field of the table. They can be read, modified, and used to create new features.

## Definitions

- **Feature**: A row in the table. It can be a point (array of a single point), a polyline (array of points), or a polygon (array of closed points).
- **Part**: A feature can consist of multiple separate parts (multi-parts). Each part is numbered starting from 0.
- **Interior ring**: When a `None` point is present in the sequence of an array of a polygon, it separates the points defining the polygon from the interior ring (hole).

## Reading Geometries

To access geometries, open the table with a cursor, read the "Shape" field, and get the array of points.

```python
areas = r"C:\myfiles\areas.shp"
with arcpy.da.SearchCursor(areas, ['SHAPE@']) as rows:
    for row in rows:
        # Starting from part 0
        partnum = 0
        for part in row[0]:
            # Print the part number
            print("Part %i:" % partnum)

            # Step through each vertex in the feature
            for pnt in part:
                if pnt:
                    # Print x,y coordinates of current point
                    print(pnt.X, pnt.Y)
                else:
                    # If pnt is None, this represents an interior ring
                    print("Interior Ring:")
            partnum += 1
```

## Writing Geometries

### Points

This example converts a CSV file to a point shapefile. The CSV has three fields: one for ID and two for X and Y coordinates in LAEA projection.

| ID | X | Y |
|----|---|---|
| 1 | 4291249 | 2847834 |
| 2 | 4297449 | 2845327 |
| 3 | 4283408 | 2837739 |

The procedure has two steps:

1. Create an empty point shapefile in LAEA projection
2. Iterate through the CSV to populate the shapefile

Point coordinates are set with the `Point()` object, then written into the "Shape" field.

```python
import arcpy
import fileinput

## 1- Creating the empty shapefile

# Define coordinate system
coordSys = arcpy.SpatialReference()
coordSys.factoryCode = 3035

# Create new empty point shapefile with an "ID" numeric field
arcpy.CreateFeatureclass_management(r"C:\workdir", "sample_points.shp", "POINT", "", "", "", coordSys)
arcpy.AddField_management(r"C:\workdir\sample_points.shp", "OID", "SHORT", "10", "", "")


## 2- Populating the shapefile with iteration
csvfile = r"C:\workdir\samples.csv"

# Open the edit session
cursor = arcpy.da.InsertCursor(r"C:\workdir\sample_points.shp", ['SHAPE@', 'OID'])

# Iterate the CSV file
for line in fileinput.input(csvfile):

    # Don't read the header
    if not fileinput.isfirstline():

        # Convert the string line into a list of strings
        # '1,4291249,2847834\n' --> ['1', '4291249', '2847834']
        data = line.strip().split(',')

        # Create the point object
        pnt = arcpy.Point()
        # Populate the object with coordinates (from string to integer)
        pnt.X = int(data[1])
        pnt.Y = int(data[2])

        # Append the row to shapefile
        cursor.insertRow([pnt, int(data[0])])

fileinput.close()
del cursor
```

## Transformations

### Project Coordinates

```python
import arcpy

x = 4291249
y = 2847834

# Create the point geometry
point_LAEA = arcpy.PointGeometry(arcpy.Point(x, y), arcpy.SpatialReference(3035))

# Project the geometry
point_WGS84 = point_LAEA.projectAs(arcpy.SpatialReference(4326))

# Convert geometry to string -> '48.74309896N 009.59562128E'
point_WGS84_str = point_WGS84.toCoordString('DD')

# From string to float
lon = float(point_WGS84_str.split(' ')[1][:-1])
lat = float(point_WGS84_str.split(' ')[0][:-1])
```
