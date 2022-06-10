# импортируем библиотеку ос
import os


def rename_long_files():
    def dir_and_max():
        # запрашиваем директорию для сканирования
        p = input('Введите путь к директории: ')
        # запрашиваем максимальный размер имени файла в байтах
        m = int(input('Укажите максимальный размер имени файла в байтах: '))
        path_to_dir = p
        max_size = m
        return path_to_dir, max_size

    path_to_dir, max_size = dir_and_max()

    def scan_dir():
        _len = []
        # сканируем директорию
        for file in os.listdir(path_to_dir):
            # проверяем превышает ли размер имени файла указанное значение
            if len(file.encode('utf-8')) > max_size:
                # формируем массив из имен файлов, которые нужно переиеновать
                _len.append(file)
        return _len

    list_of_the_files = scan_dir()
    if len(list_of_the_files) > 0:
        print('Следующие файлы из указанной директории подлежат переименованию: ')
        print(*list_of_the_files, sep='\n', end='\n\n')

        # выбираем файл из указанной директории, размер которого превышает указанный максимум
        def new_names(list_of_the_files, max_size):
            n = []
            for file in list_of_the_files:
                file, ext = os.path.splitext(file)
                new_name = list(file)
                # пока длина имени > указанный размер + длина расширения + точка:
                while len(file.encode('utf-8')) > max_size + len(ext) + 1:
                    # удаляем по одному символу из имени файла, пока он не станет допустимого размера
                    del new_name[-1]
                    file = ''.join(new_name)
                n.append(file)
            return n

        # при обнаружении одинаковых имен файлов
        def name_already_exists(path_to_dir, new_name, ext, c):
            # присваиваем значение счетчика, если такого имени нет в директории
            if os.path.exists(path_to_dir + new_name + ' (' + format(c) + ')' + ext) is False:
                os.rename(path_to_dir + old, path_to_dir + new_name + ' (' + format(c) + ')' + ext)
            else:
                # увеличиваем счетчик на 1 и рекурсивно вызываем функцию
                c += 1
                name_already_exists(path_to_dir, new_name, ext, c)

        user_answer = input('Вы хотите изменить длину имени указанных файлов? Да - y, нет - n: ')
        if user_answer == 'y':
            # присваиваем файлу новое имя
            i = 0
            c = 1
            new_name: str
            for new_name in list_of_the_files:
                only_name, ext = os.path.splitext(list_of_the_files[i])
                old = str(list_of_the_files[i])
                new_name = (new_names(list_of_the_files, max_size)[i])
                a = list(new_name)
                if os.path.exists(path_to_dir + new_name + ext):
                    c += 1
                    # отнимаем 1. пробел, 2. скобка, 3. счетчик, 4. скобка
                    for new_name in range(4 + len(format(c))):
                        del a[-1]
                        new_name = ''.join(a)
                    name_already_exists(path_to_dir, new_name, ext, c)
                else:
                    os.rename(path_to_dir + old, path_to_dir + new_name + ext)
                i += 1
        elif user_answer == 'n':
            want_another_dir = input('Вы хотите выполнить поиск в другой директории? Да - y, нет - n: ')
            if want_another_dir == 'y':
                rename_long_files()
            elif want_another_dir == 'n':
                print('(c) A. Krokhin development. No rights is reserved. Opensource forever.')
                exit()
        print('Файлы успешно переименованы!')
        want_another_dir = input('Вы хотите выполнить поиск в другой директории? Да - y, нет - n: ')
        if want_another_dir == 'y':
            rename_long_files()
        elif want_another_dir == 'n':
            print('(c) A. Krokhin development. No rights is reserved. Opensource forever.')
            exit()
    else:
        print('Имена файлов в указанной директории не превышают указанного размера. '
              'Повторить поиск в другой директории?: ')
        want_another_dir = input('Вы хотите выполнить поиск в другой директории? Да - y, нет - n: ')
        if want_another_dir == 'y':
            rename_long_files()
        elif want_another_dir == 'n':
            print('(c) A. Krokhin development. No rights is reserved. Opensource forever.')
            exit()


rename_long_files()
