import os
from name_file import LongFileName
from input_data import path, max_size


def list_of_big_names():
    file = LongFileName()
    list_of_names = []
    for file.old_name in os.listdir(path=path):
        file.size = len(file.old_name.encode('utf-8'))
        file.name, file.ext = os.path.splitext(file.old_name)
        if file.size > max_size + 4:
            list_of_names.append(file.old_name)
    return list_of_names, path, max_size

def rename_long_name():
    file = LongFileName()
    print('Следующие файлы были переименованы: \n')
    for file.old_name in os.listdir(path=path):
        file.size = len(file.old_name.encode('utf-8'))
        file.name, file.ext = os.path.splitext(file.old_name)
        if file.size > max_size + 4:
            print(file.name + file.ext + " - Переименован\n")
            file.name, file.ext = os.path.splitext(file.old_name)
            while len(file.name + file.ext) > max_size + 4:
                file_name_as_list = list(file.name)
                del file_name_as_list[-1]
                file.name = ''.join(file_name_as_list)
            file.rename_file()
        else:
            pass
