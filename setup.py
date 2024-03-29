#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='simpleai',
    version='0.8',
    description=u'An implementation of AI algorithms based on aima-python',
    long_description=open('README.rst').read(),
    author=u'Manish Marahatta',
    author_email='me@manishmarahatta.com.np',
    url='http://github.com/manishmarahatta/AI-NP',
    packages=['simpleai', 'simpleai.search', 'simpleai.machine_learning'],
    package_data={'simpleai.search': ['web_viewer_resources/*.*']},
    license='LICENSE.txt',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
