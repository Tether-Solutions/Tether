'''Package setup file'''
from setuptools import setup, find_packages

setup(
    name='Tether',
    version='1.0.0',
    url='https://github.com/Yuvanesh-ux/Tether',
    description='Providing easy to access crypto information',
    packages=find_packages(),
    install_requires=[
        'black',
        'isort',
        'email',
        'smtp',
        'ssl',
        'time',
        'requests',
        'json',
        'itertools'
    ],
    include_package_data=True
)

