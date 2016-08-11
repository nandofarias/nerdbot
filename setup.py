from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nerdbot',
    version='0.0.1',
    description='A nerd facebook chatbot',
    long_description=readme,
    author='Fernano Farias',
    author_email='nandofarias@me.com',
    url='https://github.com/NandoFarias/chatbot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
