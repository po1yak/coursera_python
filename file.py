import tempfile
import os

class File:
    """Class to works around files"""
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            open(self.path, 'a').close()

    def __add__(self, obj):
        new_file = os.path.join(tempfile.gettempdir(), 'new_add')
        new_obj = File(new_file)
        new = open(new_file, 'w')
        with open(self.path, 'r') as f:
            for line in f.readlines():
                new.writelines(line)
        with open(obj.path, 'r') as f:
            for line in f.readlines():
                new.writelines(line)
        new.close()
        return new_obj

    def __getitem__(self, index):
        with open(self.path, 'r') as f:
            return f.readlines()[index]

    def __str__(self):
        return self.path

    def write(self, line):
        f = open(self.path, 'a')
        f.writelines(f"{line}")
        f.close
