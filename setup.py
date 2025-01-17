""""
    Setup for Case Recommender

"""

# © 2019. Case Recommender (MIT License)

from distutils.core import setup
from setuptools import find_packages
from os import path

here = path.abspath(path.dirname(__file__))

__author__ = 'Arthur Fortes <fortes.arthur@gmail.com>'

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get requiriments
REQUIRED_PACKAGES = [
    'numpy',
    'scipy',
    'scikit-learn',
    'pandas'
]

setup(
    name='CaseRecommender',
    packages=find_packages(),
    version='1.1.1',
    license='MIT License',
    description='A recommender systems framework for Python',
    long_description=long_description,
    install_requires=REQUIRED_PACKAGES,
    author='Mohamed Amine EL MOUSSAOUI',
    author_email='maelmoussaoui1@gmail.com',
    url='https://github.com/MOSSAWIII/CaseRecommender',
    download_url='https://github.com/MOSSAWIII/CaseRecommender/archive/master.zip',
    keywords=['recommender systems', 'framework', 'collaborative filtering', 'content-based filtering',
              'recommendation'],

    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
)


setup(
        # ... rest of the configuration
)