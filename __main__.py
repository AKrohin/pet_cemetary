import input_data
from find_file import list_of_big_names, rename_long_name


def main():
    list_of_names, path, max_size = list_of_big_names()
    if len(list_of_names) > 0:
        list_of_big_names()
        with open("log.txt", "w") as log:
            print("Файлы в директории " + path + " , размер которых превышает " + str(max_size) + " байт: \n", file=log)
            print(*list_of_names, file=log, sep="\n")
        print('Следующие файлы имеют размер имени, превышающий указанный: \n')
        print(*list_of_names, sep="\n")
        rename = input_data.args.rename
        if rename is None:
            rename = input("Переименовать найденные файлы?: y - да, n - нет ")
            if rename == 'y':
                rename_long_name()
        else:
            rename = input_data.args.rename
            if rename == 'y':
                rename_long_name()
            else:
                pass
    else:
        print("В директории '" + path + "' отсутствуют файлы, имя которых превышает " + format(max_size) + " байт \n")


if __name__ == '__main__':
    main()
