#!/usr/bin/env python

# Support setuptools or distutils
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


import dougrain_forms


setup(
    name='dougrain-forms',
    version=dougrain_forms.__version__,
    description='Unofficial hypermedia form extension for dougrain.',
    long_description=open('README.rst').read(),
    author='Pascal Hartig',
    author_email='phartig@weluse.de',
    url='https://github.com/weluse/dougrain-forms',
    data_files=[
        'README.rst'
    ],
    packages=[
        'dougrain_forms'
    ],
    install_requires=[
        'dougrain==0.4'
    ],
    license='BSD',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
