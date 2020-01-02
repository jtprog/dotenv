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
      packages=['ndenv'],
      setup_requires=['distribute'],
      scripts=['scripts/ndenv']
      )

