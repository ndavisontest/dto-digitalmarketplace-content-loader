import re
import ast
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

setup(
    name='dto-digitalmarketplace-content-loader',
    version='1.1.1',
    url='https://github.com/AusDTO/dto-digitalmarketplace-content-loader',
    license='MIT',
    author='GDS Developers',
    description='Digital Marketplace Content Loader',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'inflection',
        'PyYAML',
        'Werkzeug',
        'six'
    ]
)
