import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.getcwd(), filename)).read()

setup(
    name='dotrc',
    description='Simple .rc file loading for your Python projects',
    author='Paul Holden',
    author_email='pholden@stria.com',
    version='0.1dev1',
    packages=['dotrc'],
    package_dir={'': 'src'},
    url='https://pypi.org/project/dotrc/',
    license='MIT',
    install_requires=['PyYAML','simplejson'],
    long_description=read('README.md')
)
