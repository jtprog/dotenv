#!/usr/bin/env python
# encoding=UTF-8
"""Setup module for NDenv"""


from setuptools import setup

try: # fix nose error
    import multiprocessing
except ImportError:
    pass

setup(name='ndenv',
      version=__import__('ndenv').__version__,
      description='Handle .env files',
      author='Mihael Savin',
      author_email='mail@jtprog.ru',
      url='https://github.com/jtprog/ndenv',
      test_suite='nose.collector',
      packages=setuptools.find_packages(),
      scripts=['scripts/ndenv'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      )

