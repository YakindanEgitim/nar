import os
from setuptools import setup, find_packages


def get_content(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name = "nar",
    version = "0.0.1",
    url = "https://github.com/YakindanEgitim/nar",
    license = "GPLv3",
    description = "New Album Reporter",
    long_description = get_content('README.md'),

    author = "Ferhat Elmas, Mesutcan Kurt",
    author_email = "elmas.ferhat@gmail.com",

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)