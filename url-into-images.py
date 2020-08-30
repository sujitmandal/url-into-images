__author__ = 'Sujit Mandal'
#Date : 30-08-2020
import pandas as pd 
import urllib.request

'''
# Author : Sujit Mandal
Github : https://github.com/sujitmandal
My Package : https://pypi.org/project/images-into-array/
My Package : https://pypi.org/project/scrape-search-engine/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
'''

URL_PATH = ('') # csv file where image URL contain
IMAGE_PATH = ('') # Download image path

def url_jpg(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    IMAGE_PATH = IMAGE_PATH

    def jpg(number, url, imagePath):
        fileName = ('image-{}.jpg'.format(number))
        imagePath = ('{}{}'.format(imagePath, fileName))
        urllib.request.urlretrieve(url, imagePath)
        print('{} saved.'.format(fileName))

    for number, url in enumerate(URLS.values):
        jpg(number, url[0], IMAGE_PATH)

def url_jpeg(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    IMAGE_PATH = IMAGE_PATH

    def jpeg(number, url, imagePath):
        fileName = ('image-{}.jpeg'.format(number))
        imagePath = ('{}{}'.format(imagePath, fileName))
        urllib.request.urlretrieve(url, imagePath)
        print('{} saved.'.format(fileName))

    for number, url in enumerate(URLS.values):
        jpeg(number, url[0], IMAGE_PATH)

def url_png(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    IMAGE_PATH = IMAGE_PATH

    def png(number, url, imagePath):
        fileName = ('image-{}.png'.format(number))
        imagePath = ('{}{}'.format(imagePath, fileName))
        urllib.request.urlretrieve(url, imagePath)
        print('{} saved.'.format(fileName))

    for number, url in enumerate(URLS.values):
        png(number, url[0], IMAGE_PATH)

def url_bmp(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    IMAGE_PATH = IMAGE_PATH

    def bmp(number, url, imagePath):
        fileName = ('image-{}.bmp'.format(number))
        imagePath = ('{}{}'.format(imagePath, fileName))
        urllib.request.urlretrieve(url, imagePath)
        print('{} saved.'.format(fileName))

    for number, url in enumerate(URLS.values):
        bmp(number, url[0], IMAGE_PATH)

def url_gif(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    IMAGE_PATH = IMAGE_PATH

    def gif(number, url, imagePath):
        fileName = ('image-{}.gif'.format(number))
        imagePath = ('{}{}'.format(imagePath, fileName))
        urllib.request.urlretrieve(url, imagePath)
        print('{} saved.'.format(fileName))

    for number, url in enumerate(URLS.values):
        gif(number, url[0], IMAGE_PATH)


if __name__ == '__main__':
    url_jpg(URL_PATH, IMAGE_PATH)
    url_jpeg(URL_PATH, IMAGE_PATH)
    url_png(URL_PATH, IMAGE_PATH)
    url_bmp(URL_PATH, IMAGE_PATH)
    url_gif(URL_PATH, IMAGE_PATH)
