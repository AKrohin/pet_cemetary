import argparse
import os


def arguments_parser():
    parser = argparse.ArgumentParser(prog="File name clipper v 1.2.0",
                                     description="Cкрипт оценивает размеры имен файлов в указанной директории, "
                                                 "сравнивает их с указанным пользователем "
                                                 "максимальным размером имени файла "
                                                 "в байтах, выводит список имен файлов, размер которых "
                                                 "превышает указанный пользователем. "
                                                 "Присутствует возможность присвоения новых имен файлам, "
                                                 "размер имени которых больше указанного."
                                                 "Данная функция реализована путем удаления части имени файла, "
                                                 "превышающего указанный пользователем максимум. "
                                                 "В случае, если файл с таким именем уже присутствует "
                                                 "в указанной директории, "
                                                 "к имени файла будет добавлен порядковый номер копии.",
                                     epilog="A. Krokhin, 2022"
                                     )
    parser.add_argument("--folder", "--f", help="Путь к директории", default=None)
    parser.add_argument("--size", "--s", type=int, help="Максимальный размер имени файла в байтах", default=None)
    parser.add_argument("--rename", "--r", help="Аргумент указывает на необходимость обрезать "
                                                "имена файлов до указанного размера",
                        action='store_true', default=None)
    parser.add_argument("--log", "--l", help="Аргумент указывает на необходимость логирования",
                        action='store_true', default=None)
    args = parser.parse_args()
    folder = args.folder
    size = args.size
    rename = args.rename
    log = args.log
    return folder, size, rename, log


def input_folder():
    folder = arguments_parser()[0]
    if folder is None:
        folder = str(os.getcwd() + '\\')
    else:
        folder = input("Введите адрес директории: ")
    return folder


def input_size():
    size = arguments_parser()[1]
    if size is not None:
        size = int(arguments_parser()[1])
    if size is None:
        size = int(input("Укажите максимальный размер файла: "))
    return size


count: int = 1


class LongFileName:

    def __init__(self):
        self.size: int = 0
        self.old_name: str = ''
        self.name: str = ''
        self.ext: str = ''

    def rename_file(self):
        if not os.path.exists(folder + self.name + self.ext):
            os.rename(folder + self.old_name, folder + self.name + self.ext)
        else:
            self.name_already_exists(count)

    def name_already_exists(self, _count):
        if not os.path.exists(folder + self.name + ' (' + format(_count) + ')' + self.ext):
            os.rename(folder + self.old_name, folder + self.name + ' (' + format(_count) + ')' + self.ext)
        else:
            _count += 1
            self.name_already_exists(_count)


def input_log():
    if len(get_list_long_names()) > 0:
        log = arguments_parser()[3]
        if log is None:
            log = input("Логировать? y == да, n == нет ")
        return log


def get_list_long_names():
    file = LongFileName()
    list_of_names = []
    for file.old_name in os.listdir(path=folder):
        file.size = int(len(file.old_name.encode('utf-8')))
        file.name, file.ext = os.path.splitext(file.old_name)
        if file.size > size + len(file.ext):
            list_of_names.append(file.old_name)
    return list_of_names


def rename_long_name():
    file = LongFileName()
    for file.old_name in os.listdir(path=folder):
        file.size = len(file.old_name.encode('utf-8'))
        file.name, file.ext = os.path.splitext(file.old_name)
        if file.size > size + len(file.ext):
            print(file.name + file.ext + " - Переименован")
            file.name, file.ext = os.path.splitext(file.old_name)
            while len(file.name + file.ext) > size - len(file.ext):
                file_name_as_list = list(file.name)
                del file_name_as_list[-1]
                file.name = ''.join(file_name_as_list)
            file.rename_file()
        else:
            pass


def input_rename():
    if len(get_list_long_names()) > 0:
        rename = arguments_parser()[2]
        if rename is None:
            rename = input("Переименовать файлы в указанной директории? y == да, n == нет \n")
            if rename == 'y':
                rename = True
            elif rename == 'n':
                rename = False
            else:
                input_rename()
        return rename


folder = input_folder()
size = int(input_size())
if len(get_list_long_names()) > 0:
    print("Следующие имена файлов превышают размер " + format(size) + " байт:")
    print(*get_list_long_names(), sep='\n' + '\n')
else:
    print("В указанной директории отсутствуют файлы, имя которых превышает " + format(size) + " байт.")

if input_rename():
    rename_long_name()
else:
    pass


def log_list_of_big_names():
        get_list_long_names()
        with open("fnc.log", "w", encoding='utf-8') as log:
            print("Файлы в директории " + folder + " , размер которых превышает " + str(size) + " байт: \n", file=log)
            print(*get_list_long_names(), file=log, sep="\n")


if input_log():
    log_list_of_big_names()
else:
    pass


