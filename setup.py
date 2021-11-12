from distutils.core import setup
from setuptools import find_packages
setup(name='ib16ipif',
      version='0.1',
      author='DSSS',
      author_email='shreya.r.more@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])