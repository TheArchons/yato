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
    assert ('test2.json' in json.loads(open('lists.json').read())['lists']) and not ('test.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('test2.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('test2.json' in json.loads(open('lists.json').read())['lists'])

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

def test_insert():
    createListList()
    #remove json files incase they exist
    if os.path.exists('test.json'):
        os.remove('test.json')
    
    new('test.json')
    insert('test.json', 'task', '1')
    assert json.loads(open('test.json').read())['tasks'][0] == 'task'

    insert('test.json', 'task2', '2')
    assert json.loads(open('test.json').read())['tasks'][1] == 'task2'

    insert('test.json', 'task1', '2')
    assert (json.loads(open('test.json').read())['tasks'][1] == 'task1') and (json.loads(open('test.json').read())['tasks'][2] == 'task2')

    temp = json.loads(open('test.json').read())['tasks']

    insert('test.json', 'task3', '5')
    assert json.loads(open('test.json').read())['tasks'] == temp # should not change the list

    #cleanup
    if os.path.exists('test.json'):
        os.remove('test.json')