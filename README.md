# py_framels

support [![python](https://img.shields.io/badge/Python-3.8,3.9,3.10,3.11,3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

![fast](https://camo.githubusercontent.com/e8a50ee9600d66095bf0046f06e65ef8fe0675a40122db2a801d1f66e595add6/68747470733a2f2f692e726564642e69742f74376e733971746235676838312e6a7067)

## Description

py_framels is a python binding to use [framels](https://github.com/doubleailes/fls) rust lib in python

For documentation about framels: [doc guide](https://doubleailes.github.io/fls/)

The module only support 3 function at the time.

## Install

`pip install py-framels`

## Usage

### Exemple

```python
import py_framels

print(py_framels.py_basic_listing(["toto.0001.tif","toto.0002.tif"]))
```

Should return

`['toto.****.tif@1-2']`

### Functions

#### py_basic_listing

The function pack provide a packing of the frame sequences using framls format.

```python
import py_framels

print(py_framels.py_basic_listing(["toto.0001.tif","toto.0002.tif"]))
```

Should return

`['toto.****.tif@1-2']`

#### py_parse_dir

The function list all the files and folders in specific directory and pack them

```python
import py_framels

py_framels.py_parse_dir("./fls/samples/big")
```

Return `['RenderPass_Beauty_1_*****.exr@0-96', 'RenderPass_DiffuseKey_1_*****.exr@0-96', 'RenderPass_Diffuse_1_*****.exr@0-96', 'RenderPass_Id_1_*****.exr@0-96', 'RenderPass_IndDiffuse_1_*****.exr@0-96', 'RenderPass_Ncam_1_*****.exr@0-41,43-96', 'RenderPass_Ncam_1_00042.exr.bkp', 'RenderPass_Occlusion_1_*****.exr@0-73,75-96', 'RenderPass_Occlusion_1_***.exr@74', 'RenderPass_Pcam_1_*****.exr@0-96', 'RenderPass_Reflection_1_*****.exr@0-96', 'RenderPass_SpecularRim_1_*****.exr@0-96', 'RenderPass_Specular_1_*****.exr@0-96']`

#### py_recursive_dir

```python
import py_framels

py_framels.py_recursive_dir("./fls/samples")

```

Return `['RenderPass_Beauty_1_*****.exr@0-96', 'RenderPass_DiffuseKey_1_*****.exr@0-96', 'RenderPass_Diffuse_1_*****.exr@0-96', 'RenderPass_Id_1_*****.exr@0-96', 'RenderPass_IndDiffuse_1_*****.exr@0-96', 'RenderPass_Ncam_1_*****.exr@0-41,43-96', 'RenderPass_Ncam_1_00042.exr.bkp', 'RenderPass_Occlusion_1_*****.exr@0-73,75-96', 'RenderPass_Occlusion_1_***.exr@74', 'RenderPass_Pcam_1_*****.exr@0-96', 'RenderPass_Reflection_1_*****.exr@0-96', 'RenderPass_SpecularRim_1_*****.exr@0-96', 'RenderPass_Specular_1_*****.exr@0-96', 'aaa.***.tif@1-5', 'big', 'foo_bar.exr', 'mega', 'response_1689510067951.json', 'samples', 'small']`
