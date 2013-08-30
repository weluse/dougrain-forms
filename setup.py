#!/usr/bin/env python

# Support setuptools or distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _xfile(filename, locals):
    with open(filename) as f:
        code = compile(f.read(), filename, 'exec')
        exec(code, {}, locals)


def get_version():
    # Version info -- read without importing
    _locals = {}
    _xfile('dougrain_forms/_version.py', _locals)
    return _locals['__version__']

setup(
    name='dougrain-forms',
    version=get_version(),
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
        'dougrain==0.5.1'
    ],
    license='BSD',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
