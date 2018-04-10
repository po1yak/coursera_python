import tempfile
import os

class File:
    """Class to works around files"""
    def __init__(self, path):
        self.path = path

    def __add__(self, obj):
        new_file = os.path.join(tempfile.gettempdir(), 'new_add')
        with open(obj.path, 'r') as f:
            txt = f.read()
        with open(self.path, 'r') as f:
            txt2 = f.read()
            txt2 = txt2 + txt
        with open(new_file, 'w') as f:
            f.write(txt2)
        return File(new_file)

    def __iter__(self):
        f = open(self.path)
        return f

    def __next__(self):
        with open(self.path, 'r') as f:
            return f.readline()

    def __str__(self):
        return self.path

    def write(self, line):
        with open(self.path, 'a') as f:
            f.writelines(line + "\n")
