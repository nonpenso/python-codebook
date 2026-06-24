# Google Earth Engine (GEE) with ArcGIS

Setup method for using Google Earth Engine with ArcGIS Python.

## Prerequisites

### Microsoft Visual C++

Install Microsoft Visual C++ Compiler for Python.

Download: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### Python Modules

On the command prompt:

```
SET HTTPS_PROXY=http://login:password@proxy.example.com:8012
SET HTTP_PROXY=http://login:password@proxy.example.com:8012

pip install google-api-python-client
pip install pycrypto
pip install oauth2client
pip install earthengine-api
```

### Google Authentication

On the command prompt:

```
earthengine authenticate
```

## Script

```python
import ee
import os

os.environ['http_proxy'] = "http://login:password@proxy.example.com:8012"
os.environ['https_proxy'] = "http://login:password@proxy.example.com:8012"

ee.Initialize()
```

:::{note}
For newer versions of the Earth Engine API, use `ee.Authenticate()` followed by `ee.Initialize(project='your-project-id')` instead of the older authentication method. The proxy settings are only needed in restricted network environments.
:::
