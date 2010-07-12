from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'daffy',
    version = version,
    description = 'Scheme in Python',
    author = 'Scott Nelson',
    author_email = 'scottbnel@gmail.com',
    url = 'http://www.github.com/scottbnel/daffy/',
    packages = find_packages(),
    install_requires = ['ply>=3.3'],
    zip_safe = True,
    scripts = ['bin/daffy']
)
