import pytest
from actions import *
import os
from pathlib import Path

def test_ListNameEdit():
    if os.path.exists('lists.json'):
        os.remove('lists.json')
    createListList()
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
    if os.path.exists('lists.json'):
        os.remove('lists.json')

def test_insert():
    if os.path.exists('lists.json'):
        os.remove('lists.json')
    createListList()
    #remove json files incase they exist
    if os.path.exists('test.json'):
        os.remove('test.json')
    
    new('test.json')
    insert('test.json', 'task', 1)
    assert json.loads(open('test.json').read())['tasks'][0] == ['task', 1]

    insert('test.json', 'task2', 2)
    
    assert json.loads(open('test.json').read())['tasks'][1] == ['task2', 2]

    insert('test.json', 'task1', 2)
    
    assert (json.loads(open('test.json').read())['tasks'][0] == ['task', 1]) and (json.loads(open('test.json').read())['tasks'][1] == ['task1', 2]) and (json.loads(open('test.json').read())['tasks'][2] == ['task2', 3])

    temp = json.loads(open('test.json').read())['tasks']

    insert('test.json', 'task3', 5)
    assert json.loads(open('test.json').read())['tasks'] == temp # should not change the list

    #cleanup
    if os.path.exists('test.json'):
        os.remove('test.json')
    
    if os.path.exists('lists.json'):
        os.remove('lists.json')

def test_changeListListPath():
    if os.path.exists('lists.json'):
        os.remove('lists.json')
    createListList()

    # Create 2 lists
    new('test.json')
    new('test2.json')

    # add tasks to lists
    addToList('test.json', 'task')
    addToList('test2.json', 'task2')

    # change path of listList
    changeListListPath('listList/listOfLists.json')
    assert(os.path.exists('listList/listOfLists.json')) # check if file exists
    assert(not os.path.exists('lists.json')) # check if file was deleted

    # check if the lists file's contents remain the same
    assert('test.json' in json.loads(open('listList/listOfLists.json').read())['lists'])
    assert('test2.json' in json.loads(open('listList/listOfLists.json').read())['lists'])

    # move the lists file to home directory
    path = str(Path.home()) + os.path.sep + 'lists.json'
    changeListListPath(path) # os.path.sep is the path separator, usually / or \
    assert(os.path.exists('lists.json')) # check if file exists
    assert(not os.path.exists('listList/listOfLists.json')) # check if file was deleted

    # check if the lists file's contents remain the same
    assert('test.json' in json.loads(open(path).read())['lists'])
    assert('test2.json' in json.loads(open(path).read())['lists'])

    # cleanup
    if os.path.exists('listOfLists'):
        os.rmdir('listOfLists')
    if os.path.exists('lists.json'):
        os.remove('lists.json')
    if os.path.exists(path):
        os.remove(path)