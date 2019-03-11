#!/usr/bin/env python
# encoding=UTF-8
"""Setup module for Dotenv"""


from setuptools import setup

setup(name='dotenv',
      version=__import__('dotenv').__version__,
      description='Handle .env files',
      author='Pedro Burón',
      author_email='pedro@witoi.com',
      url='https://github.com/jtprog/dotenv',
      packages=['dotenv'],
      setup_requires=['distribute'],
      scripts=['scripts/dotenv']
      )
