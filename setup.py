# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from opps import documents


install_requires = ["opps>=0.2"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Opps",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = documents.__description__

setup(
    name='opps-documents',
    namespace_packages=['opps', 'opps.documents'],
    version=documents.__version__,
    description=documents.__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='upload documents opps cms django apps magazines websites',
    author=documents.__author__,
    author_email=documents.__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-documents/tarball/master",
    license=documents.__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
    include_package_data=True,
)
