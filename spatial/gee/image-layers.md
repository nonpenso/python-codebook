# Image Layers

## Image Functions

| Command | Description |
|---------|-------------|
| `img.bandNames().getInfo()` | List of band names |
| `img.select(['bandname'])` | Select a band |
| `img1.addBands(img2.rename('img2'))` | Add new band to img1 and rename it |
| `ee.ImageCollection([img1, img2]).mosaic()` | Merge 2 images |
| `img.clip(fc)` | Clip image with the feature collection |
| `img.reduceRegion(reducer=<Reducer>, geometry=fc, scale=30, maxPixels=5e9)` | Apply a reducer to all the pixels in a specific region with a feature collection. Reducers: `ee.Reducer.sum()`, `ee.Reducer.count()`, `ee.Reducer.max()`, `ee.Reducer.mean()`, ... |
| `ee.Image.pixelArea()` | Create an image with area value in every pixel |

## Algebraic Functions

| Command | Description |
|---------|-------------|
| `add()`, `subtract()`, `multiply()`, `divide()`, `mod()`, `exp()` | Arithmetic: `+` `-` `*` `/` `%` `**` |
| `eq()`, `gt()`, `gte()`, `lt()`, `lte()`, `neq()` | Comparison: `==` `!=` `<` `>` `<=` `>=` |
| `And()`, `Or()`, `Not()` | Logical operators |
| `img1.where(img2, -1)` | Mask img1 where img2 has value -1 |

## Image Masking

| Command | Description |
|---------|-------------|
| `img1.selfMask()` | Mask all 0 values |
| `img1.unmask(0)` | Set 0 for masked values |
| `img1.updateMask(img2)` | Mask img1 with img2, keeping values of img1 |
