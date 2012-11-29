from setuptools import setup, find_packages
from distutils.core import Extension

desc = 'Tiny MapReduce for tiny data'


setup(
    name='mattreduce',
    version='0.1pre1',
    description=desc,
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2'
    ],
    packages=find_packages(),
)
