from setuptools import setup, find_packages

setup(
    name='DevRandom',
    version='0.1.0',
    author='Byron D Peebles',
    author_email='byron.peebles@gmail.com',
    packages = find_packages(),
    scripts=[],
    url='http://github.org/bpeebles/devrandom',
    license='LICENSE.txt',
    description='Wrapper around /dev/random',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
)
