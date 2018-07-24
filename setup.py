#!/usr/bin/env python

from setuptools import setup

setup(name='OpenNMT-py',
      description='A python implementation of OpenNMT',
      version='0.2',

      dependency_links=['https://github.com/pytorch/text/master/tarball'],
      install_requires=['six', 'tqdm', 'torch>=0.4.0', 'torchvision', 'text', 'future'],

      packages=['onmt', 'onmt.encoders', 'onmt.modules', 'onmt.tests',
                'onmt.translate', 'onmt.decoders', 'onmt.inputters',
                'onmt.models', 'onmt.utils'])
