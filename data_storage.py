import argparse
import tempfile
import json
import os

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def read_json(storage_path):
    """Read JSON from file"""
    with open(storage_path, 'r') as file_storage:
        return json.load(file_storage)

def write_file(storage_path, tmp_dict):
    """Write JSON to file"""
    with open(storage_path, 'w') as file_storage:
        json.dump(tmp_dict, file_storage)

def add_keypair(key, value, cur_stor):
    """Add keypair into the data storage"""
    if key in cur_stor:
        cur_stor[key].append(value)
    else:
        cur_stor[key] = []
        cur_stor[key].append(value)
    return cur_stor

def search_keypair(key, cur_stor):
    """Search and return keypair in the data storage"""
    if key in cur_stor:
        return(', '.join(cur_stor[key]))
    else:
        return 'None'


parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True, help='This will be prefix for the key')
parser.add_argument('--val', help='This will be prefix for the value')

arg = parser.parse_args()

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as file_storage:
        pass

if os.path.getsize(storage_path) > 0:
    if arg.val:
        cur_stor = read_json(storage_path)
        result = add_keypair(arg.key, arg.val, cur_stor)
        write_file(storage_path, result)
    else:
        cur_stor = read_json(storage_path)
        print(search_keypair(arg.key, cur_stor))
else:
    if arg.val:
        result = add_keypair(arg.key, arg.val, {})
        write_file(storage_path, result)
    else:
        print('None')
