from setuptools import setup, find_packages
from setuptools.command.install import install
from os import path
import subprocess

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    # $ pip install printmaking-dl
    name='printmaking_dl',
    version='0.0.1',
    description='A python library for layering prints',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/estorrs/printmaking-dl',
    author='Erik Storrs',
    author_email='estorrs@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='printmaking deep learning',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'torch',
    ],
    include_package_data=True,
)
