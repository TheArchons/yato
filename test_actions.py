import pytest
from actions import *
import os

def test_ListNameEdit():
    #remove json files incase they exist
    if os.path.exists('test.json'):
        os.remove('test.json')
    if os.path.exists('test2.json'):
        os.remove('test2.json')
    if os.path.exists('asd.txt'):
        os.remove('asd.txt')
    if os.path.exists('111.json'):
        os.remove('111.json')

    open('test.json', 'w').close()

    ListNameEdit('test.json', 'test2.json')
    assert os.path.exists('test2.json')

    ListNameEdit('test2.json', 'test2.json')
    assert os.path.exists('test2.json')

    ListNameEdit('test2.json', 'asd.txt')
    assert os.path.exists('asd.txt')

    ListNameEdit('asd.txt', 'asd.txt')
    assert os.path.exists('asd.txt')

    ListNameEdit('asd.txt', '111.json')
    assert os.path.exists('111.json')

    ListNameEdit('111.json', 'test.json')
    assert os.path.exists('test.json')

    os.remove('test.json')

    #cleanup
    if os.path.exists('test.json'):
        os.remove('test.json')
    if os.path.exists('test2.json'):
        os.remove('test2.json')
    if os.path.exists('asd.txt'):
        os.remove('asd.txt')
    if os.path.exists('111.json'):
        os.remove('111.json')