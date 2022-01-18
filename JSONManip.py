import json, sys

"""def replaceLine(fileName, oldText, text):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    with open(fileName, 'w') as file:
        for line in lines:
            if oldText in line:
                line = line.replace(oldText, text)
            file.write(line)""" #not required

def getFile(filePos):
    try:
        return json.load(open(filePos))
    except FileNotFoundError:
        print('File not found.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()

def changeTODOCount(fileName, add):
    file = getFile(fileName)
    if add:
        file['todos'] += 1
    else:
        file['todos'] -= 1
    #print(file['todos']) #debug
    json.dump(file, open(fileName, 'w'))
    #print(f'TODO count changed to {file["todos"]}.')
    return

def listListAdd(add):
    file = getFile('lists.json')
    file['lists'].append(add)
    json.dump(file, open('lists.json', 'w'))
    
#TEST
#replaceLine('test.txt', 'old', 'new')