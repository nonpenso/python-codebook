# Matplotlib

Matplotlib is a 2D plotting library for creating static, animated, and interactive visualisations in Python.

```python
import matplotlib.pyplot as plt
import numpy as np
```

## Basic Usage

### Single Chart

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple Plot")
plt.show()
```

### Multiple Charts (Subplots)

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y)
axes[0].set_title("Plot 1")

axes[1].bar(x, y)
axes[1].set_title("Plot 2")

plt.tight_layout()
plt.show()
```

## Chart Types

### Line and Marker

```python
plt.plot(x, y, color="blue", linestyle="--", marker="o", label="Data")
plt.legend()
plt.show()
```

### Horizontal and Vertical Lines

```python
plt.plot(x, y)
plt.axhline(y=5, color="red", linestyle="--", label="Horizontal")
plt.axvline(x=3, color="green", linestyle=":", label="Vertical")
plt.legend()
plt.show()
```

### Bar Chart

```python
categories = ["A", "B", "C", "D"]
values = [10, 25, 15, 30]

plt.bar(categories, values, color="steelblue")
plt.ylabel("Count")
plt.title("Bar Chart")
plt.show()
```

### Scatter Plot

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.rand(50) * 200

plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap="viridis")
plt.colorbar()
plt.title("Scatter Plot")
plt.show()
```

### Box Plot

```python
data = [np.random.randn(100) for _ in range(4)]
plt.boxplot(data, labels=["A", "B", "C", "D"])
plt.title("Box Plot")
plt.show()
```

### Error Bar

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
errors = [0.5, 0.3, 0.8, 0.4, 0.6]

plt.errorbar(x, y, yerr=errors, fmt="o-", capsize=4)
plt.title("Error Bars")
plt.show()
```

### Histogram

```python
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor="black", alpha=0.7)
plt.title("Histogram")
plt.show()
```

### 2D Histogram

```python
x = np.random.randn(10000)
y = np.random.randn(10000)

plt.hist2d(x, y, bins=50, cmap="Blues")
plt.colorbar()
plt.title("2D Histogram")
plt.show()
```

### Pie Chart

```python
labels = ["Python", "Java", "C++", "Other"]
sizes = [45, 25, 15, 15]
explode = (0.05, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
```

## Colours

### Basic Colour Letters

| Letter | Colour |
|--------|--------|
| `b` | Blue |
| `g` | Green |
| `r` | Red |
| `c` | Cyan |
| `m` | Magenta |
| `y` | Yellow |
| `k` | Black |
| `w` | White |

### Named Colours and Hex

You can use any [named CSS colour](https://matplotlib.org/stable/gallery/color/named_colors.html) or hex codes:

```python
plt.plot(x, y, color="steelblue")
plt.plot(x, y, color="#FF5733")
```

## Colormaps

### Discrete Classes with ListedColormap

```python
from matplotlib.colors import ListedColormap

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]
cmap = ListedColormap(colors)

data = np.random.randint(0, 4, (10, 10))
plt.imshow(data, cmap=cmap)
plt.colorbar(ticks=[0, 1, 2, 3])
plt.show()
```

### Trim Extremes with LinearSegmentedColormap

```python
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm

# Get a subsection of a colormap (trim 20% from each end)
original = cm.get_cmap("RdYlBu")
colors = original(np.linspace(0.2, 0.8, 256))
trimmed_cmap = LinearSegmentedColormap.from_list("trimmed", colors)

data = np.random.randn(20, 20)
plt.imshow(data, cmap=trimmed_cmap)
plt.colorbar()
plt.show()
```

## Chart Settings

### Axis Limits and Ticks

```python
plt.plot(x, y)
plt.xlim(0, 6)
plt.ylim(0, 12)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks(range(0, 13, 2))
plt.show()
```

### Axis Labels and Title

```python
plt.plot(x, y)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Distance (m)", fontsize=12)
plt.title("Motion", fontsize=14)
plt.show()
```

### Second Y Axis

```python
fig, ax1 = plt.subplots()

ax1.plot(x, y, "b-")
ax1.set_ylabel("Primary Y", color="blue")

ax2 = ax1.twinx()
ax2.plot(x, [v * 0.5 for v in y], "r-")
ax2.set_ylabel("Secondary Y", color="red")

plt.show()
```

### Grid

```python
plt.plot(x, y)
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

### Frame and Spines

```python
fig, ax = plt.subplots()
ax.plot(x, y)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()
```

### Text, Title, and Annotations

```python
plt.plot(x, y)
plt.title("Chart Title")
plt.text(2, 8, "Annotation here", fontsize=10)
plt.annotate("Peak", xy=(5, 10), xytext=(4, 9),
             arrowprops=dict(arrowstyle="->"))
plt.show()
```

### Background Colour

```python
fig, ax = plt.subplots()
fig.patch.set_facecolor("white")
ax.set_facecolor("#f0f0f0")
ax.plot(x, y)
plt.show()
```

## Iterating Over Subplots

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for i, ax in enumerate(axes.flatten()):
    ax.plot(np.random.randn(20))
    ax.set_title(f"Plot {i + 1}")

plt.tight_layout()
plt.show()
```

## Figure Settings

### Size and Position

```python
fig = plt.figure(figsize=(10, 6), dpi=100)
```

### Spacing Between Subplots

```python
fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.show()
```

### Figure Text

```python
fig, ax = plt.subplots()
ax.plot(x, y)
fig.text(0.5, 0.01, "Figure caption", ha="center", fontsize=10)
plt.show()
```

### Legend

```python
plt.plot(x, y, label="Series A")
plt.plot(x, [v * 0.5 for v in y], label="Series B")
plt.legend(loc="upper left")
plt.show()
```

### Save Figure

```python
plt.plot(x, y)
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.savefig("chart.pdf")
plt.close()
```

## Continuous Functions

### Linear and Quadratic

```python
x = np.linspace(-5, 5, 100)

# Linear: y = 2x + 1
y_linear = 2 * x + 1

# Quadratic: y = x^2 - 3
y_quad = x**2 - 3

plt.plot(x, y_linear, label="y = 2x + 1")
plt.plot(x, y_quad, label="y = x² - 3")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Linear Regression with polyfit

```python
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.0, 14.1])

# Fit a 1st-degree polynomial (line)
coeffs = np.polyfit(x, y, 1)
slope, intercept = coeffs
print(f"y = {slope:.2f}x + {intercept:.2f}")

# Correlation coefficient
r = np.corrcoef(x, y)[0, 1]
print(f"R = {r:.4f}")

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x, np.polyval(coeffs, x), "r-", label=f"Fit (R={r:.3f})")
plt.legend()
plt.show()
```

## Shapes

### Rectangle

```python
import matplotlib.patches as patches

fig, ax = plt.subplots()
rect = patches.Rectangle((1, 1), 3, 2, linewidth=2,
                          edgecolor="blue", facecolor="lightblue")
ax.add_patch(rect)
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)
ax.set_aspect("equal")
plt.show()
```

## Maps with Fiona and Descartes

### Plot Points

```python
import fiona
import matplotlib.pyplot as plt

with fiona.open("points.shp") as src:
    for feature in src:
        geom = feature["geometry"]
        x, y = geom["coordinates"]
        plt.plot(x, y, "ro", markersize=3)

plt.axis("equal")
plt.show()
```

### Plot Polygons

```python
import fiona
import matplotlib.pyplot as plt
from descartes import PolygonPatch

fig, ax = plt.subplots()

with fiona.open("polygons.shp") as src:
    for feature in src:
        geom = feature["geometry"]
        patch = PolygonPatch(geom, facecolor="lightgreen",
                            edgecolor="black", alpha=0.5)
        ax.add_patch(patch)

ax.axis("equal")
ax.autoscale()
plt.show()
```

!!! note "Alternative: Geopandas"
    For simpler map plotting, consider using `geopandas` which wraps Fiona and Matplotlib:
    ```python
    import geopandas as gpd
    gdf = gpd.read_file("polygons.shp")
    gdf.plot()
    ```
