import pytest
from actions import *
import os

def test_ListNameEdit():
    createListList()  # create lists.json if it doesn't exist
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
    assert ('tests2.json' in json.loads(open('lists.json').read())['lists']) and not ('test.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('test2.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('tests2.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('test2.json', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists']) and not ('test2.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('asd.txt', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('asd.txt', '111.json')
    assert os.path.exists('111.json')
    assert ('111.json' in json.loads(open('lists.json').read())['lists']) and not ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('111.json', 'test.json')
    assert os.path.exists('test.json')
    assert ('test.json' in json.loads(open('lists.json').read())['lists']) and not ('111.json' in json.loads(open('lists.json').read())['lists'])

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