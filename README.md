[![Build Status](https://travis-ci.org/sujitmandal/url-into-images.svg?branch=master)](https://travis-ci.org/sujitmandal/url-into-images) [![GitHub license](https://img.shields.io/github/license/sujitmandal/url-into-images)](https://github.com/sujitmandal/url-into-images/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/url-into-images) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/url-into-images) ![PyPI](https://img.shields.io/pypi/v/url-into-images) ![Conda Version](https://img.shields.io/conda/vn/conda-forge/url-into-images.svg) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/url-into-images/badges/version.svg)](https://anaconda.org/conda-forge/url-into-images) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/url-into-images/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/url-into-images/badges/platforms.svg)](https://anaconda.org/conda-forge/url-into-images) [![Conda Recipe](https://img.shields.io/badge/recipe-url--into--images-green.svg)](https://anaconda.org/conda-forge/url-into-images) ![](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/url-into-images-feedstock?branchName=main)

[![Downloads](https://pepy.tech/badge/url-into-images)](https://pepy.tech/project/url-into-images)

Automatically  Download Multiple Images.

## Package Installation : 
```
pip install url-into-images
```

```
conda install -c conda-forge url-into-images
```
[Conda Package Link](https://anaconda.org/conda-forge/url-into-images)


[scrape-search-engine-feedstock](https://github.com/conda-forge/url-into-images-feedstock)



## Url Into Images :
provide image download link through csv file and it will download all the images. also you can chose different extension.
```
 • jpg

 • jpeg

 • png

 • bmp

 • gif
```
## How to import the module:
```python
URL_PATH = ('') # csv file where image URL contain

IMAGE_PATH = ('') # Download image path
```
## Download JPG
```python
from url_into_images.url_into_images import url_jpg

url_jpg(URL_PATH, IMAGE_PATH)
```
## Download JPEG
```python
from url_into_images.url_into_images import url_jpeg

url_jpeg(URL_PATH, IMAGE_PATH)
```
## Download PNG
```python
from url_into_images.url_into_images import url_png

url_png(URL_PATH, IMAGE_PATH)
```
## Download BMP
```python
from url_into_images.url_into_images import url_bmp

url_bmp(URL_PATH, IMAGE_PATH)
```
## Download GIF
```python
from url_into_images.url_into_images import url_gif

url_gif(URL_PATH, IMAGE_PATH)
```

## Required package’s:
```
• pip install pandas
```
## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)
