#!/usr/bin/env python

from setuptools import setup

setup(name='OpenNMT-py',
      description='A python implementation of OpenNMT',
      version='0.2',

      install_requires=['six', 'tqdm', 'torch>=0.4.0', 'torchvision', 'torchtext', 'future'],

      packages=['onmt', 'onmt.encoders', 'onmt.modules', 'onmt.tests',
                'onmt.translate', 'onmt.decoders', 'onmt.inputters',
                'onmt.models', 'onmt.utils'])
