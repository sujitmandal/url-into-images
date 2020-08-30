## Package Installation : 
```
pip install url-into-images
```

[Package Link](https://pypi.org/project/url-into-images/)

## Scrape Search Engine :
provide image download link through csv file and it will download all the images. also you can chose different extension.
```
 • jpg

 • jpeg

 • png

 • bmp

 • gif
```
## How to import the module:
```
URL_PATH = ('') # csv file where image URL contain
IMAGE_PATH = ('') # Download image path
```
## Download JPG
```
from url_into_images.url_into_images import url_jpg

url_jpg(URL_PATH, IMAGE_PATH)
```
## Download JPEG
```
from url_into_images.url_into_images import url_jpeg
url_jpeg(URL_PATH, IMAGE_PATH)
```
## Download PNG
```
from url_into_images.url_into_images import url_png
url_png(URL_PATH, IMAGE_PATH)
```
## Download BMP
```
from url_into_images.url_into_images import url_bmp
url_bmp(URL_PATH, IMAGE_PATH)
```
## Download GIF
```
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
