import os
from input_data import *

count: int = 0


class LongFileName:

    def __init__(self):
        self.size: int = 0
        self.old_name: str = ''
        self.name: str = ''
        self.ext: str = ''

    def rename_file(self):
        if not os.path.exists(path + self.name + self.ext):
            os.rename(path + self.old_name, path + self.name + self.ext)
        else:
            self.name_already_exists(count)

    def name_already_exists(self, _count):
        if not os.path.exists(path + self.name + ' (' + format(_count) + ')' + self.ext):
            os.rename(path + self.old_name, path + self.name + ' (' + format(_count) + ')' + self.ext)
        else:
            _count += 1
            self.name_already_exists(_count)
