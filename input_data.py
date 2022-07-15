import argparse
import os

parser = argparse.ArgumentParser(prog="File name clipper v 1.2",
                                 description="Данный скрипт оценивает размеры имен файлов в указанной директории, "
                                             "сравнивает их с указанным пользователем максимальным размером имени файла "
                                             "в байтах, выводит список имен файлов, размер которых превышает указанный пользователем. "
                                             "Присутствует возможность присвоения новых имен файлам, размер имени которых больше указанного."
                                             "Данная функция реализована путем удаления части имени файла, превышающего указанный пользователем максимум. ",
                                 epilog="A. Krokhin, 2022"
                                 )
parser.add_argument("--folder", "--f", help="Путь к директории", default=os.getcwd())
parser.add_argument("--size", "--s", type=int, help="Максимальный размер имени файла в байтах")
parser.add_argument("--rename", "--r", type=str, help="Если для аргумента установлен атрибут y - найденные файлы будут переименованы", default="n")
args = parser.parse_args()

if args.folder is None:
    path = input("Укажите путь к директории: ")
else:
    path = args.folder

if args.size is None:
    max_size = int(input("Укажите максимальный размер имен файла в байтах: "))
else:
    max_size = args.size



