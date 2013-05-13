#!/usr/bin/env python

# Support setuptools or distutils
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


# Version info -- read without importing
_locals = {}
version_module = execfile('dougrain_forms/_version.py', _locals)
version = _locals['__version__']

setup(
    name='dougrain-forms',
    version=version,
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
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
