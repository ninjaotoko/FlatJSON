# -*- coding:utf8 -*-
#
# Copyright (c) 2014 Xavier Lesa <xavierlesa@gmail.com>.
# All rights reserved.
# Distributed under the BSD license, see LICENSE
from setuptools import setup, find_packages
import sys, os

setup(name='flatjson', 
        version='0.1', 
        description="Utilidad para transforma un JSON a un dict de una sola dimensión, para poder usarlo con HStore",
        packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
        include_package_data=True,
        zip_safe=False,
        author='Xavier Lesa',
        author_email='xavierlesa@gmail.com',
        url='http://github.com/ninjaotoko/FlatJSON'
        )
