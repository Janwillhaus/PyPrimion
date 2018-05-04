#!/usr/bin/env python3

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Get requirements and testsuite requirements from Pipfile
pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)


setup(name='PyPrimion',
      version='0.3',
      description='Webinterface handler for the Primion Prime Web Systems time tracking',

      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',

      url='https://github.com/janwh/PyPrimion',
      author='Jan Willhaus',
      author_email='mail@janwillhaus.de',
      install_requires=requirements,
      tests_require=requirements + test_requirements,
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: System :: Recovery Tools',

          # Pick your license as you wish
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],

      keywords='primion timetracking primeweb',  # Optional

      py_modules=['pyprimion'],
      packages=None,
      python_requires='>=3',

      entry_points={
          'console_scripts': [
              'pyprimion = pyprimion:cli',
          ],
      },
      project_urls={
          'Bug Reports': 'https://github.com/janwh/PyPrimion/issues',
          'Funding': 'https://liberapay.com/janw',
          'Say Thanks!': 'https://saythanks.io/to/janwh',
          'Source': 'https://github.com/janwh/PyPrimion/',
      },
)
