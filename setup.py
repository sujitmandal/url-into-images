__author__ = 'Sujit Mandal'
#Date : 30-08-2020
from setuptools import setup 

def readme():
    with open('README.md') as files:
        README = files.read()

    return(README)

setup(
    name = 'url-into-images',
    version = '0.0.7',
    description = "provide image download link through csv file and it will download all the images. also you can chose different extension.",
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sujitmandal/url-into-images',
    author = 'Sujit Mandal',
    author_email = 'mandals974@gmail.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    packages = ['url_into_images'],
    include_package_data = True,
)