# py_framels

support [![python](https://img.shields.io/badge/Python-3.8,3.9,3.10,3.11,3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

![fast](images/t7ns9qtb5gh81.jpg)

## Description

py_framels is a python binding to use [framels](https://github.com/doubleailes/fls) rust lib in python

For documentation about framels: [doc guide](https://doubleailes.github.io/fls/)

The library only support 3 functions at the time.

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

The function provide a packing of the frame sequences using framels format.

```python
import py_framels

print(py_framels.py_basic_listing(["toto.0001.tif","toto.0002.tif"], False))
```

Should return

`['toto.****.tif@1-2']`

#### py_parse_dir

The function list all the files and folders in specific directory and pack them

```python
import py_framels

py_framels.py_parse_dir("./fls/samples/big", False)
```

Return `['RenderPass_Beauty_1_*****.exr@0-96', 'RenderPass_DiffuseKey_1_*****.exr@0-96', 'RenderPass_Diffuse_1_*****.exr@0-96', 'RenderPass_Id_1_*****.exr@0-96', 'RenderPass_IndDiffuse_1_*****.exr@0-96', 'RenderPass_Ncam_1_*****.exr@0-41,43-96', 'RenderPass_Ncam_1_00042.exr.bkp', 'RenderPass_Occlusion_1_*****.exr@0-73,75-96', 'RenderPass_Occlusion_1_***.exr@74', 'RenderPass_Pcam_1_*****.exr@0-96', 'RenderPass_Reflection_1_*****.exr@0-96', 'RenderPass_SpecularRim_1_*****.exr@0-96', 'RenderPass_Specular_1_*****.exr@0-96']`

#### py_recursive_dir

```python
import py_framels

py_framels.py_recursive_dir("./fls/samples", False)

```

Return `['RenderPass_Beauty_1_*****.exr@0-96', 'RenderPass_DiffuseKey_1_*****.exr@0-96', 'RenderPass_Diffuse_1_*****.exr@0-96', 'RenderPass_Id_1_*****.exr@0-96', 'RenderPass_IndDiffuse_1_*****.exr@0-96', 'RenderPass_Ncam_1_*****.exr@0-41,43-96', 'RenderPass_Ncam_1_00042.exr.bkp', 'RenderPass_Occlusion_1_*****.exr@0-73,75-96', 'RenderPass_Occlusion_1_***.exr@74', 'RenderPass_Pcam_1_*****.exr@0-96', 'RenderPass_Reflection_1_*****.exr@0-96', 'RenderPass_SpecularRim_1_*****.exr@0-96', 'RenderPass_Specular_1_*****.exr@0-96', 'aaa.***.tif@1-5', 'big', 'foo_bar.exr', 'mega', 'response_1689510067951.json', 'samples', 'small']`

## Benchmark

This is benchmarks of the python binding py-framels vs pyseq at diffirent level of inputs.
Time is always in seconds.

![benchmark](benchmark/bench_100.png)

|   paths    |      1 |      2 |      5 |      10|      50|        |
|------------|--------|--------|--------|--------|--------|--------|
| py_framels |0.004966|0.000201|0.000125|0.000203|0.000999|0.001802|
|    pyseq   |4.4e-05 |0.000172|0.000291|0.000645|0.002817|0.005725|

![benchmark](benchmark/bench_25000.png)

|   paths    |   100  |   1000 |20000   |  25000 |
|------------|--------|--------|--------|--------|
| py_framels |0.002173|0.015975|0.359272|0.420266|
|    pyseq   |0.005592|0.060121|2.632283|3.918997|

Note: there is an acceleration at the level of 20000 paths, this is due to the fact
framels is multi-threaded at a threshold of 100000 paths and the bench simulate
5 aovs ( 5 x 20 000 = 100 000 paths ).
