[![python](https://img.shields.io/badge/Python-3.8,3.9,3.10,3.11,3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

# py_framels

## Description

py_framels is an python binding to use [framels](https://github.com/doubleailes/fls) rust lib in python

For documentation about framels: [doc guide](https://doubleailes.github.io/fls/)

## Install

`pip install py-framels`

## Usage

```python
import py_framels

print(py_framels.py_basic_listing(["toto.0001.tif","toto.0002.tif"]))
```

Should return

`['toto.****.tif@1-2']`
