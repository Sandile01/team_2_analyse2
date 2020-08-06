from setuptools import setup, find_packages

setup(
    name='team_2_analyse',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='7 Functions for eskom Data',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/<SandileS>/<the_7_functions.py>',
    author='<Mkhabela Sandile>',
    author_email='<saintsandile01@gmail.com>'
)