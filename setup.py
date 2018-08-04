from setuptools import setup

setup(
    name='dotrc',
    version='0.1dev',
    packages=['dotrc'],
    package_dir={'': 'src'},
    license='MIT',
    install_requires=['PyYAML','simplejson']
)
