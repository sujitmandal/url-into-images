## Convert-Images-Into-Array:
[![Build Status](https://travis-ci.org/sujitmandal/images-into-array.svg?branch=master)](https://travis-ci.org/sujitmandal/images-into-array) [![GitHub license](https://img.shields.io/github/license/sujitmandal/images-into-array)](https://github.com/sujitmandal/images-into-array/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/images-into-array) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/images-into-array) ![PyPI](https://img.shields.io/pypi/v/images-into-array)

[![Downloads](https://pepy.tech/badge/images-into-array)](https://pepy.tech/project/images-into-array) 

Convert Multiple Images into a Array and Different Color Spaces into a Array.

## Package Installation  : 
```
pip install images-into-array
```

[Package Link](https://pypi.org/project/images-into-array/)

## Convert-Images-Into-Array:
Convert Multiple Images into a Array and Different Color Spaces into a Array.This package fuction requres three argument one is path of the images folder and other is image_height and image_width.

OpenCV Document :
-----------------
[OpenCV Document](https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html)

## How to import the module:
```python
images_path = ('')

image_height = Enter The Image Size [32, 64, 128]

image_width = Enter The Image Size [32, 64, 128]
```
## NORMAL :
```python
from images_into_array.images_into_array import images

array = images(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ GRAY :
```python
from images_into_array.images_into_array import rgb_gray

gray = rgb_gray(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ CIE L*a*b* :
```python
from images_into_array.images_into_array import rgb_lab

lav = rgb_lab(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ HLS :
```python
from images_into_array.images_into_array import rgb_hls

hls = rgb_hls(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ CIE L*u*v* :
```python
from images_into_array.images_into_array import rgb_luv

luv = rgb_luv(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ HSV :
```python
from images_into_array.images_into_array import rgb_hsv

hsv = rgb_hsv(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ YCrCb JPEG (or YCC) :
```python
from images_into_array.images_into_array import rgb_ycrcb

ycrcb = rgb_ycrcb(images_path, image_height, image_width)

print(array.shape)
```

## Required package’s:
```
• conda install -c conda-forge opencv=4.2.0

• pip install shuffle

• pip install numpy

• pip install tqdm
```
## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)