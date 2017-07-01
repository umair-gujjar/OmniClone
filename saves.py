#!/usr/local/bin/python3.6
import json
from ocObjects import *


# saves objects in list to file
def save_to_file(ocList, path):
    file = open(path, 'w')
    if path in ['actions.txt', 'inbox.txt', 'projects.txt']:
        for item in ocList:
            json_str = json.dumps(item.__dict__)			# convert data to encoded string
            file.write(json_str + '\n')				# write encoded string to .txt
    elif path in ['tags.txt']:
        for item in ocList:
            file.write(item + '\n')
    else:
        print('OC ERROR: Could not save file. Given PATH doesn\'t exist')
    file.close()


# loads objects from file into list
def load_from_file(ocList, path):
    file = open(path, 'r')
    if path in ['actions.txt', 'inbox.txt', 'projects.txt']:
        for line in file.readlines():
            ocList.append(json.loads(line[0:-1]))			# load json from file into var
    elif path in ['tags.txt']:
        for line in file.readlines():
            ocList.append(line[0:-1])
    else:
        print('OC ERROR: Could not load file. Given PATH doesn\'t exist')
    file.close()


def load_ocObjects():
    for key in files.keys():
        load_from_file(files[key], key)


def save_ocObjects():
    for key in files.keys():
        save_to_file(files[key], key)
