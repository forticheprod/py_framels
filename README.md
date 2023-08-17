<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="198.0" height="20"><linearGradient id="smooth" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="round"><rect width="198.0" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#round)"><rect width="65.5" height="20" fill="#555"/><rect x="65.5" width="132.5" height="20" fill="#007ec6"/><rect width="198.0" height="20" fill="url(#smooth)"/></g><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110"><image x="5" y="3" width="14" height="14" xlink:href="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/python.svg"/><text x="422.5" y="150" fill="#010101" fill-opacity=".3" transform="scale(0.1)" textLength="385.0" lengthAdjust="spacing">python</text><text x="422.5" y="140" transform="scale(0.1)" textLength="385.0" lengthAdjust="spacing">python</text><text x="1307.5" y="150" fill="#010101" fill-opacity=".3" transform="scale(0.1)" textLength="1225.0" lengthAdjust="spacing">3.8,3.9,3.10,3.11,3.12</text><text x="1307.5" y="140" transform="scale(0.1)" textLength="1225.0" lengthAdjust="spacing">3.8,3.9,3.10,3.11,3.12</text><a xlink:href=""><rect width="65.5" height="20" fill="rgba(0,0,0,0)"/></a><a xlink:href="https://www.python.org/"><rect x="65.5" width="132.5" height="20" fill="rgba(0,0,0,0)"/></a></g></svg>

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
