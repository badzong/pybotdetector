#!/usr/bin/env python

from distutils.core import setup

setup(name='botdetector',
      version='0.1',
      description='Reliable detection of decent spiders e.g. googlebot, bingbot, ..',
      author='Factor AG',
      author_email='manuel@factor.ch',
      url='https://github.com/FactorAG/pybotdetector',
      packages=['botdetector',],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
     )
