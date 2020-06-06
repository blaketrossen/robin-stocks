from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='robin-stocks-blaketrossen',
      version='1.0.0.7',
      description='A Python wrapper around the Robinhood API',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/blaketrossen/robin-stocks.git',
      author='Josh Fernandes and Blake Trossen',
      keywords=['robinhood','robin stocks','finance app','stocks','options','trading','investing'],
      license='MIT',
      python_requires='>=3',
      packages=find_packages(),
      requires=['requests'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
