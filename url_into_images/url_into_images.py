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
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0]
        url.append(links)

    for j in range(len(url)):
        fileName = ('image{}.jpg'.format(j))
        imagePath = ('{}{}'.format(IMAGE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))

def url_jpeg(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0]
        url.append(links)

    for j in range(len(url)):
        fileName = ('image{}.jpeg'.format(j))
        imagePath = ('{}{}'.format(IMAGE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))

def url_png(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0]
        url.append(links)

    for j in range(len(url)):
        fileName = ('image{}.png'.format(j))
        imagePath = ('{}{}'.format(IMAGE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))


def url_bmp(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0]
        url.append(links)

    for j in range(len(url)):
        fileName = ('image{}.bmp'.format(j))
        imagePath = ('{}{}'.format(IMAGE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))


def url_gif(URL_PATH, IMAGE_PATH):
    URLS = pd.read_csv(URL_PATH)
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0]
        url.append(links)

    for j in range(len(url)):
        fileName = ('image{}.gif'.format(j))
        imagePath = ('{}{}'.format(IMAGE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))


if __name__ == '__main__':
    url_jpg(URL_PATH, IMAGE_PATH)
    url_jpeg(URL_PATH, IMAGE_PATH)
    url_png(URL_PATH, IMAGE_PATH)
    url_bmp(URL_PATH, IMAGE_PATH)
    url_gif(URL_PATH, IMAGE_PATH)