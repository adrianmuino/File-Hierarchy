# Pass a path that is a directory as a command-line argument
import os, sys, json

def getfile(path):
    file = { 'name': os.path.basename(path),
        'type': 'File',
        'path': path
    }
    return file

def getdir(path):
    dir_ = { 'name': os.path.basename(path),
        'type': 'Dir',
        'path': path
    }
    list = [os.path.join(path,item) for item in os.listdir(path)]
    is_dir = os.path.isdir # alias
    dir_['sub_dir'] = [getdir(p) if is_dir(p) else getfile(p) for p in list]
    return dir_


if len(sys.argv) == 2:
    path = sys.argv[1]
    if os.path.isdir(path):
        with open('struct.dat', 'w') as fh:
            hierarchy = getdir(path)
            json.dump(hierarchy, fh, indent = 2)
        print('JSON File successfully created!')
    else:
        print('Entered directory does not exist.')
else:
    print('Try again by entering only one path...')

