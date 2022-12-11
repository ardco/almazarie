# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in almuzare/__init__.py
from almuzare import __version__ as version

setup(
	name='almuzare',
	version=version,
	description='edit the method of calculating the Landed Cost Voucher by adding the CBM method',
	author='Hadeel Milad',
	author_email='hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
