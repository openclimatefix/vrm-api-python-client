from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='ocf_vrmapi',
    packages=find_packages(),
    version='0.1.3',
    description='Victron python api',
    license='MIT',
    long_description=readme,
    install_requires=['requests'],
)
