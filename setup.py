from setuptools import setup, find_packages

setup(
    name='ocf_vrmapi',
    packages=find_packages(),
    version='0.1.2',
    description='Victron python api',
    install_requires=['requests'],
)
