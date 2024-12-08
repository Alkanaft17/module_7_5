from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


def show_path_info(directory):
    '''
    выводит информацию о файлах в указанной директории
    root - корень
    dirs - директории
    files - файлы
    '''
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)  # объединение путей root и file
            filetime = getmtime(file)    # время секундах с момента создания файла
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime)) # время в вформате дата месяц год часы минуты
            filesize = getsize(filepath) # размер файла
            parent_dir = dirname(filepath)

            print(f'Обнаружен файл: {file},',
                  f'Путь: {filepath},',
                  f'Размер: {filesize} байт,',
                  f'Время изменения: {formatted_time},',
                  f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    show_path_info('.')