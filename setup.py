"""Setuptools config for yato."""

from setuptools import setup

setup(
    name='yato',
    version='1.3.0',
    description='yato - Yet another Todo app, a cli program for TODO lists',
    url="https://github.com/TheArchons/yato",
    author='TheArchons',
    author_email='alexli9138@gmail.com',
    license='MIT',
    packages=['yato'],
    install_requires=['termcolor'],
    entry_points={'console_scripts': ['yato=yato.actions:main']},
    keywords=['yato', 'todo', 'list', 'tasks'],
)
