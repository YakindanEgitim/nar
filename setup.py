from setuptools import setup, find_packages

setup(
    name = "nar",
    version = "0.0.1",
    url = "https://github.com/YakindanEgitim/nar",
    description = "New Album Reporter",
    author = "Ferhat Elmas, Mesutcan Kurt",
    license = "GPLv3",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools',
                        'django',
                        'django-social-auth',
                        'django-bootstrap-toolkit'],
)